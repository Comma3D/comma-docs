---
title: uIfcInstall
weight: 5
aliases:
  - /help/uifcinstall/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **IFC** | `uIfcInstall` |

Installs the Python packages that the IFC commands need into the Python that Rhino uses. A dialog shows which packages are present and installs the missing ones with one click.

#### Steps

1. Run `uIfcInstall`. The modal dialog `Install IFC Dependencies` opens.
2. Read the status list: `ifcopenshell`, `numpy` and `orjson` (optional, makes JSON handling 5 to 10 times faster) with their versions and a check or cross.
3. Click `Install`. The command installs the packages into Rhino's Python with pip. The output text area shows the pip output.
4. Wait until the status list updates. If installing `orjson` fails the import still works without it.
5. Click `Close`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Install | Button | Installs the missing packages. Enabled only while ifcopenshell or numpy is missing. |
| Close | Button | Closes the dialog. |

ifcopenshell and numpy are required; orjson is optional.
