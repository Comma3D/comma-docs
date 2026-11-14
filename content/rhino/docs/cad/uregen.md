---
title: uRegen
weight: 4
aliases:
  - /help/uregen/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **CAD** | `uRegen` |

Regenerates all viewports of the drawing that is open in AutoCAD, straight from Rhino. Use it after sending geometry with uDwg so the drawing refreshes.

#### Steps

1. Make sure AutoCAD is running with a drawing open.
2. Run `uRegen`.
3. The command regenerates all viewports in AutoCAD and prints `AutoCAD Regenerated successfully.`
4. If AutoCAD is not running or is busy the command prints `Error: AutoCAD is not running or busy.`
