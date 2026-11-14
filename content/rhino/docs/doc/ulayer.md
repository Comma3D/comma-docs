---
title: uLayer
weight: 1
aliases:
  - /help/ulayer/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uLayer` |

Opens the Comma Layer dock panel, or closes it when it is already open. The panel shows one button per layer you define in Setup, so you can move objects onto a layer, restyle them, or make a layer current with one click. Extra layer tools are in the Advance flyout of the panel.

#### Steps

1. Run `uLayer`. The Comma Layer panel docks next to the viewports. Run `uLayer` again to close it.
2. Open `Setup` (button in the panel header, also listed in the `Advance` flyout). The `Comma Layer Setup` dialog has one row per layer with the columns Show, Map, Nickname, Layer Name, Color, Linetype and Print Width.
3. In Setup, add rows with `+` or pull the layers that already exist in the document with `Get`. Fill in Nickname, Layer Name (use `::` for sublayers), Color, Linetype and Print Width, and tick `Show` for every row that should become a panel button.
4. Use `Bake` in Setup to create or update the layers in the Rhino document, then `OK` to save the button set. Row order is changed with the up and down arrows; `All` / `None` tick or clear the Show column.
5. Optional: save the whole button set as a preset with `Save`, switch with `Load`, remove with `Del`. Layer sets can also be moved between machines with `Import` / `Export` (JSON) or applied from a template file.
6. Optional: in the panel, type a prefix in the Main layer box (for example `Main::`, `Main_` or `Main-`). A prefix ending in `::` (or no separator) nests the button layers under it as sublayers; `_` or `-` joins prefix and layer name into one flat layer name.
7. Select objects in the model, then click a layer button. If nothing is selected, the command asks `Select objects for [layer]` and applies the click to the objects you pick.
8. Choose the click type to decide what changes: left click moves the objects to the layer; Shift+left click only sets the object color from the button swatch; Ctrl+left click moves the objects and resets color, linetype and print width to By Layer.
9. Right-click a button to make that layer the current layer. A filled dot on the button marks the current layer.
10. Open `Advance` for related tools: `uMergeLayer`, `uReNameLayer`, `uBlockToLayer`, `uFindMainLayer`, `uApplyColorMap` (assign objects to layers by color) and `Setup`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Main layer prefix | Text such as Main:: or Main_ or Main- | Text box at the top of the panel. Prepended to every button layer name. Ending in `::` creates nested sublayers; `_` or `-` creates a flat merged name. |
| Left click | Button | Moves the selected objects to the button layer (creating or updating the layer first). Without a selection it prompts for objects. |
| Shift + left click | Button | Sets only the object color from the button swatch (color from object). Layer is unchanged. |
| Ctrl + left click | Button | Moves objects to the layer and sets color, linetype and print width to By Layer. |
| Right click | Button | Sets the button layer as the current layer. |
| Setup | Button | Opens Comma Layer Setup: Show, Map, Nickname, Layer Name, Color, Linetype, Print Width, plus presets, Get, Bake, Search, templates and JSON import/export. |
| Advance | Flyout | Lists uMergeLayer, uReNameLayer, uBlockToLayer, uFindMainLayer, uApplyColorMap and Setup. |

The button layers, colors and presets are stored per user, so the same panel layout is available in every document.
