# Regenerates content/ from the catalog research. Re-run after editing the data below.
$ErrorActionPreference = "Stop"
$root = Join-Path $PSScriptRoot "content"
if (Test-Path $root) { Remove-Item $root -Recurse -Force }
New-Item -ItemType Directory -Force -Path $root | Out-Null
$utf8 = New-Object System.Text.UTF8Encoding $false
$arrow = [char]0x2192

function W([string]$rel, [string]$text) {
    $path = Join-Path $root ($rel -replace "/", "\")
    New-Item -ItemType Directory -Force -Path (Split-Path $path -Parent) | Out-Null
    [System.IO.File]::WriteAllText($path, ($text.Trim() + "`n"), $utf8)
}

function OptTable([string[]]$rows) {
    if (-not $rows -or $rows.Count -eq 0) { return "" }
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("| Option | What it does |")
    [void]$sb.AppendLine("| --- | --- |")
    foreach ($r in $rows) {
        $parts = $r -split "\|", 2
        [void]$sb.AppendLine("| $($parts[0].Trim()) | $($parts[1].Trim()) |")
    }
    return $sb.ToString().TrimEnd()
}

function CmdPage($section, $slug, $title, $weight, $group, $onMenu, $summary, $options, $prompts, $limits, $extra) {
    $alias = $title.ToLowerInvariant()
    if ($onMenu) {
        $where = "Where to find it: ``commaMenu`` $arrow **$group** $arrow ``$title``."
    } else {
        $where = "Where to find it: type ``$title``."
    }
    $optBlock = OptTable $options
    $body = @"
---
title: $title
weight: $weight
aliases:
  - /help/$alias/
---

$where

$summary
"@
    if ($optBlock) {
        $body += "`n`n## Options`n`n$optBlock"
    }
    if ($prompts) {
        $body += "`n`n## Prompts`n`n$prompts"
    }
    if ($limits) {
        $body += "`n`n## Limits`n`n$limits"
    }
    if ($extra) {
        $body += "`n`n$extra"
    }
    W "rhino/docs/$section/$slug.md" $body
}

# --- Suite home ---
W "_index.md" @"
---
title: Comma
layout: hextra-home
---

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>AEC tools</span>
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Comma
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Plugins for Rhino, Tekla Structures, and Revit.&nbsp;<br class="hx:sm:block hx:hidden" />
  Guides, install steps, and issue tracking in one place.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6 hx:flex hx:flex-wrap hx:gap-3">
{{< hextra/hero-button text="Rhino guide" link="rhino" >}}
{{< hextra/hero-button text="Report an issue" link="https://github.com/Comma3D/comma-docs/issues" >}}
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card title="CommaRh" subtitle="Rhino 8 modeling, drafting, and CAD/IFC exchange. Install from the Package Manager." link="rhino/" >}}
  {{< hextra/feature-card title="CommaTs" subtitle="Tekla Structures model and drawing plugins. Guide pages land here as the team publishes them." link="tekla/" >}}
  {{< hextra/feature-card title="CommaRvt" subtitle="Revit tools — placeholder until the product ships." link="revit/" >}}
{{< /hextra/feature-grid >}}
"@

# --- Rhino product home (Trung-style) ---
W "rhino/_index.md" @"
---
title: CommaRh
layout: hextra-home
---

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>Rhino 8</span>
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  CommaRh
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Modeling, drafting, and CAD/IFC exchange for Rhino 8.&nbsp;<br class="hx:sm:block hx:hidden" />
  Install from the Package Manager.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6 hx:flex hx:flex-wrap hx:gap-3">
{{< hextra/hero-button text="Documentation" link="docs" >}}
{{< hextra/hero-button text="Report an issue" link="https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arhino" >}}
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card title="Getting started" subtitle="Package Manager install, the type menu, and the licence on this computer." link="docs/getting-started/" >}}
  {{< hextra/feature-card title="Doc" subtitle="Layers, objects, attributes, sort, tolerance, and quick tools." link="docs/doc/" >}}
  {{< hextra/feature-card title="Curve and surface" subtitle="Scale, flip, rebuild polylines, and fit circles or arcs." link="docs/curve/" >}}
  {{< hextra/feature-card title="Brep" subtitle="Scale, loft, smooth, combine, and extract faces." link="docs/brep/" >}}
  {{< hextra/feature-card title="Mesh" subtitle="Patch, convert meshes to NURBS, and extract a 2D outline." link="docs/mesh/" >}}
  {{< hextra/feature-card title="Drafting" subtitle="Blocks, sections, annotation, hatches, and measurements." link="docs/drafting/" >}}
  {{< hextra/feature-card title="CAD" subtitle="DWG and AutoCAD import, export, and regenerate." link="docs/cad/" >}}
  {{< hextra/feature-card title="IFC" subtitle="Import, export, template setup, shared parameters, and IfcOpenShell." link="docs/ifc/" >}}
  {{< hextra/feature-card title="Issues" subtitle="Report a Rhino command problem. Leave licence keys out of the issue." link="https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arhino" >}}
{{< /hextra/feature-grid >}}
"@

