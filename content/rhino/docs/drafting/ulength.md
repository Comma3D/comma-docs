---
title: uLength
weight: 6
aliases:
  - /help/ulength/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uLength` |

Adds up the length of the selected curves. The total is printed and copied to the clipboard.

#### Steps

1. Run `uLength`.
2. At `Select Curves` pick one or more curves. Set `BakeResult` and `UnitDisplay` first if needed.
3. Press Enter. The total length is printed on the command line and copied to the clipboard.
4. With `BakeResult` Yes a text dot `L: ...` is added at the average midpoint of the curves on the layer `CheckLength`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds a text dot with the total length. |
| UnitDisplay | Document, Meters (default Document) | Unit of the result. |
