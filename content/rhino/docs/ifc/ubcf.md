---
title: uBcf
weight: 7
aliases:
  - /help/ubcf/
---

| Menu | Command |
| --- | --- |
| Not on `commaMenu`. Type the command name. | `uBcf` |

Opens the Comma BCF window: the issues of a .bcfzip (BCF 2.1) with their pictures. Click an issue to select its objects by GlobalId and go to its view. Change type, status, priority, assigned to, due date, labels and stage, add comments, make a new issue from the active view, and save the file for Solibri, BIMcollab, Revit plugins or Model.html.

#### Steps

1. Run `uBcf`. The Comma BCF window opens with the last file used.
2. `Open…` a .bcfzip. When it holds issues of the file already open (a copy sent out and returned), it is merged in: new comments and changes are marked ● until you save, and the status line says what came in (for example `1 new comment · 1 status changed`).
3. Click an issue: its objects are selected and the view is set. The list filters by status, assigned to (`Me`), label and `Overdue`; a due date in the past shows in red.
4. Edit the fields below the list, or type a comment and press `Add comment`.
5. `New from view` makes an issue from the active view, its picture and the selected objects.
6. `Save` writes the file; `Save as…` writes a copy.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Status, Type, Priority, Labels, Stage | Lists of the file, else Comma defaults | Values another tool wrote are kept and shown. |
| Due | yyyy-mm-dd, ▾ calendar, × clears | Date only. |
| Assigned to | Name or e-mail | Pick from the list or type. |

A BCF 3.0 file opens read only. Model.html (uIfcExportHtml) reads and writes the same files, so a client without Rhino can answer an issue in the browser and send the file back.
