---
title: uTolerance
weight: 6
aliases:
  - /help/utolerance/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Doc** | `uTolerance` |

Opens the Comma Tolerance toolbar that temporarily overrides the document absolute tolerance while Rhino commands run. The file itself keeps its original tolerance, so saved models are not changed.

#### Steps

1. Run `uTolerance`. The Comma Tolerance toolbar opens already enabled, showing the current document tolerance and its unit.
2. Type a new tolerance in the box. The value must be a finite number greater than zero, otherwise the command line says `uTolerance: enter a finite number greater than zero.`
3. Press Enter or leave the box to apply it. The command line confirms the active override (`ACTIVE ...`).
4. Run your Rhino commands (Boolean, join, loft, offset and so on). The override is active only while a command runs; between commands and during Save the file tolerance is restored.
5. Click `Disable` to turn the override off (the box becomes read-only and the file tolerance is used). Click `Enable` to turn it back on.
6. Close the toolbar, or disable it, to reset to the file tolerance. Changing the active document also resets it.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Tolerance | Number greater than 0 | Absolute tolerance used while commands run. Read-only while disabled. |
| Unit label | Document unit | Shows the unit of the document. |
| Enable / Disable | Toggle button | Turns the temporary override on or off. |

The command line prints reset to file tolerance when the override ends.
