---
title: "My Brain"
permalink: /brain/
layout: single
author_profile: true
---

Most of my research starts with something surprisingly simple: a three-dimensional image made up of numbers. Each number represents the measured MRI signal intensity at one small cube of space in the head: a **voxel**. If a pixel is a single square of a photograph on your screen, a voxel is its three-dimensional counterpart: a tiny block of brain, typically about a millimetre across. A whole scan is a stack of these blocks, several hundred thousand of them, each holding a single number. Once processed, these numbers can be turned into measurements of brain structure, connectivity, and development.

And this is what those numbers represent: **my brain**. Below, you can explore my own structural MRI scan, rendered directly in your browser. This is the raw material from which the measurements I work with are ultimately derived.

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

This is a **T1-weighted anatomical MRI**. It provides a detailed picture of the brain's structure, but it is not a photograph: the brightness of each tissue depends on how that tissue interacts with the MRI signal.

Around the outside you can see the scalp and skull. Inside the skull are the brain and the spaces and tissues surrounding it. The folded outer layer is **cerebral cortex**, consisting mainly of **grey matter**, roughly 2.5 mm thick. Beneath it is **white matter**, containing bundles of myelinated nerve fibres that connect different regions of the brain and help them communicate with one another. The dark spaces within the brain are the ventricles, which contain **cerebrospinal fluid** (CSF).

You can also make out other structures that are less obvious at first glance, including the **thalamus** and **basal ganglia** deep within the brain. CSF also surrounds the brain in the subarachnoid space, which lies between the arachnoid mater and pia mater. Small structures such as the choroid plexus, which produces much of the cerebrospinal fluid, can also be visible in the ventricular system, although they are not the main focus of this image.

The relative brightness of these structures depends on two main things: the type of MRI sequence used to acquire the scan and the tissue-specific properties of the brain, including their water and lipid content. In a T1-weighted image, **white matter** generally appears bright because of its high content of lipid-rich myelin, **grey matter** appears in intermediate shades, and water-rich CSF appears dark. These differences in contrast are what allow us to distinguish and measure different brain tissues from the same underlying image.

## From an image to measurements

A scan like this is where a study begins. Depending on the research question, the image can be processed to identify different tissue classes, locate anatomical structures, align the brain to a common space, and extract regional measurements such as cortical thickness, surface area or subcortical volume. Multiply that by a few thousand people across a few dozen hospitals, and you have the sort of dataset the [research pages]({{ "/research/" | relative_url }}) describe.

## The scan has been defaced

Structural MRI can contain enough information to reconstruct a person's face, making an unprocessed scan potentially identifiable. This scan has therefore been defaced: facial features have been removed while leaving the brain untouched. It is common practice before sharing any structural scan, including your own.

<a id="brain-download" class="btn btn--primary" href="#" download>Download the scan (NIfTI)</a>

The file here has been resampled to 1.2 mm and quantised to 16 bits to keep the page light, so it is intended for exploration rather than quantitative analysis.

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
      const nv = new Niivue({
        backColor: [0.055, 0.071, 0.098, 1],
        crosshairColor: [0.94, 0.66, 0.28, 1],
        show3Dcrosshair: true,
        isColorbar: false,
        dragMode: CROSSHAIR,
        multiplanarEqualSize: true,
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
