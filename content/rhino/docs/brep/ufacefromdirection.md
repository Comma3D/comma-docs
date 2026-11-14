---
title: uFaceFromDirection
weight: 5
aliases:
  - /help/ufacefromdirection/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Brep** | `uFaceFromDirection` |

Extracts the faces of a brep whose normals point in a chosen direction, for example all upward-facing faces. A tolerance angle controls how strictly the normal must match.

#### Steps

1. Run `uFaceFromDirection`. The prompt reads `Select brep to extract faces`. Select a brep or surface.
2. Optional: set `Reverse` (No or Yes) and `BothDirections` (No or Yes) on the prompts. Both are remembered.
3. At `First point of direction vector (Enter for Z-axis)` click a start point, or press Enter to use the world Z axis.
4. If you picked a point, click the `Second point of direction vector`.
5. Enter the `Angle tolerance in degrees` (0 to 90, default 0). A face is kept when its normal, measured at the middle of its surface domain, is within that angle of the direction.
6. The matching faces are extracted as new breps and selected. The command line reports `Extracted N faces from M total faces`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Reverse | No, Yes | Uses the opposite of the picked direction. |
| BothDirections | No, Yes | Accepts faces that point with or against the direction. |
| Angle tolerance | 0 to 90 degrees, default 0 | Allowed angle between face normal and direction. |
