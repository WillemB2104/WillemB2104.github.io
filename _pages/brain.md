---
title: "My Brain"
permalink: /brain/
layout: single
author_profile: true
---

Most of what I do comes down to one thing: a three-dimensional grid of numbers,
each one describing how much signal came back from a cubic millimetre of
somebody's head. Papers turn that into effect sizes and AUCs, which is useful
but abstract.

So here is the raw material, unabstracted. This is my own brain, a T1-weighted
structural MRI scan, rendered in your browser. Drag to move the crosshair,
scroll to move through slices, and use the controls to change the view.

<div id="brain-wrap">
  <div id="brain-status" role="status">Loading the scan (about 3&nbsp;MB)&hellip;</div>
  <canvas id="brain-canvas"></canvas>
</div>

<div id="brain-controls" hidden>
  <div class="brain-group">
    <span class="brain-label">View</span>
    <button type="button" data-slice="0">Axial</button>
    <button type="button" data-slice="1">Coronal</button>
    <button type="button" data-slice="2">Sagittal</button>
    <button type="button" data-slice="3" class="is-active">All three</button>
    <button type="button" data-slice="4">3D</button>
  </div>
  <div class="brain-group">
    <span class="brain-label">Colour</span>
    <button type="button" data-cmap="gray" class="is-active">Grayscale</button>
    <button type="button" data-cmap="viridis">Viridis</button>
    <button type="button" data-cmap="inferno">Inferno</button>
  </div>
</div>

<noscript>
This viewer needs JavaScript. The scan itself is linked below and opens in any
NIfTI viewer.
</noscript>

## What you are looking at

The bright ribbon around the outside is **grey matter**, the cortex, roughly
2.5&nbsp;mm thick and folded to fit inside the skull. The paler mass underneath
is **white matter**, the wiring that connects regions to one another. The dark
butterfly shapes near the middle are the **ventricles**, cavities filled with
cerebrospinal fluid.

Deep in the centre sit the **thalamus** and the **basal ganglia**, structures
that appear repeatedly in my work: the thalamus turned out to be one of the
strongest contributors to predicting who responds to electroconvulsive therapy,
and the basal ganglia are central to the models of obsessive-compulsive disorder
that my ENIGMA work has been testing.

A scan like this is where a study begins. From here it gets segmented into
tissue types, registered to a common template, and reduced to a few hundred
regional measurements. Multiply that by a few thousand people across a few dozen
hospitals, and you have the sort of dataset the
[research pages]({{ "/research/" | relative_url }}) describe.

## The scan has been defaced

Facial features can be reconstructed from a structural MRI, which makes an
unedited scan identifiable. This one has been through a defacing algorithm that
strips the face while leaving the brain untouched. It is standard
practice before sharing any structural scan, including your own.

<a id="brain-download" class="btn btn--primary" href="#" download>Download the scan (NIfTI)</a>

Rendered with [NiiVue](https://niivue.com), an open-source WebGL viewer.
{: .notice--info}

<style>
  #brain-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 3 / 2;
    background: #0e1219;
    border: 1px solid #2b3446;
    border-radius: 6px;
    overflow: hidden;
    margin: 1.6em 0 0.9em;
  }
  #brain-canvas { width: 100%; height: 100%; display: block; }
  #brain-status {
    position: absolute; inset: 0;
    display: flex; align-items: center; justify-content: center;
    text-align: center; padding: 1.5em;
    font-family: "IBM Plex Mono", monospace; font-size: 0.85rem;
    color: #8a97ab; z-index: 2;
  }
  #brain-controls {
    display: flex; flex-wrap: wrap; gap: 1.4em 2em;
    margin-bottom: 2em;
  }
  .brain-group { display: flex; align-items: center; flex-wrap: wrap; gap: 0.4em; }
  .brain-label {
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.06em;
    color: #8a97ab; margin-right: 0.5em;
  }
  #brain-controls button {
    font-family: "Space Grotesk", sans-serif;
    font-size: 0.82rem; padding: 0.35em 0.8em;
    color: #d7dee8; background: #1c2230;
    border: 1px solid #2b3446; border-radius: 4px; cursor: pointer;
    transition: border-color .15s ease, color .15s ease;
  }
  #brain-controls button:hover { border-color: rgba(63,208,201,.6); }
  #brain-controls button.is-active {
    border-color: #3fd0c9; color: #3fd0c9;
  }
</style>

<script type="module">
  // Path to the defaced scan. Replace with your own file.
  const SCAN = "{{ '/assets/data/brain.nii.gz' | relative_url }}";

  const status = document.getElementById("brain-status");
  const controls = document.getElementById("brain-controls");
  const dl = document.getElementById("brain-download");
  if (dl) dl.href = SCAN;

  // WebGL2 is required; fail with an explanation rather than a blank box
  const probe = document.createElement("canvas").getContext("webgl2");
  if (!probe) {
    status.textContent =
      "This viewer needs WebGL2, which this browser does not appear to support. " +
      "The scan can still be downloaded below.";
  } else {
    try {
      const { Niivue } = await import("https://cdn.jsdelivr.net/npm/@niivue/niivue@0.69.0/+esm");
      const nv = new Niivue({
        backColor: [0.055, 0.071, 0.098, 1],
        crosshairColor: [0.94, 0.66, 0.28, 1],
        show3Dcrosshair: true,
        isColorbar: false,
      });
      nv.attachTo("brain-canvas");
      await nv.loadVolumes([{ url: SCAN, colormap: "gray", opacity: 1, visible: true }]);
      nv.setSliceType(nv.sliceTypeMultiplanar);

      status.hidden = true;
      controls.hidden = false;

      const mark = (btn, attr) => {
        btn.parentElement.querySelectorAll("button[data-" + attr + "]")
           .forEach(b => b.classList.remove("is-active"));
        btn.classList.add("is-active");
      };

      controls.querySelectorAll("button[data-slice]").forEach(btn => {
        btn.addEventListener("click", () => {
          nv.setSliceType(Number(btn.dataset.slice));
          mark(btn, "slice");
        });
      });
      controls.querySelectorAll("button[data-cmap]").forEach(btn => {
        btn.addEventListener("click", () => {
          nv.setColormap(nv.volumes[0].id, btn.dataset.cmap);
          mark(btn, "cmap");
        });
      });
    } catch (err) {
      console.error(err);
      status.textContent =
        "The viewer could not load. The scan can still be downloaded below.";
    }
  }
</script>
