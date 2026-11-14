---
title: uAnnotation
weight: 3
aliases:
  - /help/uannotation/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uAnnotation` |

Opens the Comma Annotation toolbar to manage annotation scale for dimensions, text, leaders and hatches. You choose a drawing scale and paper text height, and annotations follow the scale automatically.

#### Steps

1. Run `uAnnotation`. The Comma Annotation toolbar opens.
2. Choose a dimension style in the style dropdown.
3. Choose the current scale (1:N) in the scale dropdown. Click `Scales` to open Edit Drawing Scales and add, edit, move, delete or reset scales.
4. Set the paper text height in millimeters (0.001 to 10000) with the stepper.
5. Draw dimensions, text, leaders or hatches. New annotations take the current scale and paper height.
6. Use `Show` to switch between all scales and the current scale only.
7. Use `Match` to copy properties: select the targets, then select the source.
8. Use `Sync` to apply the current scale and height to the selected annotations.
9. Use the `Auto` link to pause or resume automatic scale application and filtering while drawing.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Dimension style | Dropdown | Dimension style used for new dimensions. |
| Scale | Dropdown of 1:N | Current annotation scale. |
| Scales | Button | Opens Edit Drawing Scales with Add, Edit, Move Up, Move Down, Delete, Reset, OK, Cancel and Help. Drawing units are 1:N. |
| Paper text height | Millimeters, 0.001 to 10000 | Text height on paper. |
| Show | Toggle | All scales or current scale only. |
| Match | Button | Runs uAnnoMatchProperties: select targets, then the source. |
| Sync | Button | Applies current scale and height to the selection. |
| Auto | Link toggle | Auto-applies scale and filtering while drawing; click to pause. |

Standard scales are 1:1, 1:10, 1:20, 1:50, 1:100, 1:200 and 1:500. The default scale is 1:100 and the default paper height is 2.5 mm.
