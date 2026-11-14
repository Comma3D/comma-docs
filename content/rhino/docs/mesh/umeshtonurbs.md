---
title: uMeshToNurbs
weight: 2
aliases:
  - /help/umeshtonurbs/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Mesh** | `uMeshToNurbs` |

Converts meshes (including IFC tessellation) to NURBS while keeping attributes. Quality presets drive faceted and analytic fits (prisms, tubes, circular holes, auto-heal). Rotational parts become real cylinders or cones; multi-piece meshes convert piece by piece and unconvertible pieces stay meshes (PARTIAL).

#### Steps

1. Select IFC meshes (Enter = all meshes)`.


#### Options

| Option | What it does |
| --- | --- |
| Quality | Fast / Balanced / Tight (default Balanced). |
| Output | Replace or Copy. |
| Advanced | No/Yes — unlocks Mode, Method, HealOpen, Tolerance, TimeLimit, MaxFaces, CheckObjects, Report. |
| Mode (Advanced) | Auto / Primitives / Pipe / Extrude / Freeform. |
| Method (Advanced) | Smart / Faceted / Analytic. |
| HealOpen / Tolerance / TimeLimit / MaxFaces / CheckObjects / Report | Advanced conversion controls (Tolerance 0 = auto). |
