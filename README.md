# willemb2104.github.io

Source for my personal academic website: **<https://willemb2104.github.io>**

Built with [Jekyll](https://jekyllrb.com/) and the
[Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) theme (used as
a remote theme), hosted on GitHub Pages.

---

## Publications update themselves

The publication list is **not** maintained by hand. A scheduled GitHub Action
reads my [ORCID record](https://orcid.org/0000-0002-0672-8903), enriches each
entry with author lists and citation counts from
[Crossref](https://www.crossref.org/), and writes `_data/publications.yml`,
which the site renders.

| | |
|---|---|
| Script | [`scripts/fetch_orcid.py`](scripts/fetch_orcid.py) |
| Workflow | [`.github/workflows/update-publications.yml`](.github/workflows/update-publications.yml) |
| Generated data | `_data/publications.yml` - do not edit by hand |
| Page | [`_pages/publications.md`](_pages/publications.md) |
| Schedule | Weekly, Mondays 05:00 UTC |

The script also collapses duplicate records (a preprint and its published
version often both sit on an ORCID record), drops correction and erratum
notices, and shortens long consortium author lists.

**To refresh manually:** Actions → *Update publications from ORCID* → *Run
workflow*.

**If nothing appears:** check that works are set to *Everyone* visibility in
ORCID privacy settings, and that Settings → Actions → General → Workflow
permissions is set to *Read and write*.

To add a publication, add it to ORCID - not to this repo.

---

## Layout

```
_config.yml                 site settings, author profile, social links
_data/navigation.yml        top navigation bar
_data/publications.yml      generated - see above
_pages/                     about, research, publications, cv, contact
assets/images/              profile photo, thesis cover
scripts/                    ORCID fetcher (excluded from the built site)
index.html                  landing page
```

## Running it locally

Optional - everything can be edited through the GitHub web interface.

```bash
bundle install
bundle exec jekyll serve
# then open http://localhost:4000
```

Regenerating the publication list locally:

```bash
python scripts/fetch_orcid.py
```

---

## Licence

Site content © Willem B. Bruin. The Minimal Mistakes theme is
[MIT licensed](https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE).
