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
| Generated data | `_data/publications.yml` (do not edit by hand) |
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

To add a publication, add it to ORCID, not to this repo.

---

## Layout

```
_config.yml                 site settings, author profile, social links
_data/navigation.yml        top navigation bar
_data/publications.yml      generated, see above
_pages/                     about, research, publications, cv, contact
_includes/                  theme overrides and custom markup, see below
assets/css/main.scss        all styling, with the adjustable values at the top
assets/images/              portrait, profile photo, thesis cover
scripts/                    ORCID fetcher (excluded from the built site)
index.html                  landing page, including its hero content
```

### Theme overrides

A file in `_includes/` with the same name as one in Minimal Mistakes replaces
the theme's copy. Three do, and each is a small change on top of the 4.28.1
original, so compare against upstream before bumping `remote_theme`:

## Licence

Several different things live in this repo, under different licences.

| | |
|---|---|
| Prose on the site (`_pages/`, `index.html` front matter) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) feel free to reuse it, credit me |
| Code (Liquid includes, `main.scss`, the `/brain/` viewer script, `scripts/fetch_orcid.py`) | MIT |
| `assets/data/brain.nii.gz` | My own defaced T1, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Mine to give, and deliberately given. |
| Figures in `assets/images/figures/` | Rights sit with the publisher. Licence via `_includes/figure-credit.html`. |
| Photographs (`hero-portrait.*`, `profile*.jpg`, `bio-photo.jpg`, `thesis-cover.jpg`) | All rights reserved. |

Creative Commons licences are not designed for software, which is why the code
is MIT rather than folded into the CC BY line.

The Minimal Mistakes theme is
[MIT licensed](https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE),
copyright (c) 2013-2024 Michael Rose and contributors. 

[NiiVue](https://github.com/niivue/niivue) (BSD-2-Clause) powers the `/brain/`
viewer. 