W "rhino/docs/_index.md" @"
---
title: CommaRh
linkTitle: Documentation
weight: 1
cascade:
  type: docs
---

CommaRh is a Rhino 8 toolkit for inspection, modeling, drafting, and CAD/IFC exchange. Run ``commaMenu`` and choose a group: Doc, Curve, Surface, Brep, Mesh, Drafting, CAD, or IFC.

Panel actions stay inside their panels. This guide lists the public commands only.

Install from the Rhino Package Manager. To report a problem, open [Issues](https://github.com/Comma3D/comma-docs/issues) and add the ``rhino`` label.
"@

W "rhino/docs/getting-started/_index.md" @"
---
title: Getting started
weight: 1
---

Install CommaRh, open the menu, and check the licence on this computer.
"@

W "rhino/docs/getting-started/installing.md" @"
---
title: Installing
weight: 1
---

Every public command documented under Rhino ships together in one Package Manager package, **CommaRh**. One install gives you the type menu, the panels, CAD/IFC exchange, and the licence manager — there is no separate installer to download, and you do not copy files by hand.

- To install: open Rhino 8 on Windows, run ``PackageManager``, search for ``CommaRh``, and click **Install**.
- Supported versions: Rhino 8 (Windows).
- Current guide version: 26.1.8. Package Manager shows the version that is installed on this computer.

After install, run ``commaMenu``. That opens the type menu (Doc / Curve / Surface / Brep / Mesh / Drafting / CAD / IFC) plus **License Manager**.

Licence: each computer gets a 45-day trial the first time CommaRh needs a Pro feature on that machine, with nothing to register. To keep working after that, activate a licence key for the computer:

1. Run ``commaRegister`` (or ``commaMenu`` $arrow **License Manager**). It shows this computer's Machine ID and the current licence or trial status.
2. Use **Contact us to get a license**, or write to [comma3d.aec@gmail.com](mailto:comma3d.aec@gmail.com), with the Machine ID.
3. When the key arrives, paste it into **License key** (or **Browse...**) and click **Activate**.

Details are in the [Licence](../license/) page. Do not paste a licence key into a GitHub issue.
"@

W "rhino/docs/getting-started/using-the-menu.md" @"
---
title: Using the menu
weight: 2
---

Run ``commaMenu`` to open the compact type menu.

| Group | What it covers |
| --- | --- |
| Doc | Layers, objects, attributes, visibility, sort, scope box, tolerance, quick tools |
| Curve | Curve scale, direction, conversion, and circle or arc fitting |
| Surface | Surface normal |
| Brep | Scale, loft, smooth, combine, and face extraction |
| Mesh | Patch, mesh to NURBS, and 2D outline |
| Drafting | Blocks, section, annotation, hatch, and measurements |
| CAD | DWG import and export |
| IFC | IFC import, export, template, shared parameters, and IfcOpenShell |

``commaMenu`` also includes **License Manager** (``commaRegister``), **About**, and the built-in user manual.

Commands that are not on the menu are still public. Type the command name. Each of those pages says so.
"@

W "rhino/docs/getting-started/license.md" @"
---
title: Licence
weight: 3
aliases:
  - /help/commaregister/
---

Where to find it: ``commaMenu`` $arrow **License Manager**, or type ``commaRegister``.

``commaRegister`` opens Comma License Manager for this computer. It shows the Machine ID (with **Copy**), the current status, and a licence key box.

A computer without a key can run a 45-day trial. No sign-up is required. The customer line then reads "This computer (no sign-up)". Status reads **Trial** with the days left, **Trial - last day** on the final day, **Licensed** for an active Pro key, or **Unlicensed** when the trial is over and no key is active.

To activate a key, paste it into **License key** or use **Browse...**, then click **Activate**. **Remove** clears the key stored on this computer.

For Pro, more seats, or a key for another computer, use **Contact us to get a license** or write to [comma3d.aec@gmail.com](mailto:comma3d.aec@gmail.com).

Do not paste a licence key into a GitHub issue. Prefer the ``rhino`` label on [Issues](https://github.com/Comma3D/comma-docs/issues).
"@

W "rhino/docs/getting-started/report-a-problem.md" @"
---
title: Report a problem
weight: 4
---

Problems are tracked on [Comma docs Issues](https://github.com/Comma3D/comma-docs/issues). Use the ``rhino`` label for CommaRh.

Include:

- The installed CommaRh version shown in Package Manager
- The Rhino 8 version
- The command name
- What you expected and what happened

Leave licence keys out of the issue. For a new key, use ``commaRegister`` or [comma3d.aec@gmail.com](mailto:comma3d.aec@gmail.com).

This repository is also the place other Comma products publish their guides. Push markdown under ``content/rhino``, ``content/tekla``, or ``content/revit`` on the ``main`` branch; GitHub Actions rebuilds the site.
"@

W "rhino/docs/getting-started/contribute.md" @"
---
title: Contribute to the guide
weight: 5
---

The guide source lives in the public repository [Comma3D/comma-docs](https://github.com/Comma3D/comma-docs). Plugin source stays private.

1. Clone ``https://github.com/Comma3D/comma-docs.git``.
2. Edit markdown under ``content/`` (Rhino pages are under ``content/rhino/docs/``).
3. Commit on a branch and open a pull request into ``main``, or push to ``main`` if you are a collaborator.
4. The **Deploy Pages** workflow builds Hugo and publishes https://comma3d.github.io/comma-docs/.

Local check (optional):

``````powershell
git clone --depth 1 --branch v0.13.0 https://github.com/imfing/hextra.git themes/hextra
hugo server
``````

Do not commit ``public/``, ``themes/``, or ``.tools/``.
"@

# section indexes
$sections = @{
    doc = @{ title = "Doc"; weight = 2; blurb = "Document panels and settings. Open them from ``commaMenu`` $arrow **Doc**." }
    curve = @{ title = "Curve"; weight = 3; blurb = "Curve tools. Open them from ``commaMenu`` $arrow **Curve**." }
    surface = @{ title = "Surface"; weight = 4; blurb = "Surface tools. Open them from ``commaMenu`` $arrow **Surface**." }
    brep = @{ title = "Brep"; weight = 5; blurb = "Brep tools. Open them from ``commaMenu`` $arrow **Brep**." }
    mesh = @{ title = "Mesh"; weight = 6; blurb = "Mesh tools. Open them from ``commaMenu`` $arrow **Mesh**." }
    drafting = @{ title = "Drafting"; weight = 7; blurb = "Section, annotation, hatch, and measurements. Open them from ``commaMenu`` $arrow **Drafting**." }
    cad = @{ title = "CAD"; weight = 8; blurb = "DWG and AutoCAD exchange. Open these commands from ``commaMenu`` $arrow **CAD**." }
    ifc = @{ title = "IFC"; weight = 9; blurb = "IFC exchange. Open these commands from ``commaMenu`` $arrow **IFC**." }
    more = @{ title = "More"; weight = 10; blurb = "Public commands that are not listed on ``commaMenu``. Type the command name." }
}
foreach ($name in $sections.Keys) {
    $s = $sections[$name]
    W "rhino/docs/$name/_index.md" @"
---
title: $($s.title)
weight: $($s.weight)
---

$($s.blurb)
"@
}

# --- Commands (from code research; no invented options) ---
CmdPage "doc" "ulayer" "uLayer" 1 "Doc" $true `
  "Opens or toggles the Comma Layer dock panel after the licence gate. Layer actions stay in the panel (including the Advance layer-command flyout)." `
  $null $null `
  "Free/Trial: the layer panel is Pro-gated. When the panel does open on a limited plan, the layer list is truncated to three layers." $null

CmdPage "doc" "uobject" "uObject" 2 "Doc" $true `
  "Opens the Object / Select Similar dock panel for property-based matching. Select objects in the model, then use the panel columns and **Select Similar**." `
  @(
    "Heaviest / Visibility / FindBlock / Tolerance|Panel tools next to the object table.",
    "Property / Description columns|Toggle which columns are shown.",
    "Select Similar|Match from the current selection using the visible properties.",
    "All / None (per type)|Select or clear rows by object type.",
    "Area / Volume|Quick links; unit toggle mm$([char]0x00B2)/m$([char]0x00B2)."
  ) `
  "Status on open: ``Select one or more objects to begin.``" $null $null

CmdPage "doc" "umove" "uMove" 3 "Doc" $true `
  "Opens a modeless panel for saved project offsets (X / Y / Z / R) and Real / Local transforms." `
  @(
    "Save / Delete|Store or remove a named project offset.",
    "Real|Rotate about the origin, then move by XYZ.",
    "Local|Move by -XYZ, then rotate by -R.",
    "Project combo + X/Y/Z/R|Choose a saved project and edit its values."
  ) `
  "When applying: ``Select objects to transform``." $null $null

CmdPage "doc" "uattribute" "uAttribute" 4 "Doc" $true `
  "Opens Attribute Manager to sync and edit Layer, Name, Color, and user keys, with optional area/volume calculation." `
  @(
    "Scope Selected / Visible / All|Which objects the table covers.",
    "Sync / Set|Read attributes from objects or write edits back.",
    "Attribute / Group-by / Search|Filter keys and group rows.",
    "Clear Color / Group / Expand|Colour and grouping helpers.",
    "Cal Volume / Cal Area + mm/m|Compute and show measures.",
    "Import / Export / Web|Exchange attribute tables."
  ) $null `
  "Free/Trial: Attribute Manager is Pro-gated." $null

CmdPage "doc" "usort" "uSort" 5 "Doc" $true `
  "Opens the floating sort-order toolbar. Sort and bake actions stay on the toolbar (Select, Clear, X/Y/Z, Rad, Crv, Rev, Group, Loft, Nurbs, Poly)." `
  $null $null `
  "Free/Trial: ``uSort`` is Pro-gated." $null

CmdPage "doc" "utolerance" "uTolerance" 6 "Doc" $true `
  "Opens a floating toolbar that temporarily overrides Absolute Tolerance while other commands run. Turning it off restores the file tolerance." `
  @(
    "Tolerance|Absolute tolerance value to use while enabled.",
    "Enable / Disable|Apply the override or restore the document tolerance."
  ) $null $null $null

CmdPage "doc" "uquicktools" "uQuickTools" 7 "Doc" $true `
  "Shows the Quick Tools menu at the cursor. Each item runs a configured command or macro (Once / PerObject). Configure the list with ``uQuickToolsConfig``." `
  $null `
  "``Select item from quick tools (move to highlight, click to run, ESC to cancel)``" `
  "Free/Trial: Quick Tools is Pro-gated." $null

CmdPage "doc" "uquicktoolsconfig" "uQuickToolsConfig" 8 "Doc" $false `
  "Modal setup for Quick Tools items (commands and macros). Saves to the Quick Tools config file." `
  @(
    "+ Cmd / + Macro / Edit / − / ▲ / ▼|Build and reorder the item list.",
    "Reset / Import / Export / folder|Restore defaults or exchange a config file.",
    "Mode column|Once or PerObject for each item."
  ) $null `
  "Free/Trial: Quick Tools config is Pro-gated." $null

CmdPage "doc" "uscopebox" "uScopeBox" 9 "Doc" $true `
  "Creates six clipping planes from a box (draw 3-point or select an existing box), grouped as a ScopeBox." `
  @(
    "Mode|SelectBox or Draw3PtBox.",
    "Size|Clipping-plane display size.",
    "DeleteExisting|Remove prior ScopeBox objects when any exist."
  ) `
  "``Corner 1``; ``End of edge``; ``Width``; ``Height``; or ``Select Box``." $null $null

CmdPage "curve" "uscalecrvatt" "uScaleCrvAtt" 1 "Curve" $true `
  "Scales curves about their midpoint, or extends them by a length on both ends, the start, or the end." `
  @(
    "Mode|Scale or Extend.",
    "Side|Both / Start / End (Extend only)."
  ) `
  "``Select curves to scale`` or ``Select curves to extend``; then ``Scale Factor`` or ``Extension length``." $null $null

CmdPage "curve" "uflipcrv" "uFlipCrv" 2 "Curve" $true `
  "Flips curve direction to match a vector, a world axis, or a guide-curve tangent." `
  @(
    "X / Y / Z / Crv|Flip toward that axis or toward a guide curve."
  ) `
  "``Select curves to flip``; then pick a flip vector or ``Select guide curve``." $null $null

CmdPage "curve" "upolytonurbscurve" "uPolyToNurbsCurve" 3 "Curve" $true `
  "Filters polyline vertices by tolerance, then replaces the polyline with a cubic interpolated NURBS curve." `
  @(
    "Tolerance|Vertex filter tolerance."
  ) `
  "``Select polyline curves``." $null $null

CmdPage "curve" "utrygetcircle" "uTryGetCircle" 4 "Curve" $true `
  "Fits closed curves to circles and open curves to endpoint-preserving arcs, then reports deviation against the document absolute tolerance." `
  $null `
  "``Select curves to fit as circles or arcs``." $null $null

CmdPage "surface" "uflipsrf" "uFlipSrf" 1 "Surface" $true `
  "Flips surface or Brep normals to align with a vector, a world axis, or a guide curve." `
  @(
    "X / Y / Z / Crv|Flip toward that axis or toward a guide curve."
  ) `
  "``Select surfaces to flip``; then pick a flip vector or guide curve." $null $null

CmdPage "brep" "uscalebrep" "uScaleBrep" 1 "Brep" $true `
  "Scales Brep, Mesh, or Surface geometry about the centroid by a factor." `
  $null `
  "``Select Brep/Mesh/Surface to scale``; ``Scale Factor``." $null $null

CmdPage "brep" "ucombinenurbs" "uCombineNurbs" 2 "Brep" $true `
  "Extracts and direction-matches Brep or surface edges, rebuilds them, and loft-combines them. Preview first, then bake." `
  @(
    "DirectionMode|Line or Curve.",
    "BakeMode|ByLayer or ByObject.",
    "AngleTolerance / SampleCount / SegmentLength / JoinTolerance|Rebuild and join controls.",
    "SplitZone / ClosedLoft / SortByBoundary / GuidePoints / PairSimilar|Matching and loft behaviour.",
    "DeleteOriginal / GroupResult / CapResult / ShowIsocurves|Yes/No result toggles."
  ) `
  "``Select Breps or surfaces to combine``; ``Select direction curve``; ``Guide point (Enter when done)``." `
  "Free/Trial: preview only; baking is disabled." $null

CmdPage "brep" "uloftpro" "uLoftPro" 3 "Brep" $true `
  "Distributes section objects along rails with a live preview. Choose Loft or Sweep, optional cap, then Enter to bake." `
  @(
    "Mode (rails)|PerPlane or PerHorPln.",
    "DivideDist|Spacing along the rails.",
    "Method|Current Loft or Sweep.",
    "Cap / Flip_Rails / Reselect_Objects / Pick_New_Origin|Preview adjustments."
  ) `
  "``Select Alignment curves (Rails)``; ``Select Objects to Distribute``; ``Pick Reference Point (Origin)``; ``Previewing... Enter to Bake.``" `
  "Free/Trial: preview only; baking is disabled." $null

CmdPage "brep" "usmoothpolysrf" "uSmoothPolySrf" 4 "Brep" $true `
  "Smooths polysurface edges using the same combine/loft-style option set as ``uCombineNurbs``." `
  @(
    "DirectionMode / BakeMode / rebuild doubles / Yes-No toggles|Same named set as ``uCombineNurbs``."
  ) `
  "``Select Breps or surfaces``; ``Select direction curve``; ``Guide point (Enter when done)``." `
  "Free/Trial: preview only; baking is disabled." $null

CmdPage "brep" "ufacefromdirection" "uFaceFromDirection" 5 "Brep" $true `
  "Extracts Brep faces whose normals align with a direction within an angle tolerance." `
  @(
    "Reverse|No/Yes.",
    "BothDirections|No/Yes."
  ) `
  "``Select brep to extract faces``; direction points (Enter for Z-axis); ``Angle tolerance in degrees``." $null $null

CmdPage "mesh" "umeshpatch" "uMeshPatch" 1 "Mesh" $true `
  "Patches a mesh from closed boundary curve(s) using a tensile soap-film or Laplacian relax." `
  @(
    "BoundaryEdgeLength / Grading / RelaxIterations|Mesh density and relax controls.",
    "SlideBoundary|Fixed or Slide.",
    "RelaxMode|Laplacian or Tensile.",
    "MatchAttributes / DeleteInput|No/Yes."
  ) `
  "``Select closed boundary curve(s) to patch``." $null $null

CmdPage "mesh" "umeshtonurbs" "uMeshToNurbs" 2 "Mesh" $true `
  "Converts meshes (including IFC tessellation) to NURBS while keeping attributes. Quality presets drive faceted and analytic fits (prisms, tubes, circular holes, auto-heal). Rotational parts become real cylinders or cones; multi-piece meshes convert piece by piece and unconvertible pieces stay meshes (PARTIAL)." `
  @(
    "Quality|Fast / Balanced / Tight (default Balanced).",
    "Output|Replace or Copy.",
    "Advanced|No/Yes — unlocks Mode, Method, HealOpen, Tolerance, TimeLimit, MaxFaces, CheckObjects, Report.",
    "Mode (Advanced)|Auto / Primitives / Pipe / Extrude / Freeform.",
    "Method (Advanced)|Smart / Faceted / Analytic.",
    "HealOpen / Tolerance / TimeLimit / MaxFaces / CheckObjects / Report|Advanced conversion controls (Tolerance 0 = auto)."
  ) `
  "``Select IFC meshes (Enter = all meshes)``." `
  "Free/Trial: maximum 50 meshes per run." $null

CmdPage "mesh" "umeshoutline" "uMeshOutline" 3 "Mesh" $true `
  "Projects surfaces, polysurfaces, or meshes to a plane and returns outline polylines." `
  @(
    "Plane|CPlane / World / View.",
    "Merge|All / ByLayer / PerObject."
  ) `
  "``Select objects to outline``." `
  "Free/Trial: first 5 objects only." $null

CmdPage "drafting" "ufindcreateblock" "uFindCreateBlock" 1 "Drafting" $true `
  "Finds rigidly translated or rotated copies of a selected assembly and converts the matches to one block definition." `
  $null `
  "``Select one repeated assembly…``; ``Block base point``; ``Matching tolerance``; ``New block name``; confirm convert (No/Yes)." $null $null

CmdPage "drafting" "usection" "uSection" 2 "Drafting" $true `
  "Cuts section curves from selected solids, meshes, or curves with a line or plane cutter; optional project and bake." `
  @(
    "Mode|LineCut or PlaneCut.",
    "SelectResults / BakeCutter / OutputLayer / GroupOutput / Project / Plane|Result and placement controls.",
    "ExtentY|PlaneCut extent."
  ) `
  "``Select objects to section``; section line or plane source; placement point (Enter = place at cut)." `
  "Free/Trial: preview only; baking is disabled." $null

CmdPage "drafting" "uannotation" "uAnnotation" 3 "Drafting" $true `
  "Opens the floating annotation toolbar. Dimension style, scale, show/match/sync, and auto-link actions stay on the toolbar." `
  $null $null `
  "Free/Trial: Annotation is Pro-gated." $null

CmdPage "drafting" "umergehatch" "uMergeHatch" 4 "Drafting" $true `
  "Unions two or more hatches into one hatch, keeping the first hatch's pattern." `
  $null `
  "``Select hatches to merge``." $null $null

CmdPage "drafting" "udist" "uDist" 5 "Drafting" $true `
  "Measures the distance between two points; optional bake and clipboard." `
  @(
    "BakeResult|No/Yes.",
    "UnitDisplay|Document or Meters."
  ) `
  "``Start point``; ``End point``." $null $null

CmdPage "drafting" "ulength" "uLength" 6 "Drafting" $true `
  "Sums the lengths of selected curves; optional bake as a text dot." `
  @(
    "BakeResult|No/Yes.",
    "UnitDisplay|Document or Meters."
  ) `
  "``Select Curves``." $null $null

CmdPage "drafting" "ulevel" "uLevel" 7 "Drafting" $true `
  "Reports a point level along X, Y, or Z relative to World or CPlane." `
  @(
    "BakeResult / UnitDisplay|Bake and units.",
    "Reference|CPlane or World.",
    "AxisX / AxisY / AxisZ|Cycle which axis is reported."
  ) `
  "``Pick point``." $null $null

CmdPage "drafting" "udiffz" "uDiffZ" 8 "Drafting" $true `
  "Reports ΔX / ΔY / ΔZ between two points." `
  @(
    "BakeResult / UnitDisplay|Bake and units.",
    "AxisX / AxisY / AxisZ|Which deltas to emphasise."
  ) `
  "``First Point``; ``Second Point``." $null $null

CmdPage "drafting" "uangle" "uAngle" 9 "Drafting" $true `
  "Measures the angle at a vertex between two rays." `
  @(
    "BakeResult|No/Yes."
  ) `
  "``Vertex``; ``Point 1``; ``Point 2``." $null $null

CmdPage "drafting" "ugap" "uGap" 10 "Drafting" $true `
  "Reports the min/max gap between two geometries. Pick a point for a local gap, or Enter to bake min/max." `
  @(
    "BakeResult / UnitDisplay|Bake and units."
  ) `
  "``Select Source…``; ``Select Target…``; ``Pick point on Source to measure gap (Enter = bake Min/Max)``." $null $null

CmdPage "drafting" "uarea" "uArea" 11 "Drafting" $true `
  "Totals the area of surfaces, meshes, hatches, or closed curves." `
  @(
    "BakeResult / UnitDisplay|Bake and units."
  ) `
  "``Select Objects for Area``." $null $null

CmdPage "drafting" "uvolume" "uVolume" 12 "Drafting" $true `
  "Totals the volume of closed Breps or meshes." `
  @(
    "BakeResult / UnitDisplay|Bake and units."
  ) `
  "``Select Closed Brep/Mesh``." $null $null

CmdPage "drafting" "uslope" "uSlope" 13 "Drafting" $true `
  "In-plane slope (run = X, rise = Y) in World or CPlane, as percent or ratio; optional draw at a slope %." `
  @(
    "BakeResult / Display / Plane|Bake, Percent/Ratio, CPlane/World.",
    "Draw / Slope / Scale|Optional draw helpers."
  ) `
  "``Pick Point 1 (Top/Bottom)``; ``Pick Point 2`` or run direction." $null $null

CmdPage "drafting" "u3dslope" "u3dSlope" 14 "Drafting" $true `
  "3D slope between two points (horizontal/vertical), as percent or ratio." `
  @(
    "BakeResult / Display / Scale|Bake, Percent/Ratio, and ratio scale."
  ) `
  "``Pick Point 1 (Top/Bottom)``; ``Pick Point 2``." $null $null

CmdPage "cad" "udwg" "uDwg" 1 "CAD" $true `
  "Transfers selected curves, points, blocks, dimensions, hatches, and text to a running AutoCAD session via COM / DWG batch." `
  @(
    "LayerExport|ChildOnly or Full.",
    "KeepStyle|ByLayer or ByObject.",
    "ConvertCurve|No/Yes.",
    "InsertBlock|Integer; 0 = always block."
  ) `
  "``Select objects to transfer (Esc to cancel)``." `
  "Free/Trial: maximum 5 objects." $null

CmdPage "cad" "udwgimport" "uDwgImport" 2 "CAD" $true `
  "Dialog import of one or more DWG/DXF files or a folder, with a unit override." `
  @(
    "Unit|Default through Miles, or open Document Properties Units.",
    "Browse file(s) / folder|Choose what to import."
  ) $null $null $null

CmdPage "cad" "udwgexport" "uDwgExport" 3 "CAD" $true `
  "Batch-exports the selection to DWG, 3DM, or DXF by Object or Layer grouping, with composable file names and ancestor folders." `
  @(
    "Format / prefix|``.dwg`` / ``.3dm`` / ``.dxf`` and optional file-name prefix.",
    "Export mode|Object or Layer; Layer level N (0–9).",
    "File name ticks|Level (N), Path below N, Layer name, Suffix.",
    "Object layer path|Path from N down, or layer name only.",
    "Subfolders / ancestors / Ref_box / Start number / date / Replace|Folder and naming extras."
  ) `
  "``Select objects to batch export``." `
  "Free/Trial: maximum 2 files per run." $null

CmdPage "cad" "uregen" "uRegen" 4 "CAD" $true `
  "Calls AutoCAD ``Regen`` on the active document through COM. AutoCAD must be running." `
  $null $null $null $null

CmdPage "ifc" "uifcimport" "uIfcImport" 1 "IFC" $true `
  "Dialog import of IFC file(s) or a folder through Rhino built-in, IfcOpenShell, or xBIM, with offset and layer options." `
  @(
    "Engine|Rhino Built-in / IfcOpenShell / xBIM.",
    "Import Abstract/Spatial / include subfolders|What to bring in.",
    "If layer root exists|Replace or Skip.",
    "Detailed .log / native Brep / organize by IFC type|Import behaviour.",
    "Write Document User Text / object keys with [Type]|Attribute seeding.",
    "Sharp edge angle / Offset X Y Z (m)|Geometry controls."
  ) $null $null $null

CmdPage "ifc" "uifcexport" "uIfcExport" 2 "IFC" $true `
  "Exports the selection to IFC through Python ifcopenshell or Xbim after an options dialog. Default SitePlacement is Local (OpenBIM). Missing SitePlacement / MapConversion values are seeded into Document User Text when needed." `
  @(
    "Save path / Engine|Python or Xbim.",
    "Schema|IFC2x3 / IFC4 / IFC4.3.",
    "Meshing|Render Mesh or Detail Mesh (+ max angle / edge).",
    "IFC4X3 Bridge / Optimize IFC4 mesh / detailed .log|Schema extras."
  ) `
  "``Select objects to export to IFC``." `
  "Free/Trial: IFC export is Pro-gated." `
  @"
## Document User Text

Run [``uIfcSetupTemplateFile``](../uifcsetuptemplatefile/) before a serious export. Check keys in **Document Properties $arrow User Text**.

| Key | Default | Meaning |
| --- | --- | --- |
| ``IFC.SitePlacement`` | ``Local`` | Site Z = 0. ``Anchor`` / ``Mean`` / ``Legacy`` use older site anchoring. |
| ``IFC.Storey.{Building}.{Storey}.Elevation`` | min Z if unset | Storey elevation; name must match layer path segment 4. |
| ``IFC.MapConversion.*`` | seeded when Local and empty/0 | Georeference. |
| ``IFC.Offset.X/Y/Z`` | ``0`` | Geometry offset, independent of MapConversion. |
| ``IFC.Schema`` | ``IFC4`` | ``IFC4`` / ``IFC2X3`` / ``IFC4X3``. |
| ``IFC.UseBridge`` | off | ``True`` with IFC4X3 uses IfcBridge / IfcBridgePart. |

Property types live in the key. See [``uIfcApplySharedParams``](../uifcapplysharedparams/).
"@

CmdPage "ifc" "uifcsetuptemplatefile" "uIfcSetupTemplateFile" 3 "IFC" $true `
  "Creates an IFC template: ``Project::Site::Building::Storey::…`` layers, Document User Text (including ``IFC.SitePlacement=Local``), built-in shared parameters, samples, and a **TypeCatalog_Sample** object." `
  $null $null $null `
  "See [``uIfcExport``](../uifcexport/) for the Document User Text table."

CmdPage "ifc" "uifcapplysharedparams" "uIfcApplySharedParams" 4 "IFC" $true `
  "Copies ``IFC.SharedParam.*[Type]`` document keys onto the selection (skips keys that already exist on the object). The type token is in the key; the value is user data." `
  $null `
  "``Select objects to apply shared parameters``." $null `
  @"
## Key shape

``````text
Right: Dimensions.QTO.Area[Area] = 12.5
Right: Pset_WallCommon.IsExternal[YesNo] = False
Wrong: Spec.Flag = True[IfcBoolean]
``````

| Token in ``[…]`` | IFC nominal value |
| --- | --- |
| ``Text`` / ``IfcLabel`` | ``IfcLabel`` |
| ``IfcText`` | ``IfcText`` |
| ``IfcIdentifier`` | ``IfcIdentifier`` |
| ``YesNo`` / ``IfcBoolean`` | ``IfcBoolean`` |
| ``Integer`` / ``IfcInteger`` | ``IfcInteger`` |
| ``Number`` / ``IfcReal`` | ``IfcReal`` |
| ``Length`` / ``Area`` / ``Volume`` | length / area / volume measures |
| ``IfcDate`` / ``IfcDateTime`` / ``IfcTime`` / ``IfcDuration`` | time types |
"@

CmdPage "ifc" "uifcinstall" "uIfcInstall" 5 "IFC" $true `
  "Checks and installs ``ifcopenshell``, ``numpy``, and ``orjson`` into Rhino's Python environment." `
  @(
    "Install / Close|Dialog actions."
  ) $null $null $null

CmdPage "more" "commamenu" "commaMenu" 1 "More" $false `
  "Opens the compact type-based context menu (Doc / Curve / Surface / Brep / Mesh / Drafting / CAD / IFC), plus License Manager, About, and the built-in user manual." `
  $null $null $null $null

CmdPage "more" "uexportbox" "uExportBox" 2 "More" $false `
  "Parallel mesh export of geometry clipped by a closed box." `
  @(
    "Preset|Speed / Quality / Custom.",
    "IncludeHidden|No/Yes.",
    "Boolean|Off/On."
  ) `
  "``Select clipping box (closed polysurface)``; then a save-path dialog." $null $null

CmdPage "more" "uvisibilityadd" "uVisibilityAdd" 3 "More" $false `
  "Adds more objects to an already-open Visibility panel. Open the panel first (from ``uObject`` or the Doc visibility tools)." `
  $null `
  "``Select more objects to add.``" `
  "Free/Trial: Visibility is Pro-gated; the panel itself caps Free/Trial at 10 objects." $null

# --- Tekla / Revit stubs ---
W "tekla/_index.md" @"
---
title: CommaTs
layout: hextra-home
---

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>Tekla Structures</span>
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  CommaTs
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Model and drawing plugins for Tekla Structures.&nbsp;<br class="hx:sm:block hx:hidden" />
  Guide pages will publish here as the Tekla team pushes them.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6 hx:flex hx:flex-wrap hx:gap-3">
{{< hextra/hero-button text="Docs placeholder" link="docs" >}}
{{< hextra/hero-button text="Report an issue" link="https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Atekla" >}}
</div>
"@

W "tekla/docs/_index.md" @"
---
title: CommaTs docs
linkTitle: Documentation
cascade:
  type: docs
---

Tekla guide content is not in this repository yet. Collaborators can add markdown under ``content/tekla/docs/`` on ``main``; GitHub Actions will publish it.

Until then, the existing public Tekla guide remains at [trungvuduy.github.io/comma-ts-releases](https://trungvuduy.github.io/comma-ts-releases/). Use the ``tekla`` label on [Issues](https://github.com/Comma3D/comma-docs/issues).
"@

W "revit/_index.md" @"
---
title: CommaRvt
layout: hextra-home
---

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>Revit</span>
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  CommaRvt
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Revit tools — placeholder until the product ships.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-button text="Report an issue" link="https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arevit" >}}
</div>
"@

W "revit/docs/_index.md" @"
---
title: CommaRvt docs
linkTitle: Documentation
cascade:
  type: docs
---

CommaRvt is not released yet. This section is a placeholder so the suite navbar stays stable. Use the ``revit`` label on [Issues](https://github.com/Comma3D/comma-docs/issues) when that product starts.
"@

Write-Host "content built"
