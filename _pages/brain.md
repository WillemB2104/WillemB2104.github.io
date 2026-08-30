---
title: "My Brain"
permalink: /brain/
layout: single
author_profile: true
---

Most of my research starts with something simple: a
three-dimensional image made of numbers. Each number is the measured MRI signal
at one small cube of space in the head called a **voxel**, the 3D counterpart of a
pixel, typically about a millimetre across. A whole scan is a stack of several
hundred thousand of these blocks, each holding a single number. Processed, they become measurements of brain structure, connectivity and development.

And below is a concrete example of what those numbers can represent: **my brain**! This is my own
structural MRI scan, some of the raw material from
which the measurements I work with are derived, rendered directly in your browser, 

**Click or drag** to move the crosshair. **Right-click and drag** to adjust the
contrast. Once you have clicked into the viewer, **scroll** moves through
slices; until then scrolling just moves the page.

<div id="brain-wrap">
  <div id="brain-status" role="status">Loading the scan (about 3 MB)...</div>
  <canvas id="brain-canvas"></canvas>
</div>

<div id="brain-controls" hidden>
  <div class="brain-group">
    <span class="brain-label">View</span>
    <button type="button" data-slice="0">Axial</button>
    <button type="button" data-slice="1">Coronal</button>
    <button type="button" data-slice="2">Sagittal</button>
    <button type="button" data-slice="3" class="is-active">All three</button>
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

This is a **T1-weighted anatomical MRI**. It gives a detailed picture of the
brain's structure: how bright each tissue appears
depends on how it interacts with the MRI signal. In a T1-weighted image, white matter appears bright because of its lipid-rich
myelin, grey matter sits in intermediate shades, and water-rich CSF is dark.
These contrast differences are what let us distinguish and measure the
different tissues from a single image.

Around the outside are the scalp and skull. Just beneath them lies the **cerebral cortex**, the brain’s folded outer layer. It is made up mainly of **grey matter**, where nerve cells are densely packed, and is only about 2.5 mm thick. Beneath the cortex is **white matter**, made up of bundles of myelinated nerve fibres that carry signals between different brain regions.

The dark spaces inside the brain are the ventricles, which are filled with **cerebrospinal fluid (CSF)**. CSF also flows around the brain and spinal cord, helping to cushion and protect them. Deep in the centre sit the **thalamus** and, just in front and to either side, the **basal ganglia**: drag the crosshair into the middle of the axial view and they appear as paired grey masses, separated by a pale band of white matter, the internal capsule. Both sit close to the questions I work on. The thalamus is the focus of one of my Generation R projects and has surfaced in my ENIGMA OCD analyses; the basal ganglia anchor the fronto-striatal circuits that most models of OCD are built on.

## From an image to measurements

A scan like this is where neuroimaging analyses begin. Depending on the question, it can be
processed to identify tissue classes, locate anatomical structures, align the
brain to a common space, and extract measures such as cortical thickness,
surface area or subcortical volume. Multiply that by a few thousand people
across a few dozen hospitals, and you have the sort of dataset the
[research pages]({{ "/research/" | relative_url }}) describe.

## My scan has been defaced

A structural MRI can contain enough information to reconstruct a person's face,
so an unprocessed scan is potentially identifiable. This one has been defaced:
facial features removed, brain untouched, which is common practice before sharing any
structural scan, including your own.

<a id="brain-download" class="btn btn--primary" href="#" download>Download the scan (NIfTI)</a>

The file has been resampled to 1.2 mm and quantised to 16 bits to keep the page
light, so it is meant for exploration rather than quantitative analysis.
{: .notice--info}

Rendered with [NiiVue](https://niivue.com), an open-source WebGL viewer.

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
  /* `hidden` loses to the ID rules below unless we say so explicitly */
  #brain-status[hidden],
  #brain-controls[hidden] { display: none; }
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
      const mod = await import("https://cdn.jsdelivr.net/npm/@niivue/niivue@0.69.0/+esm");
      const Niivue = mod.Niivue;

      // Recent NiiVue defaults the primary drag to contrast adjustment. This
      // page wants dragging to move the crosshair instead.
      const CROSSHAIR = (mod.DRAG_MODE && mod.DRAG_MODE.crosshair !== undefined)
        ? mod.DRAG_MODE.crosshair : 8;

      // On narrow screens (e.g. iPhone SE) NiiVue's auto-layout switches the
      // three planes from a row into a 2x2 grid to make better use of the
      // space. In grid mode, NiiVue's default "auto" render setting always
      // adds a 4th panel showing a raw 3D volume render of the whole head -
      // unmasked, so it shows the scalp/skull even though the scan itself is
      // defaced. Explicitly disabling the render panel keeps the viewer to
      // just axial/coronal/sagittal at every screen size.
      const SHOW_RENDER_NEVER = (mod.SHOW_RENDER && mod.SHOW_RENDER.NEVER !== undefined)
        ? mod.SHOW_RENDER.NEVER : 0;

      const nv = new Niivue({
        backColor: [0.055, 0.071, 0.098, 1],
        crosshairColor: [0.94, 0.66, 0.28, 1],
        show3Dcrosshair: true,
        isColorbar: false,
        dragMode: CROSSHAIR,
        multiplanarEqualSize: true,
        multiplanarShowRender: SHOW_RENDER_NEVER,
      });
      nv.attachTo("brain-canvas");
      await nv.loadVolumes([{ url: SCAN, colormap: "gray", opacity: 1, visible: true }]);
      nv.setSliceType(nv.sliceTypeMultiplanar);

      status.hidden = true;
      controls.hidden = false;

      // The viewer binds the mouse wheel to slice navigation, which would trap
      // the page scroll. Swallow wheel events in the capture phase until the
      // user clicks into the viewer; clicks and drags are never intercepted.
      const wrap = document.getElementById("brain-wrap");
      let engaged = false;
      wrap.addEventListener("wheel", (e) => {
        if (!engaged) e.stopPropagation();
      }, { capture: true });
      wrap.addEventListener("pointerdown", () => {
        engaged = true;
        wrap.classList.add("is-engaged");
      });
      wrap.addEventListener("mouseleave", () => {
        engaged = false;
        wrap.classList.remove("is-engaged");
      });

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
