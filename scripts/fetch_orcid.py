#!/usr/bin/env python3
"""
Fetch publications from a public ORCID record, enrich them via Crossref, and
write _data/publications.yml for Jekyll to render.

Run locally:   python scripts/fetch_orcid.py
Run in CI:     see .github/workflows/update-publications.yml

No API key required — both ORCID's public API and Crossref are open.
"""

import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

# ----------------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------------
ORCID_ID = "0000-0002-0672-8903"
CONTACT_EMAIL = "w.b.bruin@amsterdamumc.nl"   # Crossref "polite pool" identifier

# Your name, for bolding in author lists. Matched per author entry, so a
# co-author called "de Bruin" will not be bolded by mistake.
HIGHLIGHT_FAMILY = "bruin"
HIGHLIGHT_GIVEN_PREFIX = "w"
# ----------------------------------------------------------------------------

OUT_PATH = Path("_data/publications.yml")

KEEP_TYPES = {
    "journal-article",
    "preprint",
    "book-chapter",
    "book",
    "conference-paper",
    "dissertation-thesis",
    "review",
    "data-set",
    "software",
    "other",
}


# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------
def get_json(url, headers=None, retries=3):
    req = urllib.request.Request(url, headers=headers or {})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == retries - 1:
                print(f"  ! HTTP {e.code} for {url}", file=sys.stderr)
                return None
            time.sleep(2 ** attempt)
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                print(f"  ! {e} for {url}", file=sys.stderr)
                return None
            time.sleep(2 ** attempt)
    return None


def dig(obj, *keys, default=None):
    cur = obj
    for k in keys:
        if not isinstance(cur, dict) or cur.get(k) is None:
            return default
        cur = cur[k]
    return cur if cur is not None else default


