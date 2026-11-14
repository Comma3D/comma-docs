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
    # $limits kept for call-site compatibility; never written to the page.
    $alias = $title.ToLowerInvariant()
    if ($onMenu) {
        $menu = "``commaMenu`` $arrow **$group**"
    } else {
        $menu = "Not on ``commaMenu``. Type the command name."
    }
    $optBlock = OptTable $options
    $body = @"
---
title: $title
weight: $weight
aliases:
  - /help/$alias/
---

| Menu | Command |
| --- | --- |
| $menu | ``$title`` |

$summary
"@
    if ($prompts) {
        # Turn prompt strings into Rhino-style Steps when they look like a sequence.
        $steps = @()
        foreach ($p in ($prompts -split ';')) {
            $t = $p.Trim().TrimStart('`').TrimEnd('`').Trim()
            if ($t) { $steps += $t }
        }
        if ($steps.Count -gt 0) {
            $body += "`n`n#### Steps`n"
            $i = 1
            foreach ($s in $steps) {
                $body += "`n$i. $s"
                $i++
            }
            $body += "`n"
        }
    }
    if ($optBlock) {
        $body += "`n`n#### Options`n`n$optBlock"
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

{{< brand-logo name="comma" height="3.5rem" >}}

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

{{< brand-logo name="rhino" height="4rem" >}}

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Modeling, drafting, and CAD/IFC exchange for Rhino 8.&nbsp;<br class="hx:sm:block hx:hidden" />
  Install from the Package Manager (``CommaRh``).
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6 hx:flex hx:flex-wrap hx:gap-3">
{{< hextra/hero-button text="Documentation" link="docs" >}}
{{< hextra/hero-button text="Report an issue" link="https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arhino" >}}
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card title="Getting started" subtitle="Package Manager install, the type menu, and the licence on this computer." link="docs/getting-started/" >}}
  {{< hextra/feature-card title="Changelog" subtitle="Package Manager update history for CommaRh releases." link="docs/getting-started/changelog/" >}}
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

Install from the Rhino Package Manager. See the [Changelog](getting-started/changelog/) for Package Manager update history. To report a problem, open [Issues](https://github.com/Comma3D/comma-docs/issues) and add the ``rhino`` label.
"@

W "rhino/docs/getting-started/_index.md" @"
---
title: Getting started
weight: 1
---

Install CommaRh, open the menu, check the licence, and read the [Changelog](changelog/) for Package Manager updates.
"@

W "rhino/docs/getting-started/installing.md" @"
---
title: Installing
weight: 1
---

Every public command documented under Rhino ships together in one Package Manager package, **CommaRh**. One install gives you the type menu, the panels, CAD/IFC exchange, and the licence manager — there is no separate installer to download, and you do not copy files by hand.

- To install: open Rhino 8 on Windows, run ``PackageManager``, search for ``CommaRh``, and click **Install**.
- Supported versions: Rhino 8 (Windows).
- Current guide version: 26.1.9. Package Manager shows the version that is installed on this computer.
- Update history: [Changelog](changelog/) (and GitHub Releases tagged ``CommaRh-v*`` on [Comma3D/comma-docs](https://github.com/Comma3D/comma-docs/releases)).

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

``commaMenu`` also includes **License Manager** (``commaRegister``), **About**, and **User Manual** (opens the online docs).

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
weight: 5
---

Problems are tracked on [Comma docs Issues](https://github.com/Comma3D/comma-docs/issues). Use the ``rhino`` label for CommaRh.

Issues are for **new** reports. Past Package Manager updates live on the [Changelog](changelog/), not as backfilled issues.

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
weight: 6
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

# Detailed command pages (Steps + Options from code research)
$gen = Join-Path $PSScriptRoot "_gen_commands.py"
if (-not (Test-Path $gen)) { throw "_gen_commands.py missing." }
python $gen
if ($LASTEXITCODE -ne 0) { throw "_gen_commands.py failed." }

# CommaRh Package Manager history — short user notes (not the developer CHANGELOG)
$changelogSrc = Join-Path $PSScriptRoot "_changelog-user.md"
if (-not (Test-Path $changelogSrc)) { throw "_changelog-user.md missing." }
$clBody = [System.IO.File]::ReadAllText($changelogSrc).Trim()
$clBody = [regex]::Replace($clBody, "^#\s+[^\r\n]+\s*", "")
$changelogPage = @"
---
title: Changelog
weight: 4
---

What changed in each **CommaRh** Package Manager version.

Report a new problem on [Issues](https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arhino). Release tags: [CommaRh-v* on comma-docs](https://github.com/Comma3D/comma-docs/releases).

$clBody
"@
W "rhino/docs/getting-started/changelog.md" $changelogPage

Write-Host "content built"
