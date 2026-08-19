#!/usr/bin/env python3
"""
Derive the list of collaborating countries from the publication list.

Reads _data/publications.yml (written by fetch_orcid.py), asks OpenAlex which
institutions authored each paper, and writes _data/collaborations.yml with one
entry per country.

Why OpenAlex rather than Crossref: Crossref affiliation data is sparse and
inconsistent, especially for large consortium papers. OpenAlex resolves author
affiliations to institutions with country codes and covers these papers well.

Run:  python scripts/fetch_collaborations.py
"""

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CONTACT_EMAIL = "w.b.bruin@amsterdamumc.nl"   # OpenAlex polite pool
HOME_COUNTRY = "NL"

PUBS = Path("_data/publications.yml")
OUT = Path("_data/collaborations.yml")

# Representative coordinates per country, for plotting. Only countries listed
# here can appear on the map; add more as needed.
COORDS = {
    "NL": (52.2, 5.3, "Netherlands"),      "BE": (50.6, 4.6, "Belgium"),
    "DE": (51.2, 10.4, "Germany"),         "FR": (46.6, 2.4, "France"),
    "GB": (54.0, -2.0, "United Kingdom"),  "IE": (53.2, -8.0, "Ireland"),
    "ES": (40.3, -3.7, "Spain"),           "PT": (39.6, -8.0, "Portugal"),
    "IT": (42.8, 12.6, "Italy"),           "CH": (46.8, 8.2, "Switzerland"),
    "AT": (47.6, 14.1, "Austria"),         "NO": (61.0, 8.5, "Norway"),
    "SE": (62.0, 15.0, "Sweden"),          "DK": (56.1, 9.5, "Denmark"),
    "FI": (64.0, 26.0, "Finland"),         "PL": (52.0, 19.3, "Poland"),
    "CZ": (49.8, 15.5, "Czechia"),         "GR": (39.0, 22.0, "Greece"),
    "TR": (39.0, 35.2, "Turkey"),          "IL": (31.5, 34.8, "Israel"),
    "RU": (57.0, 60.0, "Russia"),          "UA": (49.0, 32.0, "Ukraine"),
    "US": (39.5, -98.4, "United States"),  "CA": (56.1, -106.3, "Canada"),
    "MX": (23.6, -102.6, "Mexico"),        "BR": (-14.2, -51.9, "Brazil"),
    "AR": (-38.4, -63.6, "Argentina"),     "CL": (-35.7, -71.5, "Chile"),
    "CO": (4.6, -74.3, "Colombia"),        "ZA": (-30.6, 22.9, "South Africa"),
    "EG": (26.8, 30.8, "Egypt"),           "NG": (9.1, 8.7, "Nigeria"),
    "KE": (-0.0, 37.9, "Kenya"),           "IN": (20.6, 79.0, "India"),
    "CN": (35.9, 104.2, "China"),          "JP": (36.2, 138.3, "Japan"),
    "KR": (35.9, 127.8, "South Korea"),    "TW": (23.7, 121.0, "Taiwan"),
    "SG": (1.35, 103.8, "Singapore"),      "TH": (15.9, 101.0, "Thailand"),
    "ID": (-0.8, 113.9, "Indonesia"),      "AU": (-25.3, 133.8, "Australia"),
    "NZ": (-40.9, 174.9, "New Zealand"),   "IR": (32.4, 53.7, "Iran"),
    "SA": (23.9, 45.1, "Saudi Arabia"),    "AE": (23.4, 53.8, "UAE"),
}


def get_json(url, headers=None, retries=3):
    req = urllib.request.Request(url, headers=headers or {})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == retries - 1:
                print(f"  ! HTTP {e.code} {url}", file=sys.stderr)
                return None
            time.sleep(2 ** attempt)
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                print(f"  ! {e}", file=sys.stderr)
                return None
            time.sleep(2 ** attempt)
    return None


def read_dois():
    if not PUBS.exists():
        sys.exit("_data/publications.yml not found. Run fetch_orcid.py first.")
    return re.findall(r'^\s*doi:\s*"([^"]+)"', PUBS.read_text(encoding="utf-8"), re.M)


def countries_for(doi):
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="")
    url += "?mailto=" + urllib.parse.quote(CONTACT_EMAIL)
    data = get_json(url, headers={"User-Agent": f"personal-site/1.0 ({CONTACT_EMAIL})"})
    if not data:
        return set()
    found = set()
    for a in data.get("authorships", []):
        for c in (a.get("countries") or []):
            found.add(c)
        for inst in (a.get("institutions") or []):
            if inst.get("country_code"):
                found.add(inst["country_code"])
    return found


def main():
    dois = [d for d in read_dois() if d]
    print(f"{len(dois)} DOIs from the publication list")

    tally, resolved = {}, 0
    for doi in dois:
        cs = countries_for(doi)
        time.sleep(0.15)
        if cs:
            resolved += 1
        for c in cs:
            tally[c] = tally.get(c, 0) + 1
        print(f"  {doi[:44]:46} {len(cs):3} countries")

    print(f"\nresolved {resolved}/{len(dois)} papers in OpenAlex")

    known = {c: n for c, n in tally.items() if c in COORDS}
    unknown = sorted(set(tally) - set(known))
    if unknown:
        print("no coordinates for (add to COORDS if wanted):", ", ".join(unknown))

    rows = sorted(known.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "# AUTO-GENERATED by scripts/fetch_collaborations.py",
        "# Countries hosting co-author institutions, counted across publications.",
        "",
    ]
    for code, n in rows:
        lat, lon, name = COORDS[code]
        lines += [
            f'- code: "{code}"',
            f'  name: "{name}"',
            f"  lat: {lat}",
            f"  lon: {lon}",
            f"  papers: {n}",
            f'  home: {"true" if code == HOME_COUNTRY else "false"}',
            "",
        ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {len(rows)} countries to {OUT}")


if __name__ == "__main__":
    main()