# --------------------------------------------------------------------------
# ORCID
# --------------------------------------------------------------------------
def fetch_orcid_works(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    data = get_json(url, headers={"Accept": "application/json"})
    if not data:
        sys.exit(
            f"Could not read ORCID record {orcid_id}.\n"
            "Check the iD is correct and that your works are set to "
            "'Everyone' visibility in your ORCID privacy settings."
        )

    summaries = []
    for group in data.get("group", []):
        works = group.get("work-summary", [])
        if not works:
            continue
        # One group = one publication, possibly claimed from several sources.
        # Prefer whichever entry carries a DOI.
        best = next((w for w in works if extract_doi(w)), works[0])
        summaries.append(best)
    return summaries


def extract_doi(summary):
    ids = dig(summary, "external-ids", "external-id", default=[]) or []
    for eid in ids:
        if (eid.get("external-id-type") or "").lower() == "doi":
            val = eid.get("external-id-value")
            if val:
                return val.strip().lower().replace("https://doi.org/", "")
    return None


# --------------------------------------------------------------------------
# Author formatting
# --------------------------------------------------------------------------
def is_self(family, given):
    return (
        family.strip().lower() == HIGHLIGHT_FAMILY
        and given.strip().lower().startswith(HIGHLIGHT_GIVEN_PREFIX)
    )


def format_authors(authors):
    """Normalised author dicts -> 'Bruin, W.B., van den Heuvel, O.A., ...'

    Accepts entries with family/given, or a single 'name' field. Returns
    (full, short). The matching author is wrapped in <strong> individually,
    which avoids partial matches inside names like 'de Bruin'.
    """
    out = []
    self_index = None
    for a in authors:
        family = (a.get("family") or "").strip()
        given = (a.get("given") or "").strip()

        if not family:
            name = (a.get("name") or "").strip()
            if name:
                out.append(name)
            continue

        initials = "".join(
            f"{p[0]}." for p in re.split(r"[\s\-]+", given) if p
        )
        entry = f"{family}, {initials}" if initials else family
        if is_self(family, given):
            entry = f"<strong>{entry}</strong>"
            self_index = len(out)
        out.append(entry)

    return ", ".join(out), ", ".join(shorten_authors(out, self_index))


def shorten_authors(entries, self_index, threshold=8):
    """Trim long consortium author lists to something readable.

    Keeps the first three authors, your own name wherever it falls, and the
    final (usually senior) author, with ellipses marking the gaps:
    'Bruin, W.B., Taylor, L., Thomas, R.M., … van Wingen, G.A.'
    """
    n = len(entries)
    if n <= threshold:
        return entries

    keep = {0, 1, 2, n - 1}
    if self_index is not None:
        keep.add(self_index)

    out, prev = [], None
    for i in sorted(keep):
        if prev is not None and i > prev + 1:
            out.append("&hellip;")
        out.append(entries[i])
        prev = i
    return out


# --------------------------------------------------------------------------
# Crossref
# --------------------------------------------------------------------------
def fetch_datacite(doi):
    """Zenodo, figshare and other DataCite DOIs are not in Crossref at all."""
    url = "https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe="")
    data = get_json(url, headers={"Accept": "application/vnd.api+json"})
    return dig(data or {}, "data", "attributes")


def fetch_orcid_work_detail(orcid_id, put_code):
    """Last resort: the full ORCID work record sometimes lists contributors."""
    if not put_code:
        return None
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/work/{put_code}"
    return get_json(url, headers={"Accept": "application/json"})


def authors_from_crossref(cr):
    out = []
    for a in (cr.get("author") or []):
        out.append({"family": a.get("family") or "",
                    "given": a.get("given") or "",
                    "name": a.get("name") or ""})
    return out


def authors_from_datacite(att):
    out = []
    for c in (att.get("creators") or []):
        out.append({"family": c.get("familyName") or "",
                    "given": c.get("givenName") or "",
                    "name": c.get("name") or ""})
    return out


def authors_from_orcid_detail(detail):
    out = []
    contribs = dig(detail or {}, "contributors", "contributor", default=[]) or []
    for c in contribs:
        name = dig(c, "credit-name", "value", default="")
        if not name:
            continue
        # ORCID credit names arrive in mixed formats; keep them verbatim
        out.append({"family": "", "given": "", "name": name})
    return out


# Venues that mean "preprint" regardless of how ORCID typed the record
PREPRINT_VENUES = (
    "research square", "biorxiv", "medrxiv", "arxiv", "ssrn",
    "preprints.org", "osf preprints", "psyarxiv",
)


def looks_like_preprint(journal, wtype):
    if wtype in ("preprint", "working-paper"):
        return True
    return any(v in (journal or "").lower() for v in PREPRINT_VENUES)


def fetch_crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    headers = {"User-Agent": f"personal-site/1.0 (mailto:{CONTACT_EMAIL})"}
    data = get_json(url, headers=headers)
    return (data or {}).get("message")


def year_from_orcid(summary):
    y = dig(summary, "publication-date", "year", "value")
    try:
        return int(y)
    except (TypeError, ValueError):
        return None


def build_record(summary, orcid_id=ORCID_ID):
    doi = extract_doi(summary)
    put_code = summary.get("put-code")
    title = dig(summary, "title", "title", "value", default="").strip()
    journal = (dig(summary, "journal-title", "value") or "").strip()
    year = year_from_orcid(summary)
    wtype = (summary.get("type") or "other").lower().replace("_", "-")
    authors = ""
    authors_short = ""
    citations = 0
    url = dig(summary, "url", "value") or ""

    people = []

    if doi:
        cr = fetch_crossref(doi)
        time.sleep(0.2)  # be polite to the API
        if cr:
            title = (cr.get("title") or [title])[0] or title
            container = cr.get("container-title") or []
            journal = container[0] if container else journal
            people = authors_from_crossref(cr)
            citations = cr.get("is-referenced-by-count", 0) or 0
            parts = dig(cr, "issued", "date-parts", default=[[]])
            if parts and parts[0]:
                year = parts[0][0]
            if cr.get("type") == "posted-content":
                wtype = "preprint"

        # Zenodo/figshare DOIs are registered with DataCite, not Crossref,
        # and versioned Research Square DOIs often miss in Crossref too.
        if not people:
            att = fetch_datacite(doi)
            time.sleep(0.2)
            if att:
                people = authors_from_datacite(att)
                journal = journal or (att.get("publisher") or "")
                if not year:
                    year = att.get("publicationYear") or year
                print(f"      (authors via DataCite)")

        url = f"https://doi.org/{doi}"

    # Final fallback: the full ORCID record occasionally lists contributors
    if not people:
        detail = fetch_orcid_work_detail(orcid_id, put_code)
        time.sleep(0.2)
        people = authors_from_orcid_detail(detail)
        if people:
            print(f"      (authors via ORCID record)")

    if people:
        authors, authors_short = format_authors(people)

    if looks_like_preprint(journal, wtype):
        wtype = "preprint"

    return {
        "title": re.sub(r"\s+", " ", title).strip(),
        "authors": authors,
        "authors_short": authors_short,
        "journal": journal,
        "year": year,
        "type": wtype,
        "doi": doi or "",
        "url": url,
        "citations": citations,
    }


# --------------------------------------------------------------------------
# Post-processing
# --------------------------------------------------------------------------
def norm_title(t):
    t = unicodedata.normalize("NFKD", t.lower())
    return re.sub(r"[^a-z0-9]+", "", t)


CORRECTION_RE = re.compile(
    r"^\s*(author\s+)?(correction|corrigendum|erratum|retraction)\b[:\s]", re.I
)


def is_correction(title):
    return bool(CORRECTION_RE.match(title))


def same_work(a, b):
    """Do two normalised titles refer to the same paper?

    Handles the common cases: identical titles differing only in case or
    punctuation, and preprints whose subtitle changed before publication.
    """
    if a == b:
        return True
    if len(a) >= 40 and len(b) >= 40:
        if a.startswith(b[:50]) or b.startswith(a[:50]):
            return True
    return SequenceMatcher(None, a, b).ratio() >= 0.88


def record_rank(r):
    """Higher is better. Used to pick the canonical copy of a duplicated work."""
    return (
        0 if r["type"] == "preprint" else 1,
        1 if r["journal"] else 0,
        1 if r["authors"] else 0,
        r["citations"],
        r["year"] or 0,
    )


def deduplicate(records):
    """Collapse duplicate entries of the same work, keeping the best copy.

    ORCID often holds several entries per paper: a preprint, the published
    version, and sometimes copies claimed from different sources with
    different DOIs. This groups them and keeps the most complete record.
    """
    clusters = []
    for r in records:
        key = norm_title(r["title"])
        for c in clusters:
            if same_work(key, c["key"]):
                c["items"].append(r)
                break
        else:
            clusters.append({"key": key, "items": [r]})

    kept = []
    for c in clusters:
        best = max(c["items"], key=record_rank)
        if len(c["items"]) > 1:
            others = len(c["items"]) - 1
            print(f"    merged {others} duplicate(s) of: {best['title'][:55]}")
        kept.append(best)
    return kept


def to_yaml(records):
    """Minimal YAML writer, so CI needs no third-party dependencies."""
    def esc(v):
        return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'

    lines = [
        "# AUTO-GENERATED by scripts/fetch_orcid.py — do not edit by hand.",
        f"# Source: https://orcid.org/{ORCID_ID}",
        "",
    ]
    for r in records:
        lines.append(f"- title: {esc(r['title'])}")
        for key in ("authors", "authors_short", "journal", "type", "doi", "url"):
            lines.append(f"  {key}: {esc(r[key])}")
        lines.append(f"  year: {r['year'] if r['year'] else 'null'}")
        lines.append(f"  citations: {r['citations']}")
        lines.append("")
    return "\n".join(lines)


def main():
    print(f"Reading ORCID {ORCID_ID} ...")
    summaries = fetch_orcid_works(ORCID_ID)
    print(f"  {len(summaries)} work groups found")

    records = []
    skipped_corrections = 0
    for s in summaries:
        wtype = (s.get("type") or "other").lower().replace("_", "-")
        if wtype not in KEEP_TYPES:
            print(f"  (skipping type '{wtype}')")
            continue
        rec = build_record(s)
        if not rec["title"]:
            continue
        if is_correction(rec["title"]):
            skipped_corrections += 1
            continue
        records.append(rec)
        print(f"  · {rec['year']} — {rec['title'][:68]}")

    if skipped_corrections:
        print(f"  (skipped {skipped_corrections} correction/erratum notice(s))")

    print("\nDeduplicating ...")
    records = deduplicate(records)
    records.sort(key=lambda r: (r["year"] or 0), reverse=True)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(to_yaml(records), encoding="utf-8")
    print(f"\nWrote {len(records)} publications to {OUT_PATH}")


if __name__ == "__main__":
    main()
