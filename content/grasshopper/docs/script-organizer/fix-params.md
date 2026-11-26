---
title: Fix Params
weight: 2
---

Parameters such as Number Slider or Curve show an icon by default. Fix Params switches them to show their **name** instead, so a canvas full of parameters stays readable.

## Automatic mode

With **Auto** on, every parameter you add to the canvas is set to name display. Parameters that were already in the document are not touched until you run the command.

## Commands

| Command in **Comma → Fix Params** | What it does |
| --- | --- |
| **Run Once** | Sets name display on every parameter in the active document. |
| **Reset Default** | Puts the selected parameters (or all of them when nothing is selected) back on Grasshopper's default display mode. |

Turn **Print Log** on in [Settings](../settings/) to see in the Rhino command line which parameters were changed.
