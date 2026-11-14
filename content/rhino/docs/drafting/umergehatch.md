---
title: uMergeHatch
weight: 4
aliases:
  - /help/umergehatch/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uMergeHatch` |

Merges touching or overlapping hatches into one hatch by taking the union of their boundaries. The first selected hatch supplies the pattern, rotation and scale.

#### Steps

1. Run `uMergeHatch`. The prompt reads `Select hatches to merge`.
2. Select at least two hatches and press Enter.
3. The command builds a planar region for each hatch boundary, unions them, joins the outer edges and creates new hatches.
4. The new hatches use the pattern, rotation and scale of the first hatch. The original hatches are deleted on success.
