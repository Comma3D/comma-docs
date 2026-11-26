---
title: uIfcExportHtml
weight: 6
aliases:
  - /help/uifcexporthtml/
---

| Menu | Command |
| --- | --- |
| Not on `commaMenu`. Type the command name. | `uIfcExportHtml` |

Writes Model.html next to any IFC file: one offline page that shows the model in 3D with a structure tree, an attribute table and a Properties panel. Edit attributes, save a new IFC, and write or answer BCF issues. No install and no upload: the file stays on the computer.

#### Steps

1. Run `uIfcExportHtml` and pick the IFC file.
2. Model.html is written next to it, with the same name. The IFC is inside the page up to 150 MB; a larger IFC is opened with `Open IFC` in the page.
3. Open Model.html in Chrome, Edge or Firefox. The uAttribute picklist, when one is loaded, is in the page too, for dropdowns and required fields.
4. `Issue` saves the view, a picture and the selected objects as a BCF topic; `Open BCF` shows a .bcfzip over the 3D view to read, comment and change status. See uBcf.

To make the page while exporting from Rhino, tick `Also save Model.html` in uIfcExport.
