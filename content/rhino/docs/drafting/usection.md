---
title: uSection
weight: 2
aliases:
  - /help/usection/
---

| Menu | Command |
| --- | --- |
| `commaMenu` → **Drafting** | `uSection` |

Cuts sections through solids, surfaces, meshes, blocks and curves with a line or a plane and places the section curves where you click. It repeats until you press Esc, so you can create many sections from the same selection.

#### Steps

1. Run `uSection`. At `Select objects to section` pick breps, surfaces, meshes, blocks or curves and press Enter.
2. Set `Mode` to `LineCut` (default) or `PlaneCut`, and set the other options (see the table).
3. In `LineCut` mode pick `Start of section line (Esc to exit)` and `End of section line`. The cutter is a tall plane along the CPlane Z direction.
4. In `PlaneCut` mode pick `Select plane source (Esc to exit)` (a surface, brep, mesh or face), then `Pick origin point for section plane`, then the two corners of the cut range (`First point of cut range (on plane)` and `Second point of cut range`).
5. At `Pick placement point (Enter = place at cut, no orient)` click where the section should be placed. Placement is constrained to the world XY plane and the section curves are oriented onto it. Press Enter to leave them at the cut.
6. The command line reports `Section complete (N result(s)). Pick new section line or Esc to exit.` Repeat with a new line or press Esc to finish.

#### Options

| Option | Values | What it does |
| --- | --- | --- |
| Mode | LineCut, PlaneCut (default LineCut) | Section by a line or by a plane. |
| SelectResults | Off, On (default On) | Selects the new section curves. |
| BakeCutter | No, Yes (default No) | Keeps the cutter: a curve named Reference_Line in LineCut, a brep named Section_Cutter in PlaneCut. |
| OutputLayer | InputLayer, CurrentLayer (default InputLayer) | Layer of the section curves. |
| GroupOutput | No, Yes (default No) | Groups the results as Section_Result. |
| Project | No, Yes (default No) | Projects the picked points onto the plane chosen in Plane before cutting. |
| Plane | CPlane, World (default CPlane) | Plane used by Project. |
| ExtentY | 0 to 1000000, default 1000 | PlaneCut only: height of the cutting plane. |
