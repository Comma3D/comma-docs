---
title: uAngle
weight: 9
aliases:
  - /help/uangle/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uAngle` |

Measures the angle at a vertex between two picked points. The angle is reported in degrees with two decimals.

#### Steps

1. Run `uAngle`.
2. Optional: set `BakeResult`.
3. Pick the `Vertex`.
4. Pick `Point 1`.
5. Pick `Point 2`.
6. The angle in degrees is printed and copied to the clipboard. With `BakeResult` Yes the angle is added to the model on the layer `CheckAngle`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| BakeResult | No, Yes (default No) | Adds the measurement to the model. |
