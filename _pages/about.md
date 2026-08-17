---
title: "About"
permalink: /about/
layout: single
author_profile: true
toc: true
toc_label: "On this page"
toc_sticky: true
---

I'm a postdoctoral researcher in **precision psychiatry**, working at the
intersection of neuroimaging, machine learning and clinical psychiatry. I hold
positions at
[Amsterdam UMC](https://pure.amsterdamumc.nl/en/persons/willem-bruin/),
Department of Psychiatry, and at
[Leiden University](https://www.universiteitleiden.nl/en/staffmembers/willem-bruin),
Institute of Education & Child Studies.

The broad question I keep returning to is a simple one that turns out to be very
hard: **can we measure something in an individual's brain that meaningfully
sharpens a diagnosis, or tells us in advance which treatment is likely to
work?**

Answering it means analysing brain imaging data at a scale no single hospital
can reach, and building predictive models that hold up when they meet patients
they were never trained on.

## What I work on now

At **Amsterdam UMC** I work in the Team Neuropsychiatry group at the VUmc, in
collaboration with **Prof. dr. Odile van den Heuvel**, on how the brain develops
from childhood into young adulthood and how deviations from typical trajectories
relate to obsessive-compulsive symptomatology. The work uses **normative
modelling** across repeated MRI assessments to follow individuals rather than
group averages, and asks how early deviations shape later development and the
emergence or persistence of symptoms.

At **Leiden University**, in collaboration with **Dr. Moji Aghajani**, my
research applies machine learning and big data to predictive and biological
psychiatry. Collaboration with global consortia is central to this work,
leveraging large-scale neuroimaging datasets to investigate anxiety disorders in
adolescents. The aim is to understand the developing brain and how it may
deviate in youth with anxiety, and to build predictive models that could support
decision-making in mental healthcare by providing inferences at the level of the
individual patient.

Understanding why some young people are more vulnerable to obsessive-compulsive
disorder, anxiety and depression, and what that vulnerability looks like in the
brain, connects both positions.

## Background

<a href="https://pure.uva.nl/ws/files/163646716/Thesis.pdf">
<img src="/assets/images/thesis-cover.jpg"
     alt="Cover of the PhD thesis 'Neuroimaging Biomarkers for Psychiatry'"
     style="width: 220px; float: right; margin: 0 0 1em 1.5em; border-radius: 4px;">
</a>

I completed my **PhD in 2024** at Amsterdam UMC, Department of Psychiatry,
supervised by Prof. dr. Guido van Wingen and Prof. dr. Damiaan Denys.

**[Neuroimaging Biomarkers for Psychiatry: Predicting Diagnosis and Treatment
Outcome using Machine Learning](https://pure.uva.nl/ws/files/163646716/Thesis.pdf)**

Psychiatric diagnosis still rests on the subjective assessment of symptoms.
Patients sharing a diagnosis can look very different from one another, symptoms
overlap heavily across disorders, and treatment guidelines largely follow a
one-size-fits-all logic,  which for some patients means delay, or a treatment
that was never going to work. The thesis asked whether machine learning applied
to neuroimaging data could produce **generalisable** biomarkers to help with
this.

The answer turned out to be more interesting than a straightforward yes or no.
Working with the **ENIGMA-OCD** consortium, 2,304 patients and 2,068 controls
across 36 institutes, structural MRI proved unable to separate patients from
controls in a way that transferred to new sites. But grouping patients by
medication status enabled good classification, revealing that medication is
associated with substantial, widely distributed differences in brain anatomy,
and that clinical heterogeneity is a large part of why these models underperform.
A subsequent mega-analysis of resting-state connectivity in over 2,000
participants found widespread hypo-connectivity in OCD, concentrated in the
**sensorimotor network** rather than the fronto-striatal circuitry that dominates
existing disease models.

Extending this to **anxiety disorders in youth** across 32 sites and 3,343 young
people aged 10–25, transdiagnostic classification again reached only modest
performance - though the effect sizes were considerably larger than for
univariate differences, and comparable to brain-based classification elsewhere in
psychiatry.

The clearest positive result came from treatment prediction. Using multimodal
data from the **GEMRIC** consortium, models combining grey matter volume,
functional connectivity and clinical variables predicted **remission after
electroconvulsive therapy** in treatment-resistant depression, reaching AUCs of
0.82–0.83 at the larger centres and holding up under leave-one-site-out
validation. Since ECT is delivered in hospital and MRI is inexpensive relative to
the treatment itself, this is a setting where a decision-support tool is
genuinely plausible.

Alongside the consortium work, I carried out a **randomised controlled trial in
OCD** comparing the effects of pharmacological and psychological treatment on
brain activity - running it from recruitment through data collection. The
resulting dataset has since been contributed to ENIGMA-OCD and continues to
support international collaborative research.

## Consortium work

Much of what I do happens at a scale no single site can reach. I've led and
coordinated analyses within international consortia including
[**ENIGMA**](https://enigma.ini.usc.edu/) - both the
[OCD](https://enigma.ini.usc.edu/ongoing/enigma-ocd-working-group/) and
[anxiety](https://enigma.ini.usc.edu/ongoing/enigma-anxiety/) working groups -
and [**GEMRIC**](https://mmiv.no/gemric/), working across 70+ sites for
data-driven biomarker development and validation.

The functional connectivity mega-analysis framework I developed for ENIGMA-OCD
was the first of its kind within the consortium, and has since been adopted
across more than ten ENIGMA disease working groups for standardised
resting-state fMRI analysis.

Studies I led within these consortia:

- **Structural brain differences associated with panic disorder: an
  ENIGMA-Anxiety Working Group mega-analysis of 4,924 individuals worldwide.**
  *Molecular Psychiatry* (2025). *Shared first author.*
  [Link](https://www.nature.com/articles/s41380-025-03376-4)

- **Brain-based classification of youth with anxiety disorders: transdiagnostic
  examinations within the ENIGMA-Anxiety database using machine learning.**
  *Nature Mental Health* (2024).
  [doi:10.1038/s44220-023-00173-2](https://doi.org/10.1038/s44220-023-00173-2)

- **The functional connectome in obsessive-compulsive disorder: resting-state
  mega-analysis and machine learning classification for the ENIGMA-OCD
  consortium.** *Molecular Psychiatry* (2023).
  [doi:10.1038/s41380-023-02077-0](https://doi.org/10.1038/s41380-023-02077-0)

- **Development and validation of a multimodal neuroimaging biomarker for
  electroconvulsive therapy outcome in depression: a multicenter machine
  learning analysis.** *Psychological Medicine* (2023).
  [doi:10.1017/S0033291723002040](https://doi.org/10.1017/S0033291723002040)

- **Structural neuroimaging biomarkers for obsessive-compulsive disorder in the
  ENIGMA-OCD consortium: medication matters.** *Translational Psychiatry*
  (2020).
  [doi:10.1038/s41398-020-01013-y](https://doi.org/10.1038/s41398-020-01013-y)

This kind of work might seem unglamorous but is essential: harmonising protocols,
reconciling heterogeneous data, and building analyses that hold up across
populations rather than fitting the quirks of one scanner in one hospital.

My collaboration with **Prof. Paul Thompson**, director of ENIGMA, has been
supported by two personal grants from the Royal Netherlands Academy of Arts and
Sciences (KNAW) - the
[Van der Gaag](https://www.knaw.nl/interview-van-der-gaag-beurs-willem-bruin-onderzoek-naar-stemmingsstoornissen-bij-jongeren)
and Van Leersum grants - and included research visits to his lab at USC. The
KNAW published a short
[interview about the Van der Gaag project](https://www.knaw.nl/interview-van-der-gaag-beurs-willem-bruin-onderzoek-naar-stemmingsstoornissen-bij-jongeren)
(in Dutch), covering the use of AI and normative modelling to study brain
development in young people with anxiety and mood disorders.
 

## Approach

I care about **validation**. A prediction model that performs beautifully in
a held-out split of the same dataset and collapses at a new site hasn't told us
much, and internal cross-validation on a small, carefully curated sample is a
poor guide to what will happen in practice. Leave-one-site-out validation,
external replication, and honest reporting of where models fail are what make the
difference between an interesting result and a usable one.

The work I find worth doing is the kind that survives contact with new, unseen
samples that better reflect clinical practice, patients with prior treatment
exposure, comorbidities, varying symptom severity, and all the heterogeneity that
gets excluded from tightly controlled study populations.

I also share my analysis pipelines and preprocessing tools
[openly on GitHub](https://github.com/WillemB2104), for much the same reason:
methods that can't be inspected or reused are hard to trust.

---

*A full list of my publications is [generated automatically from my ORCID
record]({{ "/publications/" | relative_url }}), and my
[CV]({{ "/cv/" | relative_url }}) is available to download.*
