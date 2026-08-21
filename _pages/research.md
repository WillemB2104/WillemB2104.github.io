---
title: "Research"
permalink: /research/
layout: single
author_profile: true
toc: true
toc_label: "Research themes"
toc_sticky: true
---

Psychiatry still diagnoses and treats largely on the basis of what patients
report about their own symptoms. Two people with the same diagnosis can look
very different from one another, the same symptoms appear across different
disorders, and treatment decisions mostly follow general guidelines rather than
anything measured in the individual patient.

My research asks whether measurements of the brain can add something useful.

Can we sharpen diagnosis, explain why some people develop psychiatric disorders
while others do not, and predict which treatment will work for a given patient?
{: .lead-question}

I work across obsessive-compulsive, anxiety and mood disorders, using brain
scans from thousands of people, machine learning, and studies that follow the
same individuals over many years.

Four strands run through this work.

## Brain development and individual trajectories

Many psychiatric disorders first appear during childhood, adolescence or young
adulthood, while the brain is still changing rapidly. Yet most brain imaging
studies take a single snapshot, comparing a group of patients with a group of
healthy people at one moment in time. A snapshot cannot show how anyone got
there, or what happens next.

**Normative modelling** offers one way to address this. It works much like the
growth charts used at any child health clinic: instead of asking whether a
group of patients differs from a group of controls on average, it maps the
range of brain measures expected at each age, and then asks where one
individual sits relative to that range. How far someone deviates from the
expected range becomes a measurement in its own right.

{% include figure-credit.html
   src="/assets/images/figures/fig-normative-model.svg"
   alt="Centile curves of a brain measure plotted against age, with one individual's four repeated scans overlaid. The first three sit within the expected range; the fourth falls below the fifth centile."
   caption="Rather than comparing patients with controls as groups, a normative model places each individual against the range expected at their age. With repeated scans, a departure from that range can be dated."
   credit="Figure by W.B. Bruin" %}

With repeated scans of the same people, this approach can do something a
snapshot cannot: follow individuals along their own developmental paths, and
ask whether deviations in brain development come before symptoms appear, change
alongside them, or follow them. That ordering in time is essential for
understanding what drives what.

This is the focus of my current work at Amsterdam UMC with Prof. dr. Odile van
den Heuvel, using **Generation R**, a Dutch study that has followed thousands
of children from before birth with repeated MRI scans. Two preregistered
projects run in parallel: one examining the maturation of the **thalamus**, a
relay station deep in the brain, in relation to wider brain development, and
another examining brain maturation in relation to obsessive-compulsive
symptoms.

At Leiden University, I work with Dr. Moji Aghajani on similar questions in adolescent anxiety, using data from the **ENIGMA-Anxiety** consortium.

Related work uses **brain-age modelling**. A model learns to guess a person's
age from their brain scan alone; applied to a new individual, the gap between
the guessed age and their real age becomes a simple summary of whether their
brain looks older or younger than expected.

A **KNAW Ter Meulen Beurs** supports an international extension of this line of research with the University of Southern California and the University of Michigan. Using scans from roughly 15,000 young people across more than thirty countries, this work aims to develop developmental reference curves that capture normative variation across populations rather than being specific to individual diagnostic groups.

## Diagnostic biomarkers in OCD and anxiety

Can a brain scan tell us whether someone has a psychiatric disorder?
{: .lead-question}

Working with the **ENIGMA-OCD** consortium, I tested this on the largest dataset
then available: scans of brain anatomy from 2,304 people with OCD and 2,068
healthy controls, collected at 36 institutes around the world.

The result was informative in an unexpected way. Models trained to recognise
OCD from brain anatomy did not hold up when tested on scans from hospitals they
had not seen before. But models distinguishing medicated from unmedicated
patients worked considerably better, revealing widespread differences in brain
anatomy associated with medication use. The lesson: the differences between
patients, including the treatments they are already receiving, can be larger
than the differences produced by the disorder itself.

