---
title: uDwg
weight: 1
aliases:
  - /help/udwg/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **CAD** | `uDwg` |

Sends selected Rhino geometry straight into the running AutoCAD drawing, with layers, colors and block instances mapped. Use it to hand off curves, points, text, hatches and blocks to CAD without exporting a file.

#### Steps

1. Start AutoCAD and open the target drawing.
2. Run `uDwg`. The prompt reads `Select objects to transfer (Esc to cancel)`. Pick curves, points, text dots, annotations, hatches or block instances (preselected objects are accepted).
3. Set the options on the prompt: `LayerExport`, `KeepStyle`, `ConvertCurve`, `InsertBlock`.
4. Press Enter. A progress meter runs; press Esc to cancel.
5. Hatches, dimensions and leaders go through a temporary DWG batch INSERT, with a COM fallback.
6. The command line ends with `Done. Sent: N, Failed: M`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| LayerExport | ChildOnly, Full (default ChildOnly) | Uses only the child layer name, or the full layer path. |
| KeepStyle | ByLayer, ByObject (default ByLayer) | ByLayer takes color and linetype from the layer; ByObject keeps the object overrides. |
| ConvertCurve | No, Yes (default Yes) | Yes turns freeform curves into polylines using the document tolerance. No joins lines and arcs and leaves freeform curves as splines. |
| InsertBlock | 0 to 100000, default 100 | When a batch has more objects than this number, the INSERT stays one block. 0 always uses one block. |

If AutoCAD is not running the command says `AutoCAD is not running.` If AutoCAD is busy it asks you to press Esc in AutoCAD and run `uDwg` again.
