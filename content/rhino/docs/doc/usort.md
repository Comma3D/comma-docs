---
title: uSort
weight: 5
aliases:
  - /help/usort/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uSort` |

Opens the Comma Sort floating toolbar that sorts the selected objects by axis, radial position or guide curve and remembers that order. The saved order can then be injected into another command's object prompt, or baked into groups, lofts, curves and polylines.

#### Steps

1. Select at least two objects in the model, then run `uSort`. The Comma Sort toolbar appears; its label reads `Select -> sort` until you sort.
2. Click `X`, `Y` or `Z`. A single click adds that axis to the sort stack and sorts the selection; double-click sorts by that axis only and replaces the stack.
3. Or click `Rad` for a radial sort: pick the origin at `Radial sort origin (Enter for centroid)`.
4. Or click `Crv` to sort along a guide curve: pick it at `Select guide curve for sort order`.
5. Click `Rev` to reverse the saved order. Click `Clear` to discard it.
6. Use the saved order: click `Select` to select the objects in the sorted order. When another command is waiting for objects (for example `Loft`), `Select` injects the objects into that prompt in the saved order.
7. Optional: type a group pattern such as `2` or `2,3` (repeats) and click `Group` to bake Rhino groups named CommaSort_1, CommaSort_2 and so on.
8. Optional: click `Loft` to loft each complete group of sorted curves, `Nurbs` to create a control-point curve per group of sorted points, or `Poly` to create a polyline per group.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Select | Button | Selects the saved order, or injects it into an active object prompt. |
| Clear | Button | Clears the saved sort order. |
| X / Y / Z | Buttons | Single click adds the axis to the sort stack; double-click sorts by that axis alone. |
| Rad | Button | Radial sort around a picked origin (Enter uses the centroid). |
| Crv | Button | Sorts by position along a guide curve. |
| Rev | Button | Reverses the saved order. |
| Group pattern | Text such as 2 or 2,3 | Number of objects per group; a list repeats. |
| Group | Button | Bakes Rhino groups from the sorted list using the pattern. |
| Loft | Button | Lofts each complete group of sorted curves. |
| Nurbs | Button | Builds a control-point curve per group of sorted points. |
| Poly | Button | Builds a polyline per group. |

uSortOrder is a hidden alias. The nested sub-command uSortApply is run for you by the Select button.