A follow-up study looked at brain activity rather than anatomy, measuring how
strongly different regions communicate with one another in more than 2,000
participants. People with OCD showed weaker communication across much of the
brain, and the effect was strongest in the **sensorimotor network**, the
regions handling movement and bodily sensation, rather than in the
decision-and-habit circuits that textbook models of OCD emphasise. The
disorder's biology, in other words, may reach further than the standard models
suggest.

{% include figure-credit.html
   src="/assets/images/figures/fig-ocd-connectome.png"
   alt="Two panels. Above, the 400-parcel functional atlas mapped onto 17 resting-state networks, shown on inflated brain surfaces with a colour key. Below, a circular connectogram in which each arc is a connection differing between OCD patients and controls; blue arcs mark lower connectivity and are densest within the sensorimotor networks."
   caption="Connections differing between 1,024 patients with OCD and 1,028 controls across 28 sites. Blue arcs mark lower connectivity in patients. The densest cluster sits within the sensorimotor networks (SomMotA and SomMotB, upper left) rather than in the fronto-striatal circuitry that dominates existing models of the disorder."
   credit="Bruin et al. (2023), Molecular Psychiatry"
   url="https://doi.org/10.1038/s41380-023-02077-0"
   licence="CC BY 4.0"
   light="true" %}

I then extended this approach to anxiety disorders in young people, using
scans from 3,343 participants aged 10 to 25 across 32 sites. Models that
combined information from across the whole brain could separate patients from
controls only modestly, though far better than any single brain measure could.
Together these studies show both the promise of brain-based classification and
how far it still is from being clinically useful.

Key papers
{: .section-label}

