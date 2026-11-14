---
title: uDwgImport
weight: 2
aliases:
  - /help/udwgimport/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **CAD** | `uDwgImport` |

Imports one or many DWG and DXF files into the current Rhino document with a chosen source unit. New layers are grouped under a parent layer named after each file.

#### Steps

1. Run `uDwgImport`. The modal dialog `uDwgImport - Import CAD (Esc to cancel)` opens.
2. Enter the path in the text box: one file, several files separated by `;`, or a folder. A folder imports every `*.dwg` and `*.dxf` directly inside it (not subfolders).
3. Or use the file button to browse for files (multi-select) or the folder button to browse for a folder.
4. Choose the source unit in the dropdown.
5. Optional: click `Options` to open Document Properties, Units.
6. Click `Import`. Each file is imported with `_-Import` using the chosen units, and its new top-level layers are moved under a layer named after the file.
7. The command line reports `Import Complete. N file(s) imported.`

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Path | File, files separated by ;, or folder | What to import. |
| Browse files | Button | Multi-select file picker. |
| Browse folder | Button | Folder picker; imports *.dwg and *.dxf in that folder. |
| Unit | From DWG, Microns, Millimeters, Centimeters, Meters, Kilometers, Inches, Feet, Miles (default From DWG) | Unit of the source file, used for scaling. It is not the document unit. |
| Options | Button | Opens Document Properties, Units. |
| Import / Cancel | Buttons | Runs the import or closes the dialog. |
