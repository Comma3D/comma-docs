# Comma docs

Public user guides for Comma products:

| Product | Path | Status |
| --- | --- | --- |
| CommaRh | `content/rhino/` | Published |
| CommaGh | `content/grasshopper/` | Published (written by hand, the component pages are generated, see below) |
| CommaTs | `content/tekla/` | Published (generated from the CommaTs guide, see below) |
| CommaRvt | `content/revit/` | Installation and troubleshooting guide |

Live site: https://comma3d.github.io/comma-docs/

Issues: https://github.com/Comma3D/comma-docs/issues  
Use labels `rhino`, `tekla`, or `revit` (a `grasshopper` label is still to be created).

## Contribute

1. Edit markdown under `content/`.
2. Push to `main` (or open a PR).
3. The **Deploy Pages** workflow builds Hugo 0.162 + Hextra v0.13 and publishes the site.

```powershell
# Local preview
git clone --depth 1 --branch v0.13.0 https://github.com/imfing/hextra.git themes/hextra
hugo server
```

Do not commit `public/`, `themes/`, or `.tools/`. Plugin source stays private.

## From the monorepo

```powershell
cd src/CommaDocs
.\publish.ps1          # regenerate content + local Hugo build
.\publish.ps1 -Deploy  # push source to this repository
```

### CommaTs pages are generated

`content/tekla/` and `static/images/tekla/` are written by `src/CommaTs/docs/site/scripts/convert-guide.mjs` from the CommaTs
guide (`src/CommaTs/docs/PluginGuide.html`) and committed here. To change a CommaTs page, edit the guide, run `npm run build`
in `src/CommaTs/docs/site`, and commit the result with it; do not edit `content/tekla/` by hand. `_build-content.ps1` rebuilds the
rest of `content/` and leaves `content/tekla/` alone. The Help button of every CommaTs tool opens
`https://comma3d.github.io/comma-docs/tekla/help/<tool>/`, an alias of that tool's page: keep those addresses working.

### CommaGh pages

`content/grasshopper/` is written by hand (home, Getting started, Script Organizer, Container), except `content/grasshopper/docs/components/`
and `static/images/grasshopper/components/`: those are generated from the plugin's C# component classes by
`src/Grasshopper/docs/scripts/generate-components.mjs` and committed. Run `npm run generate` in
`src/Grasshopper/docs` after a component changes (add `-- --source <dir>` while `src/Grasshopper/Comma.GH.Components` is older than
the plugin that ships), then `npm run check` (with the same `-- --source <dir>`) after a Hugo build. Do not edit the generated pages by hand. `_build-content.ps1`
rebuilds the rest of `content/` and leaves `content/grasshopper/` alone. Every component page is also reachable at
`https://comma3d.github.io/comma-docs/grasshopper/help/<id>/` (the class name without `Component`, in lower case): keep those
addresses working. See `src/Grasshopper/docs/README.md`.

### After a CommaRh Yak ship

1. Add short user bullets to `_changelog-user.md` (not the developer `CommaRh/CHANGELOG.md`).
2. Run (personal GitHub account with Write on this repo):

```powershell
.\release-docs.ps1     # deploy Pages + create/skip CommaRh-v* releases
```

Releases: https://github.com/Comma3D/comma-docs/releases  
Do not publish CommaRh release notes on private `Comma3D/Comma`.
