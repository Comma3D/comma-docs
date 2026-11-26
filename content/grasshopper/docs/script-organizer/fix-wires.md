---
title: Fix Wire
weight: 3
---

Fix Wire fades the wires that connect objects living in **different groups**, so the wires inside a group stand out and the canvas looks calmer.

## How it decides

Only objects that belong to at least one group are looked at. For each input, Fix Wire checks the objects its wires come from: when **none** of them shares a group with the input's object, the input's wires are faded. If at least one source shares a group with it, the wires keep the default display.

{{% callout type="warning" %}}
If you change the display of a wire yourself (right-click menu or the canvas wire buttons), Fix Wire stops managing that wire and leaves your choice alone. **Reset Default** gives control back to it.
{{% /callout %}}

## Automatic mode

With **Auto** on, Fix Wire runs after every solution, once all the wires are settled.

## Commands

| Command in **Comma → Fix Wire** | What it does |
| --- | --- |
| **Run One** | Fades the cross-group wires in the active document now. |
| **Reset Default** | Resets the selected wires (or all of them when nothing is selected) to the default display. |

## Canvas wire buttons

Three buttons on the canvas toolbar set the wire display of the **selected** parameters and components that have at least one incoming wire: **Default**, **Faint** and **Hidden**.
