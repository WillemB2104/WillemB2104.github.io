---
title: "Research"
permalink: /research/
layout: single
author_profile: true
toc: true
toc_label: "Research themes"
toc_sticky: true
---

Psychiatric disorders are diagnosed almost entirely from symptoms. Yet people
who share a diagnosis can differ substantially in their symptoms, their biology,
the course their illness takes and how they respond to treatment. This
heterogeneity is one of the central problems in psychiatry. If two patients look
very different clinically, why should we expect them to share the same
underlying (neuro)biology, or to benefit from the same treatment?

My research asks whether brain and other biological measurements can help move
psychiatry from population-level descriptions toward **individualised,
developmentally informed models of mental health**.

Three linked questions run through the work: how brain development relates to
the emergence of psychopathology, whether biological measures can identify
meaningful subgroups of patients, and whether they can help predict which
treatment will work for a given individual. Underneath all three sits a concern
with generalisability, which is to say understanding when a computational model
has captured clinically meaningful biology and when it has merely captured
noise, scanner differences or other artefacts of how the data were collected.

## Brain development and individual trajectories

Most psychiatric conditions first emerge during adolescence and young adulthood,
while the brain is still changing substantially. Much neuroimaging research
nonetheless relies on cross-sectional comparisons of patient and control groups,
and group averages obscure exactly the individual variation that is likely to
matter most.

**Normative modelling** offers a different approach. Rather than asking whether
patients differ from controls on average, it estimates where an individual sits
relative to an expected developmental trajectory, much as paediatric growth
charts situate a single child against reference curves. The deviation itself
becomes the measurement.

With repeated MRI assessments, this framework can go beyond asking whether a
brain looks atypical at one moment. It can ask whether developmental deviations
*precede* the emergence of symptoms, whether they shift as symptoms develop, and
whether different trajectories lead to different clinical outcomes. Those are
questions about direction of influence, and they are difficult to approach any
other way.

