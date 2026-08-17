---
title: "Publications"
permalink: /publications/
layout: single
author_profile: true
toc: true
toc_label: "By year"
toc_sticky: true
---

{% assign pubs = site.data.publications | where_exp: "p", "p.title != ''" %}

{% if pubs.size == 0 %}

The publication list is being generated. In the meantime, my papers are listed on
[ORCID](https://orcid.org/{{ site.author.orcid_id }}) and
[Google Scholar](https://scholar.google.nl/citations?user=TUq1H20AAAAJ&hl=en).

{% else %}

{% assign total_citations = 0 %}
{% for p in pubs %}{% assign total_citations = total_citations | plus: p.citations %}{% endfor %}

This list is generated automatically from my
[ORCID record](https://orcid.org/{{ site.author.orcid_id }}) and refreshed each
week, with metadata and citation counts from Crossref. My name is shown in
**bold**. See also my
[Google Scholar profile](https://scholar.google.nl/citations?user=TUq1H20AAAAJ&hl=en).
{: .notice--info}

**{{ pubs | size }} outputs · {{ total_citations }} citations recorded by Crossref.**

{% assign preprints = pubs | where: "type", "preprint" %}
{% assign published = pubs | where_exp: "p", "p.type != 'preprint'" %}

{% if preprints.size > 0 %}
## Preprints

{% for p in preprints %}
{% if p.authors != "" %}{{ p.authors }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.
**{{ p.title }}**.{% if p.journal != "" %} *{{ p.journal }}*.{% endif %}
{% if p.url != "" %}[{% if p.doi != "" %}doi:{{ p.doi }}{% else %}link{% endif %}]({{ p.url }}){% endif %}
{: .pub-entry}

{% endfor %}
{% endif %}

{% assign by_year = published | group_by: "year" | sort: "name" | reverse %}

{% for group in by_year %}
## {{ group.name }}

{% for p in group.items %}
{% if p.authors != "" %}{{ p.authors }}. {% endif %}**{{ p.title }}**.{% if p.journal != "" %} *{{ p.journal }}*.{% endif %}
{% case p.type %}
{% when 'book-chapter' %}<span class="pub-tag">Book chapter</span>
{% when 'book' %}<span class="pub-tag">Book</span>
{% when 'review' %}<span class="pub-tag">Review</span>
{% when 'software' %}<span class="pub-tag">Software</span>
{% when 'data-set' %}<span class="pub-tag">Dataset</span>
{% when 'dissertation-thesis' %}<span class="pub-tag">Thesis</span>
{% when 'conference-paper' %}<span class="pub-tag">Conference paper</span>
{% endcase %}
{% if p.url != "" %}[{% if p.doi != "" %}doi:{{ p.doi }}{% else %}link{% endif %}]({{ p.url }}){% endif %}{% if p.citations > 0 %} <span class="pub-cites">· {{ p.citations }} citations</span>{% endif %}
{: .pub-entry}

{% endfor %}
{% endfor %}

{% endif %}

<style>
  .pub-entry { margin-bottom: 1.1em; line-height: 1.5; }
  .pub-cites { opacity: 0.55; font-size: 0.85em; white-space: nowrap; }
  .pub-tag {
    display: inline-block;
    font-size: 0.7em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.15em 0.5em;
    border: 1px solid currentColor;
    border-radius: 3px;
    opacity: 0.6;
    vertical-align: middle;
  }
</style>
