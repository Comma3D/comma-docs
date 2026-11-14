---
title: uDist
weight: 5
aliases:
  - /help/udist/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uDist` |

Measures the distance between two points with a live preview. The result is printed on the command line and copied to the clipboard.

#### Steps

1. Run `uDist`.
2. Optional: set `BakeResult` (No or Yes) and `UnitDisplay` (Document or Meters).
3. Pick the `Start point`.
4. Pick the `End point`. The distance updates live while you move the mouse.
5. The result is printed and copied to the clipboard. With `BakeResult` Yes a line and a text dot are added on the layer `CheckDist` and grouped.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a line and a text dot to the model. |
| UnitDisplay | Document, Meters (default Document) | Unit of the printed result. |