This is the focus of my current work at Amsterdam UMC with Prof. dr. Odile van
den Heuvel, using repeated MRI assessments from the **Generation R** cohort to
map brain development from childhood into young adulthood in relation to
obsessive-compulsive symptomatology. Two preregistered projects run in parallel:
one on [thalamic maturation](https://osf.io/9zwtc/overview) and its relation to 
broader subcortical and cortical development, and one on brain maturation in relation 
to obsessive-compulsive symptoms. At Leiden University I work with Dr. Moji Aghajani 
on similar questions in adolescent anxiety, using data from the ENIGMA consortium.  
A KNAW Ter Meulen grant supports an extension of this line with the University
of Southern California and the University of Michigan, using scans from roughly
15,000 young people across more than thirty countries to build developmental
reference curves that hold across diagnostic boundaries rather than within them.

Related work uses **brain-age modelling**, in which a model trained to estimate
chronological age from imaging data is applied to individuals, and the gap
between predicted and actual age is treated as an index of atypical development.

The longer-term aim is to move from static measures of brain structure toward
**longitudinal, multimodal models of developmental trajectories**, integrating
brain structure, brain function, behaviour and other biological measures.

## From group differences to individual biomarkers

Much of my earlier work asked a more direct question: can neuroimaging
distinguish people with a psychiatric disorder from those without one?

Within the
[ENIGMA-OCD](https://enigma.ini.usc.edu/ongoing/enigma-ocd-working-group/)
consortium I examined structural MRI from 2,304 patients with OCD and 2,068
controls across 46 datasets. The central finding was not an accurate diagnostic
classifier. It was a demonstration of how strongly **clinical and technical
heterogeneity constrain brain-based classification**. Structural MRI produced no
model that transferred reliably to new sites, while medication status was
associated with substantial and widely distributed anatomical differences,
separable at the individual level in a way that diagnosis itself was not.

A subsequent mega-analysis of resting-state functional connectivity, covering
1,024 patients and 1,028 controls across 28 sites and the largest such study of
OCD at the time of publication in 2023, found widespread reduced connectivity,
most pronounced within the **sensorimotor network**, alongside a smaller number
of hyper-connections involving the thalamus. Notably, the fronto-striatal
circuitry that has long dominated neurobiological models of OCD was not where
the strongest effects lay.

Extending this to anxiety disorders in young people, across 32 sites and 3,343
participants aged 10 to 25, transdiagnostic classification again reached only
modest accuracy at the individual level. The multivariate effect sizes were
nonetheless considerably larger than those from conventional univariate
comparisons, which illustrates both the promise of distributed brain signatures
and the distance that still separates statistical discrimination from clinically
useful prediction.

Taken together these results shaped how I approach biomarker research: **a
biomarker earns its name only if it generalises beyond the dataset it was built
on and captures variation that means something at the level of the individual.**

Key papers:

* Bruin et al. (2025). *Structural brain differences associated with panic
  disorder: an ENIGMA-Anxiety Working Group mega-analysis of 4,924 individuals
  worldwide.* Molecular Psychiatry. Shared first author.
  [Link](https://www.nature.com/articles/s41380-025-03376-4)
* Bruin et al. (2024). *Brain-based classification of youth with anxiety
  disorders: transdiagnostic examinations within the ENIGMA-Anxiety database
  using machine learning.* Nature Mental Health.
  [doi:10.1038/s44220-023-00173-2](https://doi.org/10.1038/s44220-023-00173-2)
* Bruin et al. (2023). *The functional connectome in obsessive-compulsive
  disorder: resting-state mega-analysis and machine learning classification for
  the ENIGMA-OCD consortium.* Molecular Psychiatry.
  [doi:10.1038/s41380-023-02077-0](https://doi.org/10.1038/s41380-023-02077-0)
* Bruin et al. (2020). *Structural neuroimaging biomarkers for
  obsessive-compulsive disorder in the ENIGMA-OCD consortium: medication
  matters.* Translational Psychiatry.
  [doi:10.1038/s41398-020-01013-y](https://doi.org/10.1038/s41398-020-01013-y)

## Predicting treatment response

Distinguishing patients from controls is, in the end, the less consequential
question. Clinicians already know who is ill. What they cannot know is what will
happen next, and which treatment a particular person is most likely to benefit
from.

My clearest result here concerns **electroconvulsive therapy** for
treatment-resistant depression. Working with the
[GEMRIC](https://mmiv.no/gemric/) consortium, I developed and validated
multimodal models combining grey matter volume, functional connectivity and
clinical variables to predict remission, using data from 189 patients across
seven centres. At the three larger contributing centres the models reached AUCs
of 0.82 to 0.83, and retained acceptable performance under leave-one-site-out
validation.

ECT is a useful test case. It is delivered in hospital, outcomes vary widely
between patients, MRI is inexpensive relative to the treatment itself, and the
scan could be acquired before treatment begins. The broader goal is not a
biomarker for one intervention, though, but an understanding of how **multimodal
biological information can be turned into treatment-relevant predictions**.

I have also worked on treatment effects more directly, including a randomised
controlled trial in OCD comparing how pharmacological and psychological
treatment alter brain activity, which I ran from recruitment through data
collection. I am currently a co-investigator on a funded project examining the
brain dynamics underlying esketamine treatment in depression.

Key papers:

* Bruin et al. (2023). *Development and validation of a multimodal neuroimaging
  biomarker for electroconvulsive therapy outcome in depression: a multicenter
  machine learning analysis.* Psychological Medicine.
  [doi:10.1017/S0033291723002040](https://doi.org/10.1017/S0033291723002040)
* van der Straten, Bruin et al. (2024). *Pharmacological and psychological
  treatment have common and specific effects on brain activity in
  obsessive-compulsive disorder.* Depression and Anxiety.
  [doi:10.1155/2024/6687657](https://onlinelibrary.wiley.com/doi/10.1155/2024/6687657)

## Making biomarkers generalisable

A recurring lesson across all of this is that building a model is far easier than
showing it works outside the data it was trained on.

Large-scale neuroimaging supplies the statistical power needed to study
heterogeneity, but brings a problem of its own. Data pooled across dozens of
sites differ in scanners, acquisition protocols, preprocessing, participant
populations and clinical procedures. Without careful harmonisation and
validation, a model will happily learn those differences instead of the biology.

I developed the functional connectivity mega-analysis framework first used within
ENIGMA-OCD, since adopted across more than ten ENIGMA disease working groups as
a standard approach to multi-site resting-state fMRI. I have also written on the
methodological obstacles to clinical translation more broadly: missing data,
small samples, site heterogeneity and the gap between a research cohort and a
clinic population.

This is why **external validation** matters. A model that performs
well on a random held-out subset of its own dataset and fails at a new site has
told us very little. Leave-one-site-out validation, independent replication and
frank reporting of failure are not optional extras but core parts of biomarker
development. My preprocessing and analysis pipelines are
[openly available](https://github.com/WillemB2104) for the same reason: methods
that cannot be inspected are difficult to trust.

## Towards individualised, multimodal psychiatry

What connects these strands is an interest in understanding psychiatric illness
at the level of the individual rather than the group.

I want to move past asking whether a disorder is associated with an average
difference somewhere in the brain, toward models that can say where a particular
person sits on a developmental trajectory, how their brain departs from what
would be expected, how that departure relates to their symptoms, and whether it
carries any information about which treatment will help.

Getting there will take more than a single MRI scan. My work is moving increasingly 
toward **multimodal and longitudinal approaches**, combining structural and functional
imaging with clinical, behavioural and other biological measures, and toward
models that can characterise individual trajectories and identify biologically
meaningful subgroups without assuming that diagnostic categories map neatly onto
distinct neurobiology.

The aim is not better prediction models for their own sake. It is generalisable,
reproducible and clinically meaningful biomarkers that change how psychiatric
disorders are understood, stratified and treated.

---

A full and continuously updated list of my work is on the
[publications page]({{ "/publications/" | relative_url }}). More about my
background is on the [about page]({{ "/about/" | relative_url }}).
