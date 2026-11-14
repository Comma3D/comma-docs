---
title: uFindCreateBlock
weight: 1
aliases:
  - /help/ufindcreateblock/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uFindCreateBlock` |

Finds identical copies of an assembly (moved or rotated, not scaled or mirrored) and replaces all of them with one block definition. You pick one example and the command locates every repeat in the visible model.

#### Steps

1. Run `uFindCreateBlock`. At `Select one repeated assembly to find and convert to blocks` select one example (any object types, several objects allowed).
2. At `Block base point (uses active CPlane)` pick the base point of the new block.
3. Enter the `Matching tolerance` (default is the larger of the document tolerance and 1 mm).
4. Enter the `New block name` (default CommaBlock_N). The name must not already exist.
5. The command scans visible objects for rigid copies. If fewer than two occurrences are found it says `No repeat found...`.
6. The matching occurrences are highlighted. Answer `Convert highlighted occurrences to one block` with No or Yes.
7. On Yes the block is created and each occurrence is replaced by a block instance.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Matching tolerance | Number | How closely a copy must match the example. |
| New block name | Text, default CommaBlock_N | Name of the block definition. |
| Convert | No, Yes | Confirms replacement of the highlighted occurrences. |

Text, annotations, lights, grips, details and clipping planes cannot be part of the assembly.
