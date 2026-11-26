---
title: Ctrl+Alt copy without wires
weight: 6
---

Grasshopper copies objects when you drag with **Alt** held down, and the copies keep their input wires to the original sources. With **Ctrl+Alt Copy Without Wires** you can drag-copy and leave the wires behind.

1. Select the objects and start dragging them with **Alt** held down.
2. **Hold Ctrl as you release the mouse button.**

The copies come out without the input wires from the original sources. Wires between the copied objects themselves are kept, and one **Undo** removes the copies.

Without Ctrl, Alt drag-copy behaves exactly as in Grasshopper. The feature is a toggle in **Comma → Ctrl+Alt Copy Without Wires** (on by default). Only drag-copies are affected: pasting and dropping from the toolbar are left alone.
