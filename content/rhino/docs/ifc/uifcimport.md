---
title: uIfcImport
weight: 1
aliases:
  - /help/uifcimport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcImport` |

Imports one or many IFC files into Rhino as meshes or Breps, with layers built from the IFC spatial structure. You choose the engine, what to import, how layers and metadata are written, and an optional coordinate offset.

#### Steps

1. Run `uIfcImport`. The modal dialog `uIfcImport - Import IFC` opens.
2. Enter the path in the box (`File path(s) or folder...`): one file, several files separated by `;`, or a folder. Or use the file and folder buttons to browse.
3. Choose the `Engine`: `Rhino Built-in`, `IfcOpenShell (Hierarchy)` (default) or `xBIM (Direct Memory)`.
4. Tick what to import and how to handle the file, then set `Sharp edge angle` and the `Offset (m)` X, Y and Z.
5. Click `Import`. The layer root is the file name (prefixed by the relative folder segments when a folder was chosen). Layers follow Project, Site, Storey and, optionally, the IFC type.
6. The command line reports `Files: ok/total`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Engine | Rhino Built-in, IfcOpenShell (Hierarchy), xBIM (Direct Memory) (default IfcOpenShell) | Import engine. |
| Import Abstract/Spatial Elements (IfcSpace, IfcOpening...) | On, off (default off) | Also imports spaces and openings. |
| When selecting a folder: include IFC files in all subfolders | On, off (default off) | Searches subfolders when a folder is chosen. |
| If layer root exists | Replace existing (delete old objects), Skip file | What to do when the file layer root is already in the document. |
| Export detailed error/skip report to Desktop (.log) | On, off (default off) | Writes a log file. |
| IfcOpenShell: use native Brep when available (extrusions) | On, off (default off) | Creates Breps for extrusions instead of meshes. Only for IfcOpenShell. |
| Organize layers by IFC type | On, off (default off) | Off: Project, Site, Storey (and Name) layers with IfcType stored on the object. On: adds the IfcType segment to the layer path. |
| Write IFC metadata to Document User Text | On, off (default off) | Stores project data in Document User Text. With several files the keys are overwritten and the last file wins. |
| Write object UserText keys with [Type] | On, off (default off) | On writes keys like Pset.Name[Volume] = value so they can be re-exported. |
| Sharp edge angle | 0 to 180 degrees, default 80 | 0 makes every edge sharp, 180 makes all smooth. |
| Offset (m) X / Y / Z | Numbers, default 0 | Subtracted from real-world coordinates so the model sits near the origin. |

Check the layer tree after import. It is the same structure that uIfcExport reads back.
