---
title: uAnimation
weight: 1
aliases:
  - /help/uanimation/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Animation** | `uAnimation` |

Opens the animation panel: move parts along curves, lines and axes, link them to a leader, bend a chain, play the timeline, and export one MP4 video or PNG frames. Play only previews; the model changes only with `Apply pose`.

#### Steps

1. Run `uAnimation`. The panel shows the steps: 1 Add a motion, 2 Pick the objects and what drives them, 3 Press Play.
2. `Add motion`, then choose how the objects move: Move along a curve, Slide along a line, Follow two curves, Follow a leader, Turn around an axis, Planes from a table, Highlight only or Bend a chain (IK). Pick the objects and the curve, line or axis.
3. Set the frames (`Start`, `End`) and the speed over time; `Show guides` draws the curves and axes in the viewport.
4. Press `Play`. Drag the slider to preview any frame.
5. Export: choose `MP4 video` (default) or `PNG frames`, the quality (High, Medium, Small), the view and the folder, then `Export MP4` or `Export PNG`.
6. `Save` keeps the animation in a file; `Open` reads it back. `uAnimationSample1` and `uAnimationSample2` build two examples.

MP4 uses the H.264 encoder of Windows; when it is missing the panel says so and no file is left.
