---
title: uDwgExport
weight: 3
aliases:
  - /help/udwgexport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **CAD** | `uDwgExport` |

Batch exports selected objects into several DWG, 3DM or DXF files, one file per object or per layer group. You control the folder layout and file names from the layer path, with a live list of the files that will be created.

#### Steps

1. Run `uDwgExport`. At `Select objects to batch export` pick any objects (preselected objects are accepted).
2. The modal dialog `uDwgExport - Batch export (DWG/3DM/DXF)` opens. Choose the `Export folder` (default Desktop).
3. Choose the `Format` (.dwg, .3dm or .dxf) and the `File name prefix` (default Export).
4. Choose the `Export mode`: `Layer` (default, one file per layer group) or `Object` (one file per selected object).
5. Set `Level N` (0 to 9). Level 0 is the root of the layer table, the same as path level 1.
6. Tick the parts of the file name: `Level (N)` (on), `Path below N`, `Layer name (leaf)` and `Suffix` (number or date, on).
7. Set the layer name written inside each file: `Path from level N down` (off) and `Layer name only (leaf)` (on).
8. Optional: set the folder layout `Create subfolders from ancestors above level N` (on) with `Ancestor levels` 1 to 9 (default 1).
9. Optional: tick `Include Ref_box in every file (Layer mode)`, `Use date suffix instead of number` (suffix _yyyyMMdd), set `Start number` (default 1001) and the `Replace in file name` From and To (default `::` to `_`).
10. Check the `Files to be created` list, then click `Export`.
11. The command line reports `Successfully exported N files to: ...`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Export folder | Folder path (default Desktop) | Destination folder; use Browse to choose. |
| Format | .dwg, .3dm, .dxf | File type of the exported files. |
| File name prefix | Text, default Export | Start of every file name. |
| Export mode | Object, Layer (default Layer) | One file per object, or one file per layer group. |
| Level N | 0 to 9 | Layer level used for grouping and naming. 0 is the root in the layer table. |
| Level (N) | On, off (default on) | Adds the layer name at level N to the file name. |
| Path below N | On, off (default off) | Adds the segments under level N to the file name. |
| Layer name (leaf) | On, off (default off) | Adds the last layer segment to the file name. |
| Suffix | On, off (default on) | Adds a number or a date. Required in Object mode so each file name is unique. |
| Path from level N down | On, off (default off) | Writes the layer path from level N down to each object inside the file. |
| Layer name only (leaf) | On, off (default on) | Writes only the last layer segment inside the file. |
| Create subfolders from ancestors above level N | On, off (default on) | Builds subfolders from the layer segments above level N. |
| Ancestor levels | 1 to 9, default 1 | How many ancestor levels become subfolders. |
| Include Ref_box in every file | On, off | Layer mode: adds the Ref_box object to each file. |
| Use date suffix instead of number | On, off | Uses _yyyyMMdd instead of a number. |
| Start number | 1 to 99999, default 1001 | First number for numeric suffixes. |
| Replace in file name | From, To (default :: and _) | Text replacement applied to the file name. |

Validation messages: `File name: tick at least one of Level (N), Path below N, or Layer name.`, `Object mode requires a suffix so each file stays unique.`, and an error for duplicate output paths. Objects whose layer depth is below N are skipped and counted in `Skipped N object(s) with layer depth below level N.`