- Han, Bruin, et al. (2025). *Structural brain differences associated with panic disorder: an ENIGMA-Anxiety Working Group mega-analysis of 4,924 individuals worldwide.* **Molecular Psychiatry.** Shared first author.
  [Link](https://www.nature.com/articles/s41380-025-03376-4)

- Bruin et al. (2024). *Brain-based classification of youth with anxiety disorders: transdiagnostic examinations within the ENIGMA-Anxiety database using machine learning.* **Nature Mental Health.**
  [doi:10.1038/s44220-023-00173-2](https://doi.org/10.1038/s44220-023-00173-2)

- Bruin et al. (2023). *The functional connectome in obsessive-compulsive disorder.* **Molecular Psychiatry.**
  [doi:10.1038/s41380-023-02077-0](https://doi.org/10.1038/s41380-023-02077-0)

- Bruin et al. (2020). *Structural neuroimaging biomarkers for obsessive-compulsive disorder in the ENIGMA-OCD consortium: medication matters.* **Translational Psychiatry.**
  [doi:10.1038/s41398-020-01013-y](https://doi.org/10.1038/s41398-020-01013-y)

## Predicting treatment outcome

Diagnosis is only one challenge. Clinicians usually know who is unwell. What
they cannot know in advance is **which treatment is likely to work for which
patient**, and choosing wrongly can cost months.

My clearest example concerns **electroconvulsive therapy (ECT)**, one of the
most effective treatments for severe depression that has resisted other
options. Working within the **Global ECT-MRI Collaboration (GEMRIC)**, I built
models that combine brain structure, brain activity and clinical information to
predict, before treatment begins, who will recover. At the larger contributing
centres these predictions were right substantially more often than chance, and
crucially they remained informative when tested on hospitals the models had
never seen.

{% include figure-credit.html
   src="/assets/images/figures/fig-ect-networks.png"
   alt="Axial brain slices showing two independent component networks: one centred on the temporal lobes, one on frontopolar cortex."
   caption="The two brain networks that contributed most to predicting who recovers with ECT: one centred on the temporal lobes, one on the frontopolar cortex. Each was informative for predicting recovery even on its own."
   credit="Bruin et al. (2023), Psychological Medicine"
   url="https://doi.org/10.1017/S0033291723002040"
   licence="CC BY" %}

ECT is a setting where a prediction like this could genuinely matter: the
treatment is demanding for patients and hospitals alike, its effects when it
works are substantial, and an MRI scan is cheap compared with the cost and
burden of a full treatment course. It is a concrete example of where a
validated brain measure could one day help decide who should be offered which
treatment.

The same question applies to psychological treatment. In related work I contributed to models predicting **cognitive behavioural therapy outcome in OCD** from clinical and neuroimaging data, where clinical variables turned out to carry much of the predictive information. That result is a useful corrective: neuroimaging has to earn its place against simpler and cheaper measures rather than being assumed to improve on them.

I have also conducted a randomised controlled trial in OCD examining how pharmacological and psychological treatment affect brain activity, from recruitment through data collection.

Most recently, I am a co-investigator on a project funded by the **ZonMw Neuropsychoanalyse Fonds** investigating the brain dynamics underlying **esketamine treatment** in depression. Esketamine acts far more rapidly than conventional antidepressants, which makes it an unusually informative setting for asking what changes in the brain when a treatment works, and how quickly.

Key paper
{: .section-label}

- Bruin et al. (2023). *Development and validation of a multimodal neuroimaging biomarker for electroconvulsive therapy outcome in depression: a multicenter machine learning analysis.* **Psychological Medicine.**
  [doi:10.1017/S0033291723002040](https://doi.org/10.1017/S0033291723002040)

## Making biomarkers generalisable

It is surprisingly easy to build a model that predicts well for the patients
it was developed on and then fails for patients at a different hospital,
scanned on a different machine. This is one of the central challenges in
psychiatric neuroimaging, and much of my methodological work confronts it
directly.

{% include figure-credit.html
   src="/assets/images/figures/fig-generalisation.png"
   alt="Boxplots of classification AUC for ten machine learning algorithms under three cross-validation schemes. Internal validation clusters near 0.6; leave-one-site-out validation drops to around chance level."
   caption="Telling OCD from controls with ten different algorithms. Tested against the data they were built on (light and green boxes), all perform above chance; tested on hospitals they had never seen (dark boxes), performance drops to a coin flip. How a model is tested, not which algorithm is used, decides whether it generalises."
   credit="Bruin et al. (2020), Translational Psychiatry"
   url="https://doi.org/10.1038/s41398-020-01013-y"
   licence="CC BY 4.0" %}

Data pooled from dozens of hospitals arrive with dozens of differences:
different scanners, different scanning protocols, different patient
populations, different diagnostic habits. Rather than treating all of that
variation as a nuisance, my work examines how it shapes the measurements and
predictions we make, and what it takes for a finding to hold up in spite of
it.

For ENIGMA-OCD I developed the consortium's first shared framework for
analysing brain activity data across all of its sites at once; it has since
been adopted by more than ten other ENIGMA working groups studying different
disorders. I have also worked on the quieter problems that decide whether such
analyses can be trusted: missing data, scanner differences between sites, and
how models should be validated.

The principle running through all of it is **external validation**: testing
every model on data it has never seen, from places it has never been, and
reporting openly when it fails. That is a far stronger test than any amount of
checking a model against the data it was built from.

My analysis code and preprocessing pipelines are [openly available](https://github.com/WillemB2104) where possible. Making methods inspectable and reproducible is part of the same goal: developing neuroimaging biomarkers that are not only statistically interesting, but robust enough to be useful beyond the dataset in which they were developed.

## Towards individualised psychiatry

What connects these projects is a focus on understanding psychiatric illness at the level of the **individual**.

Rather than asking only whether a disorder is associated with an average difference in the brain, I want to understand how brain development differs between people, how these differences relate to symptoms, and whether they can provide information about prognosis or treatment response.

Achieving this will require following people over time rather than photographing
them once, measuring more than one aspect of brain and behaviour, working with
large and diverse samples, and validating every model far beyond the data it was
built on. The goal is not prediction for its own sake, but brain measures that
are **reproducible, generalisable and clinically meaningful**.

---

A full and continuously updated list of my work is available on the [publications page]({{ "/publications/" | relative_url }}). More about my background is on the [about page]({{ "/about/" | relative_url }}).
