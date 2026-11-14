# Comma docs

Public user guides for Comma products:

| Product | Path | Status |
| --- | --- | --- |
| CommaRh | `content/rhino/` | Published |
| CommaTs | `content/tekla/` | Placeholder (migrate from the Tekla site when ready) |
| CommaRvt | `content/revit/` | Placeholder |

Live site: https://comma3d.github.io/comma-docs/

Issues: https://github.com/Comma3D/comma-docs/issues  
Use labels `rhino`, `tekla`, or `revit`.

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
