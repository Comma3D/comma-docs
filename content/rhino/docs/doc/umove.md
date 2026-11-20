---
title: uMove
weight: 3
aliases:
  - /help/umove/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uMove` |

Opens the Comma Move form to shift objects between local model coordinates and real-world (survey) coordinates using a saved offset and rotation. Real applies the offset, Local reverses it. Named offsets can be saved per project and reused.

#### Steps

1. Select the objects to transform. If nothing is selected when you click `Real` or `Local`, the command asks `Select objects to transform`.
2. Run `uMove`. The Comma Move form opens and stays open while you work.
3. Type a project name in the project combo box, or pick a saved one to load its values.
4. Enter `X` and `Y` (required) and optionally `Z` and `R`. `Z` and `R` default to 0. `R` is a rotation in degrees.
5. Click `Save` to store the current values under the project name, or `Delete` to remove the selected saved project.
6. Click `Real` to go from local to real coordinates: objects are rotated by `R` about 0,0,0 and then moved by (X, Y, Z).
7. Click `Local` to go back: objects are moved by (-X, -Y, -Z) and then rotated by -R about 0,0,0.
8. Read the report label and the command line message `uMove: Transformed N object(s).` A message box confirms the operation; a model base point warning is added when Rhino has a model base point set.
9. Close the form with `Cancel`.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Project | Saved name or new name | Combo box that loads or names a saved offset. |
| X | Number (required) | Move offset along X in model units. |
| Y | Number (required) | Move offset along Y in model units. |
| Z | Number (default 0) | Move offset along Z in model units. |
| R | Degrees (default 0) | Rotation about 0,0,0 around the world Z axis. |
| Save | Button | Stores the project values in the Comma settings file (UMoveConfig.json). |
| Delete | Button | Removes the selected saved project. |
| Real | Button | Rotate by R, then move by (X, Y, Z). |
| Local | Button | Move by (-X, -Y, -Z), then rotate by -R. |
| Cancel | Button | Closes the form without transforming anything. |

Real followed by Local with the same values returns objects to their original position.
