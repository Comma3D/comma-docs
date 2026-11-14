---
title: uScopeBox
weight: 9
aliases:
  - /help/uscopebox/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uScopeBox` |

Creates six clipping planes around a box so the active viewport shows only what is inside it. The box is drawn with three points or taken from an existing closed box object.

#### Steps

1. Run `uScopeBox` in the viewport you want to clip.
2. Choose `Mode`: `Draw3PtBox` (default) or `SelectBox`. Optionally set `Size` (clipping plane size, default 500) and `DeleteExisting` (shown only when ScopeBox objects already exist).
3. In `Draw3PtBox` mode pick `Corner 1`, then `End of edge`, then `Width`, then `Height`.
4. In `SelectBox` mode pick an existing closed box at `Select Box` (a polysurface or extrusion).
5. Six clipping planes are added to the active viewport, each flipped to face the center of the box. They are grouped as `ScopeBox` and carry the user text ScopeBox=ScopeBox at each face center.
6. Run `uScopeBox` again with `DeleteExisting` set to Yes to replace the previous scope box.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Mode | SelectBox, Draw3PtBox (default Draw3PtBox) | Selects an existing box or draws a new one by three points and a height. |
| Size | Number (default 500) | Clipping plane size. |
| DeleteExisting | No, Yes | Deletes the previous ScopeBox clipping planes. Only shown when ScopeBox objects exist. |
