---
title: Input tools
weight: 5
---

Two commands in the **Comma** menu work on the inputs of the components you have selected.

## Clear Selected Inputs

Clears the persistent data stored in the selected inputs and disconnects their wires. Use it to reset a component to an empty state.

## Internalise Selected Inputs

Copies the data that arrives through wires (or from Rhino references) into the input's own persistent storage, and disconnects the wires. The component then keeps working without its former sources, and a parameter that referenced Rhino geometry no longer depends on the Rhino document. It does the same as Grasshopper's built-in **Internalise** command, but for all selected inputs at once.
