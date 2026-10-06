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

| File | What it changes |
|---|---|
| `_includes/page__hero.html` | Adds the landing-page hero (portrait, research question, actions). Every other page falls through to the stock markup. |
| `_includes/masthead.html` | Adds `aria-current="page"` to the matching nav link, so the current section is marked. |
| `_includes/footer.html` | Compact footer: name, tagline, links. Drops the "Follow:" label and the Atom feed link. |

`_includes/home-cards.html` is not an override; it is the three landing-page
cards, and the middle one reads the two most recent entries from
`_data/publications.yml` so the home page updates with the ORCID job.

The landing hero's text lives in the `hero_home:` block in `index.html`'s front
matter, not in the include.

### The hero animation

`_includes/footer/custom.html` draws two canvases. The one in the splash hero is
a normative model: shaded percentile bands, individual trajectories, and
measurement points that turn amber once they leave the ±1.96 SD band. If you
change the accent colours in `main.scss`, change `EXPECTED` and `DEVIATION`
here to match.

The second canvas is a much fainter site-wide backdrop, masked out of the
centre column so it never sits behind body text. Set `BACKDROP = false` at the
top of its block to switch it off.

## Running it locally

Optional. Everything can be edited through the GitHub web interface.

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
