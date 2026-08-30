---
title: "About"
permalink: /about/
layout: single
author_profile: true
toc: true
toc_label: "On this page"
toc_sticky: true
---

I'm a postdoctoral researcher in **precision psychiatry**: the effort to tailor
psychiatric diagnosis and treatment to the individual patient, rather than to
the average of many. I hold positions at
[Amsterdam UMC](https://pure.amsterdamumc.nl/en/persons/willem-bruin/),
Department of Psychiatry, and at
[Leiden University](https://www.universiteitleiden.nl/en/staffmembers/willem-bruin),
Institute of Education & Child Studies.

The question I keep returning to:

Can we measure something in an individual's brain that helps explain, predict,
and ultimately improve their diagnosis and treatment?
{: .lead-question}

My approach to answering this question combines brain scans from thousands of people across many countries, far more than any single study or hospital can collect, with machine learning to find patterns that hold at the level of the individual patient.

## What I work on now

I work across **obsessive-compulsive, anxiety and mood disorders**.

At **Amsterdam UMC** I work with **Prof. dr. Odile van den Heuvel** on brain
development and obsessive-compulsive disorder. We use **Generation R**, a Dutch
study that has followed thousands of children from before birth with repeated
MRI scans, to ask how differences in brain development relate to the emergence
and persistence of symptoms through childhood and adolescence.

At **Leiden University** I work with **Dr. Moji Aghajani** on brain development
and clinical anxiety in young people, largely within the **ENIGMA-ANXIETY**
consortium.

Across both positions, the aim is to keep the individual in the picture, and to
model the differences that usually get averaged away. The
[research page]({{ "/research/" | relative_url }}) goes into what that involves
in more detail.

## From biomarkers to brain development

<a href="https://pure.uva.nl/ws/files/163646716/Thesis.pdf">
<img src="/assets/images/thesis-cover.jpg"
     alt="Cover of the PhD thesis 'Neuroimaging Biomarkers for Psychiatry'"
     style="width: 220px; float: right; margin: 0 0 1em 1.5em; border-radius: 4px;">
</a>

I completed my **PhD in 2024** at Amsterdam UMC, Department of Psychiatry,
supervised by Prof. dr. Guido van Wingen and Prof. dr. Damiaan Denys.

**[Neuroimaging Biomarkers for Psychiatry: Predicting Diagnosis and Treatment
Outcome using Machine Learning](https://pure.uva.nl/ws/files/163646716/Thesis.pdf)**

Psychiatric diagnosis rests on the subjective assessment of symptoms. Patients
sharing a diagnosis can look very different from one another, the same symptoms often 
overlap across disorders, and treatment guidelines largely follow a
one-size-fits-all logic, which for some patients means delay, or a treatment
that was never going to work. The thesis asked whether machine learning applied to neuroimaging data could produce generalisable **biomarkers**, objective measurements of the brain that could help identify, distinguish, or predict something about an individual patient to aid clinical decision-making.

The answer was neither a clean yes or no. Biomarkers that
looked convincing in one dataset often weakened when tested on data 
collected from new hospitals, and much of what made prediction hard was not noise 
but the sheer variety among patients themselves. That experience has shaped 
how I work since: large samples, rigorous external validation, reproducibility, and a 
lasting interest in how exactly patients differ so much from one another in the first place.

## Consortium work

Much of my work runs through international consortia, in which
dozens of hospitals and institutes pool their brain scans to answer questions
none of them could answer alone. I've led and coordinated analyses within
[**ENIGMA**](https://enigma.ini.usc.edu/), across both the
[ENIGMA-OCD](https://enigma.ini.usc.edu/ongoing/enigma-ocd-working-group/) and
[ENIGMA-ANXIETY](https://enigma.ini.usc.edu/ongoing/enigma-anxiety/) working
groups, and within [**GEMRIC**](https://mmiv.no/gemric/), a global collaboration
studying electroconvulsive therapy, together spanning more than seventy sites
worldwide.

For ENIGMA-OCD, I developed the consortium’s first shared mega-analytic framework for functional MRI across thousands of individuals at sites around the world. The framework has since been adopted by other working groups.

{% include collaboration-map.html %}

This kind of work often looks unglamorous, but it is what allows the field to
move forward: agreeing on shared standardized protocols, reconciling data collected in
different ways at different hospitals, and building analyses that hold up across
populations rather than fitting the quirks of one scanner in one place. 

My collaboration with **Prof. Paul Thompson**, director of ENIGMA, has been
supported by personal grants from the Royal Netherlands Academy of Arts
and Sciences (KNAW): the
[Van der Gaag](https://www.knaw.nl/interview-van-der-gaag-beurs-willem-bruin-onderzoek-naar-stemmingsstoornissen-bij-jongeren),
Van Leersum and Ter Meulen grants. They have led to several research visits to his lab at USC, where I have worked closely with the ENIGMA team. The KNAW published a short
[interview about the Van der Gaag project](https://www.knaw.nl/interview-van-der-gaag-beurs-willem-bruin-onderzoek-naar-stemmingsstoornissen-bij-jongeren)
(in Dutch), on using normative modelling to study brain
development in young people with anxiety and mood disorders.

## Approach

I care about **validation**: whether a finding still holds beyond the data from which it was derived. It is often much easier to build a predictive model that performs well in the sample it was derived from than to build one that generalises to patients at another hospital, scanned on a different machine.

That is why I test my models on patients from independent sites and who better resemble those seen in actual practice: people on medication, with multiple diagnoses, and across the full range of illness severity. I also make my analysis pipelines and preprocessing tools [open on GitHub](https://github.com/WillemB2104), because methods that can be inspected and reused are easier to trust.

---

*A full list of my publications is [generated automatically from my ORCID
record]({{ "/publications/" | relative_url }}). Interviews and talks are on the
[talks and media page]({{ "/media/" | relative_url }}), and my
[CV]({{ "/cv/" | relative_url }}) is available to download.*
