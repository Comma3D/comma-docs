---
title: uExportBox
weight: 2
aliases:
  - /help/uexportbox/
---

| Menu | Command |
| --- | --- |
| Not on `commaMenu`. Type the command name. | `uExportBox` |

Exports the part of the model that lies inside a closed box to a new 3DM file. Meshes are clipped to the box in parallel, so large IFC models export quickly.

#### Steps

1. Run `uExportBox`. At `Select clipping box (closed polysurface)` pick a polysurface or extrusion that is a closed box. Otherwise the command says `Selected object is not a closed box-like Brep.`
2. Choose a `Preset`: `Speed` (default), `Quality` or `Custom`. Changing `IncludeHidden` or `Boolean` switches the preset to Custom.
3. Optional: set `IncludeHidden` (No or Yes) and `Boolean` (Off or On).
4. Press Enter. The Save dialog `Export Box Region` opens; choose a `.3dm` file (default `uExportBox.3dm`).
5. The meshes are clipped to the box and written to the file. The command line reports `uExportBox done - N meshes written to ...`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Preset | Speed, Quality, Custom (default Speed) | Speed: IncludeHidden No and Boolean Off. Quality: IncludeHidden Yes and Boolean On. Custom: your own mix. |
| IncludeHidden | No, Yes | Also exports hidden objects. |
| Boolean | Off, On | On makes watertight clipped results with a Boolean operation; Off only cuts the meshes, which is faster. |
