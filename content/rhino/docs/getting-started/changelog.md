---
title: Changelog
weight: 4
---

Package Manager update history for **CommaRh**. Source of truth: `src/CommaRh/CHANGELOG.md`. GitHub Releases use tags `CommaRh-v*` on [Comma3D/Comma](https://github.com/Comma3D/Comma/releases?q=CommaRh).

Report new problems on [Issues](https://github.com/Comma3D/comma-docs/issues?q=is%3Aissue+label%3Arhino) — do not open issues for past release notes.

All notable changes to CommaRh will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [26.1.9] - 2026-11-14

### Changed
- **About / User Manual:** Opens online CommaRh docs (`https://comma3d.github.io/comma-docs/rhino/`) instead of the old embedded HTML guide; removed `CommaRh_UserGuide.html` from the package.
- Version bump to 26.1.9 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

---

## [26.1.8] - 2026-11-11

### Added
- **uMeshToNurbs - tubes (PipeTrace):** Round bars and tubes are rebuilt from cross-sections walked along the axis: solid and hollow (outer and inner radius), straight or bent (lines and tangent arcs, U-bends as two bends plus a short straight), as real cylinders. Cut ends are taken from the mesh: square, mitre, bevel and compound bevel (end plane + half-space cut), and saddle copes against a mating tube (cutter cylinder, equal-size tubes included). When an end cannot be reproduced the plain tube is delivered up to the farthest rim point (info `uncut`) and the cut is left to the user. Runs before the beam ladder (railing posts: 181-251 faces and 2 s down to 4-5 faces and 0.15 s).
- **uMeshToNurbs - CSG rebuild:** When every region was fitted but the joined brep does not close (a rod with a through slot, for example), the part is rebuilt from the fitted planes and cylinders: cells are classified inside/outside by ray parity against the mesh (IFC face normals are not trusted) and united.
- **uMeshToNurbs - low-poly fasteners:** A piece that stays CHECK is retried with a relaxed plane angle (3, then 6 degrees): end caps and facets of bolt shanks, washers and heads are planar only within 2-5 degrees and were dropped silently at 1 degree.
- **uMeshToNurbs - touching solids:** Meshes whose edge-connected shells are all closed manifolds (welds touching a plate along an edge) are converted shell by shell. Tiny closed meshes try the face fitter before the beam ladder.
- **uMeshToNurbs - failure cache:** Identical pieces that failed every strategy are not retried (Tekla bolt sets: about 40 % less time).
- **uMeshToNurbs - Revolve:** New converter for solids of revolution (stud bolts, shafts, rods, rings, cones, washers). It finds the axis with a per-slice circle fit, groups vertices into rings, walks the meridian, builds a line-and-arc profile, and revolves one face per segment, so cylinders, cones and tori are real analytic faces (a Tekla stud: about 240 faces down to 6). The result is accepted only when deviation, volume and solid checks pass. Runs in Auto and Primitives for every Quality.
- **uMeshToNurbs - pieces:** Meshes made of several disjoint pieces (Tekla bolt sets, grouped parts) are converted piece by piece and merged into one Brep. Identical pieces reuse the shape cache. A piece that cannot become a solid stays a mesh (`PARTIAL`) instead of failing the whole object.
- **uMeshToNurbs - working tolerance:** The automatic tolerance follows the tessellation (about 1.5 x the median chord sagitta of curved edges), capped at 0.4 % of the bounding-box diagonal and at 2 mm (converted to model units). The document tolerance is far below the chord error of curved meshes, so analytic fits used to fail and fall back to facets.
- **uMeshToNurbs - verification gate:** Every non-faceted result must stay within 2.5 x working tolerance of the mesh and keep its volume within -15 % / +25 % (absolute values, because pieces can have mixed orientation). Failures fall back to the faceted solid.
- **uMeshToNurbs - report:** Summary line `exact NURBS / faceted / partial / kept as mesh`.
- **uMeshToNurbsBenchDoc (NoShip):** CSV adds `AnalyticFaces`, `MaxDev`, `VolRatio`.

### Changed
- **uMeshToNurbs - faceted merge:** Coplanar merge widens in steps (x2.5) while the solid stays valid and within the working tolerance of every mesh vertex (a 1 degree angle tolerance alone moved long faces by up to 10 mm). Face counts drop sharply on slabs and plates.
- **uMeshToNurbs - time:** Hard per-mesh cap = min(2 x TimeLimit, (0.8 s + 4 ms x faces) x TimeLimit / 5 s). Deviation checks are time-bounded and sample-limited on dense breps. A bolt-set mesh no longer runs past 45 s.
- **uMeshToNurbs:** Tolerance and Advanced reset on every run.
- Version bump to 26.1.8 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

### Fixed
- **uMeshToNurbs:** A degenerate torus (tube radius larger than the ring radius) made the trimming explode (one weld mesh ran 46 s); refined tori are validated again.
- **uMeshToNurbs:** The faceted fallback froze the UI thread on dense meshes (coplanar merge is not interruptible and grows about with the cube of the face count: 3300 triangles 36 s). It is skipped above 1600 triangles and limited to one merge pass above 800; Smart continues with Revolve/Pipe/Beam.
- **uMeshToNurbs:** A thin plate converted to a sheet with one third of the volume (distance checks cannot see this) is now rejected by the volume gate.

---

## [26.1.7] - 2026-11-06

### Changed
- **uMeshToNurbs:** Beam and column meshes use the v4 profile extrusion (axis, line-and-arc section, end cuts). Auto also tries that path, or Pipe, when the name matches or a cheap shape test says the mesh is a prism or a tube. A specialist result is kept only when the solid is closed and within deviation and volume limits. Otherwise the face fitter still runs, including mixed PARTIAL results. Pipe, Extrude, and Primitives still run only the chosen path.
- Version bump to 26.1.7 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

## [26.1.6] - 2026-11-05

### Fixed
- **uDwg COM:** A line/arc polycurve stays one LWPOLYLINE (bulge arcs). Coplanar tests allow large-coordinate noise. If the bulge polyline cannot be built, the chain becomes one polyline instead of one LINE/ARC per segment.
- **uDwg DWG+INSERT:** Temp DWG writes polycurves as bulge polylines (`SplitPolycurves=false`, `ExportPolycurvesAs=Polybulges`) so exploding the INSERT no longer drops a line/arc chain into separate LINE and ARC entities.
- **uDwg `InsertBlock`:** Command option (default 100, same prompt style as `ConvertCurve`). Batch larger than this stays one block; `0` always stays one block.
- **uDwg `ConvertCurve`:** Yes facets freeform at document tolerance on both COM and DWG+INSERT, including curves inside blocks, and stitches coplanar spans into one polyline. No still joins line/arc and leaves freeform as a spline.
- Version bump to 26.1.6 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

## [26.1.5] - 2026-11-04

### Fixed
- **uDwg COM:** Polycurve line+arc+freeform no longer fails AutoCAD join when a freeform segment becomes a spline. New option `ConvertCurve` (default Yes, document Absolute/Angle tolerance) facets freeform into the bulge LWPOLYLINE; No keeps consecutive line/arc joined and leaves freeform as a separate spline.

### Changed
- **uMeshToNurbs / Ifc2Nurbs:** Port Desktop v3 torus merge — seed ball + `FitTorus` + `RefineTorus` (LM on vertices) + `TorusSpanOk` instead of pairwise group merge; step timing log; budget checks in grow / merge rounds / seams / trim.
- **uMeshToNurbs:** Drop per-layer OK/OK_SOFT/CHECK command-line table (not useful for end users); keep summary line + optional CSV report.
- **uMeshToNurbs:** Replace `MaxTolerance` + `Accuracy` with one `Quality` option — `Strict` (no retry, fit 1.5) / `Normal` (maxTol 0.4, fit 2.5) / `Loose` (maxTol 10, fit 4).
- **uMeshToNurbs:** Disjoint mixed results → `PARTIAL`: OK pieces replace as NURBS; CHECK pieces added back as mesh objects (selected) instead of discarding the whole joined mesh.
- **uMeshToNurbsBench (NoShip):** Synthetic 90° elbow bench (R/r = 1.5, 2.3, 5; coarse/fine mesh) — ConvertMesh Primitives, no document edits.
- Version bump to 26.1.5 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

## [26.1.4] - 2026-11-03

### Fixed
- **uIfcExport Site elevation:** Default `IFC.SitePlacement=Local` (OpenBIM): `IfcSite` at mean XY with **Z=0**, product Z stays in the engineering datum, storey `ObjectPlacement.Z` = `IFC.Storey.*.Elevation`, seeds `IfcMapConversion` Eastings/Northings/OrthogonalHeight when unset. Opt-in `Anchor` / `Mean` / `Legacy` keeps previous mean-XYZ Site. First export **persists missing Document UserText from the exported layer tree** (`SitePlacement`, Project/Site/Building names, storey Elevations, MapConversion) — never overwrites existing keys; not the full template.
- **Release / Yak load on NETCore (.NET 10):** ConfuserEx stripped to License `rename mode=letters` only. Prior `anti tamper` / `constants` / `ctrl flow` / `unicode` rename left nested types that throw `BadImageFormatException: Enclosing type(s) not found` when Rhino 8.36+ loads under .NET 10 (clean `bin` worked; Publish/Yak failed). Build now runs `Validate-NetCoreLoad.ps1` on obfuscated outputs.
- **uDwg:** AutoCAD 2027 hatch `AppendOuterLoop` via typed `AcadEntity[]`; curves/points/blocks/dims one DWG INSERT; abort when CAD is busy instead of freezing Rhino on long `SendCommand` waits.
- **uRegen / load:** Rhino 8.36 .NET 10 no longer fails plugin load on `Marshal.GetActiveObject` (use `ComHelper.GetRunningComObject`).

### Changed
- **uMeshToNurbs:** Shipped in commaMenu Mesh group (was NoShip). Ifc2Nurbs v3 — options `Output=Replace|Copy`, `Tolerance` (0 = auto), `MaxTolerance` retry ladder (tol×2, ×4 … ≤ max; default 0.4), `Accuracy` (fit factor, default 2.5), `TimeLimit` (s/object), `CheckObjects=KeepMesh|ToBrep`, `Report` (CSV next to .3dm or Desktop); all persisted. Copy hides the source mesh and tags the brep with `Ifc2Nurbs_SourceMesh`. Curved groups merged into tori (bent pipe/bar, centerline fit), parameter-space trim rescue (`TrimPullback`), open IFC meshes capped, invalid slivers repaired/dropped. Batch runs on an Eto `UITimer` (UI thread; Rhino.Geometry not free-threaded); Esc cancels. CHECK results cached too. On cancel/time budget, remaining regions become triangles instead of leaving holes; closed shared seams promoted to exact circles.
- **uMeshToNurbs — reconstruct modes:** New `Mode` option: `Auto` (default, rule-based), `Primitives` (v3 analytic), `Pipe`, `Extrude` (stub), `Freeform` (stub). Pattern-based rules match layer/IfcType/name against built-in keywords (e.g. "rebar"→Pipe, "steel"→Extrude). Optional user override via `%AppData%\CommaRh\Ifc2Nurbs.modes.json`. Pipe mode estimates tube radius from dihedral angles, chains centerline via nearest-neighbor, creates `Brep.CreatePipe`; Auto+Pipe falls back to Primitives on failure.
- **uMeshOutline:** Renamed from `uOutlineGeometries` and shipped in Mesh menu; legacy name remains a NoShip alias.
- Version bump to 26.1.4 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

### Added
- **IFC shared params:** `[Type]` accepts any IFC simple/measure name (`IfcBoolean`, `IfcIdentifier`, `IfcCountMeasure`, `IfcDate`, …) in addition to Text/Number/Length/Area/Volume/YesNo. `IfcIdentifier` is no longer flattened to `[Text]`.

## [26.1.3] - 2026-11-03

### Changed
- Version bump to 26.1.3 (shipped package; NETCore obfuscation load still broken until 26.1.4).

## [26.1.2] - 2026-10-18

### Fixed
- **uDwg:** Hatch/annotation COM insert, MText alignment, polycurve arcs, and hatch-select freezes.
- **uAnnotation:** Scale dropdown crash and scales UI stability.
- **Installer:** Stop fake license activation; CDDL/xBIM source offer paths corrected.
- **Packaging:** xBIM native Geometry engines shipped with release builds.

### Added
- **IFC:** Default import layers follow spatial hierarchy; setup/import defaults improved.
- **UI:** Panel icons, text flyout menus, and layer/object panel UX refresh.
- **uAnimation:** Available as NoShip command.

### Changed
- Version bump to 26.1.2 (`Directory.Build.props`, `Comma.RH.csproj`, `CommaLicense/Directory.Build.props`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

## [26.1.1] - 2026-10-16

### Fixed
- **uDwg:** Release/obfuscated builds no longer crash with `BeginPerformanceMode` RuntimeBinderException (ConfuserEx rename + `dynamic` COM call sites). Cad COM helpers keep stable names; performance-mode entry points take `object` and callers cast away `dynamic` before the static call.
- **Packaging:** xBIM native Geometry Engine32/64 copied next to the plugin; ConfuserEx RhinoCommon probe; Publish folder rebuild allowed.

### Changed
- Version bump to 26.1.1 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `XBIM_SOURCE_OFFER.md`).

## [26.1.0] - 2026-09-01

### Added
- **uObject:** Object inspection and selection workspace; Select Similar is an action within the workspace.
- **uTolerance:** Temporary Absolute Tolerance override while commands execute, without leaving the file tolerance changed between commands.
- **uSort:** Selection-order toolbar with X/Y/Z, radial, and curve ordering.
- **uFindCreateBlock:** Find translated or rotated copies of selected geometry and convert all matched assemblies to one Rhino block.

### Changed
- **Commands:** Centralized command catalog (`CommaCommandCatalog`) — single source for commaMenu, command picker, and dev inventory script.
- **Navigation:** `commaMenu` and user documentation use type-based groups: **Doc / Curve / Surface / Brep / Mesh / Drafting / CAD / IFC**. Panel actions remain inside their panels instead of being duplicated in the menu.
- **commaMenu:** Builds from the catalog instead of duplicated inline definitions; tooltips describe the action actually opened by each entry.
- **CommandListDialog:** Full CommaRh command list with categories and descriptions from catalog.
- **QuickTools:** Reserved-command filter accepts camelCase and legacy uppercase config values; removed debug log spam.
- **Curve direction:** The documented command name is `uFlipCrv`.
- **User surface:** Internal/no-ship commands are excluded from normal user guidance.
- **About:** Shows the runtime assembly informational version, current product/workflow summary, built-in User Manual action, `commaRegister` license entry, and support contact `comma3d.aec@gmail.com`.
- **Documentation:** Reworked the Vietnamese manual and bundled English guide for the 26.1.0 workflow model; marked the old all-commands inventory as historical.
- Version bump to 26.1.0 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

### Migration notes
- Replace old workflow category assumptions with the type-based groups listed above.
- Use `commaMenu` for public workflow navigation and `uObject` for object inspection or Select Similar.
- Existing macros using `uSelectSimilar` continue to work through the hidden compatibility alias; update new macros to `uObject`.
- Update macros and documentation that use the previous curve-flip name to `uFlipCrv`.
- Do not depend on internal/no-ship commands as supported release UI.

## [26.0.3] - 2026-08-26

### Changed
- **uLayer:** Main layer input suffix controls naming — `::` (or no suffix) = nested sublayer (`Building::Wall`); `_`/`-`/other non-alnum = merge flat name (`Building_Wall`). Multi-level prefixes like `Building::BlockA::` are supported.
- Version bump to 26.0.3 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

## [26.0.2] - 2026-08-04

### Added
- **uLayer:** optional Main layer input below Setup; when set, layer buttons create/assign under `MainLayer::LayerName` and persist the value in config.

### Changed
- Version bump to 26.0.2 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

## [26.0.1] - 2026-07-19

### Changed
- **uMeshToNurbs:** thin wrapper around native Rhino `MeshToNURB` (+ optional `MergeAllCoplanarFaces`); temporarily overrides document AbsoluteTolerance per run, then restores it.
- License: offline grace (30 days from last online validate), seat revision (`rev`), backend/client sync improvements; registration form updates.
- **uOutlineGeometry:** outline extraction refinements.
- Version bump to 26.0.1 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

## [26.0.0] - 2026-07-07

### Added
- License hardening migration: server-signed license path (`LicenseClient`, `LicenseToken`) with JWT ES256 verification on client.
- New license backend scaffolding (`scripts/LicenseBackend/Code.gs`) and key utility scripts (`tools/genkeys.js`, `tools/encode-endpoint.js`).
- License unit tests (`tests/Comma.License.Tests`) and CI workflow (`.github/workflows/ci.yml`) for build + test validation.
- IFC shared parameters C+B: measure type in Key (`IFC.SharedParam.<Name>[Area]`), plain Value; typed `NominalValue` on export (Python + Xbim); Document key migration helper (`IfcSharedParamKey`).

### Changed
- Version bump to 26.0.0 (`Directory.Build.props`, `Comma.RH.csproj`, `manifest.yml`, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).
- License manager now prefers signed token cache (`License2`) with legacy AES grace fallback for transition.
- Registration and sync flow now prioritize backend activation and keep legacy Google Sheets path as transition fallback.
- Trial duration standardized to 30 days in license paths.
- IFC docs/user guide: shared-param `Key[Type]` convention; Length/Area/Volume property values entered in SI (m/m²/m³), geometry still auto-scaled from Rhino units.

## [3.4.15] - 2026-06-04

### Changed
- **uDwgExport:** Object/Layer modes with combinable File name and Object layer options; layer table level 0 = root; DWG layers follow export options; scrollable dialog with top Export/Cancel bar; merge duplicate output paths in Layer mode.
- Version bump to 3.4.15 (`Comma.RH.csproj`, `Directory.Build.props`, Yak `manifest.yml`, installer script, `Comma.License` assembly info, IFC version fallbacks, bundled user guide).

### Fixed
- **uDwgExport:** File names and preview no longer use Rhino full path when only Level or leaf options are selected; CAD export layer tree matches Object layer choice.

## [3.4.14] - 2026-05-27

### Fixed
- **uExportBox:** fail-safe export when clip/boolean fails — keep original Brep or mesh (no silent drop); Mesh/SubD still processed when bbox test reports Outside.

### Changed
- Version bump to 3.4.14 (`Comma.RH.csproj`, `Directory.Build.props`, Yak `manifest.yml`, installer script, `Comma.License` assembly info, IFC version fallbacks, bundled user guide).

## [3.4.13] - 2026-05-26

### Changed
- Version bump to 3.4.13 (`Comma.RH.csproj`, `Directory.Build.props`, Yak manifest, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

---

## [3.4.12] - 2026-05-15

### Changed
- Version bump to 3.4.12 (`Comma.RH.csproj`, `Directory.Build.props`, Yak manifest, installer script, `Comma.License` assembly info, IFC application version fallbacks, bundled user guide).

---

## [3.4.11] - 2026-05-08

### Added
- **uSelHeaviest:** New Selection command — find and mark the heaviest objects (Brep / Mesh / Surface / PointCloud) by `MemoryEstimate`, label each with a `MB` TextDot at its bounding box center, group dot+object, and select all top-N. Optional `Isolate` toggle hides every other object so only the heaviest objects and their dots remain visible. Last count and isolate state are sticky between runs.

### Changed
- Version bump to 3.4.11 (`Comma.RH.csproj`, `Directory.Build.props`, Yak manifest, installer script, `Comma.License` assembly info, IFC application version fallbacks).

---

## [3.4.10] - 2026-05-08

### Added
- **uIfcImport (IfcOpenShell):** Optional checkbox to build native Brep from IFC extrusions where supported (default off); tessellated meshes remain the default path.

### Changed
- **uIfcImport (IfcOpenShell):** Representation-aware routing, IFC representation metadata on imported objects, and Brep only from native parametric data (no automatic mesh→Brep for faceted or polygonal tessellation).
- Version bump to 3.4.10 (`Comma.RH.csproj`, `Directory.Build.props`, Yak manifest, installer script, `Comma.License` assembly info, IFC application version fallbacks).

---

## [3.4.9] - 2026-04-28

### Changed
- Version bump to 3.4.9 (assembly metadata and IFC export default application version).

---

## [3.4.8] - 2026-04-21

### Changed
- Version bump to 3.4.8 (build metadata, manifest, installer, IFC export defaults).

### Fixed
- **uSmoothPolySrf / uCombineNurbs:** PairSimilar/SplitZone loft closure — inter-pair loft and corrected `CreateStepClosingBreps` wiring so top/bottom step faces are built (previously only side faces in some cases).
- **xBIM import:** Detected north rotation is no longer applied on top of instance transforms that already express world coordinates (avoids double-rotation).

---

## [2.4.7] - 2026-04-07

### Changed
- Version bump 2.4.5 -> 2.4.7 (build metadata, manifest, installer, exporter defaults).
- **uIfcExport:** Simplified meshing presets to 2 modes: `Fast and Render Mesh` and `Smooth and Slower`.

### Fixed
- **uIfcExport:** Prioritize `GetMeshes(Render)` cache before analytical remeshing for faster exports and lighter IFC output in typical Rhino workflows.
- **uIfcExport:** Non-render mode (`Smooth`) now skips failed objects instead of falling back to render remeshing that can inflate file size unexpectedly.

---

## [2.4.5] - 2026-04-07

### Changed
- Version bump 2.4.4 -> 2.4.5 (build metadata, manifest, installer, export fallback tags).

### Fixed
- **uIfcExport:** Document offsets are consistently interpreted as meters in export math (no unintended 1000x scaling by Rhino model units).
- **uIfcExport:** Added explicit fallback reporting with object IDs when Brep meshing falls back to Render Mesh.
- **uIfcExport (IfcOpenShell writer):** Per-item export errors now skip only the failing item/definition/instance and continue writing IFC for remaining valid data.

---

## [2.4.4] - 2026-04-07

### Changed
- Version bump 2.4.3 -> 2.4.4 (build metadata, manifest, installer, export fallback tags).

### Fixed
- **uIfcImport (xBIM):** Updated model-base detection to digits-first heuristic (order-of-magnitude matching, with ratio fallback) to avoid double-shift on infra files where coordinates are already in real/world range.

---

## [2.4.3] - 2026-04-03

### Changed
- Version bump 2.4.2 → 2.4.3 (build, manifest, installer, bundled user guide).

### Fixed
- **uIfcImport (xBIM):** Khi không chọn "Import Abstract/Spatial Elements", không còn import geometry cho IfcProject, IfcSite, IfcBuilding, IfcSpace, IfcOpeningElement (đồng bộ với IfcOpenShell).

---

## [Unreleased]

### Changed (breaking)
- **IFC command names** aligned with other `uIfc*` commands: **`uExportIfc` → `uIfcExport`**, **`uImportIfc` → `uIfcImport`**. Update scripts, toolbar buttons, and `RunScript` aliases.
- **CAD / DWG batch command names** aligned with the `uDwg*` family: **`uImportCad` → `uDwgImport`**, **`uExportDwgPlus` → `uDwgExport`**. Update scripts, toolbar buttons, and aliases.

---

## [2.3] - 2026-03-11

### Changed
- **uImportIfc:** Version bump 2.2 → 2.3. Import IFC: xử lý hình học đa luồng (Phase 1 parallel, Phase 2 sequential), stream parsing JSON tránh OutOfMemory với file lớn, dọn bộ nhớ trung gian sau import, logic tọa độ Python dùng `verts_local` (trừ offset khi serialize). Mesh: CullDegenerateFaces, UnifyNormals, SolidOrientation/Flip, material cache.

---

## [1.1.3.0] - 2026-02-25

### Added
- **Comma Layer Mapping** (bộ độc lập với ULayer): config riêng `CommaLayerMapping.json`, panel "Comma Layer Mapping", lệnh `uLayerMapping` (mở panel) và `uLayerMappingApply` (áp dụng mapping theo màu lên selection). Dialog Setup: thêm/xóa/sửa dòng mapping màu → tên layer, Import/Export JSON.

### Changed
- Version bump 1.1.2.3 → 1.1.3.0.

---

## [1.1.2.2] - 2026-02-04

### Changed
- Version bump 1.1.2.1 → 1.1.2.2.

---

## [1.1.2.1] - 2026-02-04

### Changed
- Version bump 1.1.2.0 → 1.1.2.1.

---

## [1.1.2.0] - 2026-02-04

### Changed
- Version bump 1.1.1.3 → 1.1.2.0 (docs, installer, manifest).

---

## [1.1.1.3] - 2026-02-04

### Added - IFC Shared Parameters
- **uIfcSetupTemplateFile:** Built-in shared parameters (37 keys) integrated into the command; no CSV file or dialog. Keys are written to Document User Strings with prefix **IFC.SharedParam.*** so they appear in Document User Text (empty values use a placeholder so Rhino shows the keys). Main IFC params are written first, then shared params (so shared params appear at the bottom of the Document User Text table).
- **uIfcApplySharedParams:** Applies shared params to selected objects using **doc.Objects.ModifyAttributes** (duplicate attributes, set user strings, then modify) so changes persist. Empty default values are stored as a single space on the object (like uAttribute) so Rhino persists the keys; existing keys are not overwritten.
- **uExportIfc:** When building object Properties from user text, values that are a single space or zero-width character (placeholders for “empty”) are normalized back to empty string for IFC export.

### Changed - IFC
- **uIfcSetupTemplateFile:** No longer prompts for or links to a CSV file; all shared parameter definitions are embedded in the command. Removed Pset.csv copy from build output.
- **CommaMenu:** uIfcSetupTemplateFile tooltip updated (no “select CSV”; “built-in shared params”).

### Fixed - IFC
- **Document User Text:** Shared param keys (IFC.SharedParam.*) now appear in Document User Text panel (non-empty placeholder used so Rhino displays them).
- **Object User Text:** Shared params applied by uIfcApplySharedParams now persist on objects (ModifyAttributes + non-empty value for empty default).

---

## [1.1.1.2] - 2026-02-04

### Changed
- **uSection:** Tối ưu tốc độ cut (BrepPlane thay BrepBrep, cache IsWorksessionOrXref, trim curve đúng rectangle, dedupe luôn chạy).
- **uSection:** Bỏ bước pick hướng nhìn; mặc định CPlane mặt cắt = line 1–2 (X) và Z view (Y).
- **uSection:** Option Project/Plane (khi pick cut 1–2): chiếu p1–p2 xuống World/CPlane để line cắt luôn nằm trên mặt phẳng.
- **uSection:** Enter tại placement = đặt section ngay tại vết cắt (không orient).
- **uSection:** GroupOutput=Yes luôn tạo group Section_Result (không cần input cùng layer).
- **uSection:** Tránh double result (dedupe ObjectId, nested block, curve trùng hình học).

### Fixed
- **uSection:** Trim curve từ BrepPlane theo đúng hình chữ nhật cắt (không kéo dài ra ngoài vùng cắt).

---

## [1.1.1.1] - 2026-01-28

### Changed
- **uLoftPro:** Luôn gán mặt phẳng ở đầu và cuối alignment (GetDivideParamsWithEnd) để loft/sweep không thiếu đoạn cuối.
- **u3dSlope:** Hiển thị dấu **-** khi điểm 1 cao hơn điểm 2, **+** khi điểm 2 cao hơn điểm 1 (chế độ Percent); chế độ Ratio giữ nguyên không dấu.

---

## [1.1.0.0] - 2026-01-27

### Major Release - IFC Import/Export Overhaul

### Added - IFC Import
- **Material Support:** Automatic Rhino Material creation from IFC materials (IfcMaterial, IfcMaterialLayerSet, IfcMaterialConstituentSet)
- **Color Extraction:** Multiple fallback strategies for color (shape.styles → IfcStyledItem → geometry.materials)
- **Property Set Prefixing:** All properties now use `Group.Parameter` format (e.g., `Pset_WallCommon.IsExternal`)
- **IfcMapConversion Support:** Read georeferencing from IFC files for precise coordinate restoration
- **Mesh Unweld:** Automatic sharp edge detection (45° crease angle) to fix shading artifacts
- **Smart Name Processing:** Remove numeric IDs from object names to merge similar objects (e.g., `Wall:123` → `Wall`)
- **Import Statistics:** Detailed reporting (success/skipped/error counts, offset info)

### Added - IFC Export
- **RenderMesh Extraction:** Fast export using pre-cached render meshes (respects user display settings)
- **Material Export:** Create IfcMaterial + IfcRelAssociatesMaterial from Rhino materials
- **Color Export:** Create IfcSurfaceStyle + IfcStyledItem with proper IfcColourRgb
- **Property Set Grouping:** Automatic grouping by prefix (Pset_WallCommon.*, Dimensions.*) → Multiple IfcPropertySets
- **Auto IfcType from Layer:** Fallback to Layer Level 5 if User Text not set
- **Manual Offset Support:** Handle large coordinates (IFC.Offset.X/Y/Z) for precision
- **Georeferencing:** Full IfcMapConversion support (Eastings, Northings, OrthogonalHeight, rotation)
- **Storey Elevation:** Auto-calculate or manual override
- **1-based Indexing:** Proper IFC4 geometry indexing (converted from Rhino 0-based)
- **Thin Mesh Handling:** Special processing for thin geometry to prevent precision loss
- **Spatial Hierarchy Fallback:** Auto-extract Project/Site/Building from layer structure
- **Export Statistics:** Detailed reporting (exported/failed counts)

### Added - UI
- **CommaMenu Title:** Added "Comma Menu" title with logo icon at top
- **Icon Support:** CommaRhLogo.ico integrated across all dialogs and panels
- **About Menu:** Link to Notion user manual
- **QuickTools Color:** Changed to #F97316 (orange) with bold-on-hover effect

### Changed - Commands
- **Command Names:** All commands now use camelCase (uAttribute, uDwgExport, etc.)
- **IFC Group Separation:** uImportIfc, uExportIfc, uIfcInstall moved to dedicated "Ifc" menu group
- **Menu Organization:** Merged "To Layer" and "Layer Visibility" into main "Layers" group with separators
- **CPlane Menu:** Renamed from "CPlane & Construction" to "CPlane"

### Fixed - IFC
- **JSON Serialization:** Convert colour objects to lists before JSON export
- **Geometry Precision:** Objects far from origin no longer lose precision or deform
- **Vertex Sharing:** Proper topology for IFC export (CombineIdentical for normal meshes)
- **Invalid Mesh Repair:** Automatic FillHoles() for broken meshes
- **Extrusion Support:** Automatic conversion to meshable geometry

### Fixed - General
- **Ambiguous References:** Resolved Eto.Drawing.Image vs System.Drawing.Image conflicts
- **Icon Loading:** Fixed embedded resource paths for CommaRhLogo.ico
- **QuickTools Double Execution:** Reverted to Idle event handler to prevent command doubling
- **Registry Cleanup:** Installer now cleans old registry entries before installation

### Documentation
- **IFC Export Guide:** Complete workflow for IFC4-compliant export with IfcOpenShell
- **Georeferencing Guide:** Step-by-step for IfcMapConversion setup
- **Offset Workflow:** Manual offset procedure for large-coordinate models
- **Property Set Standards:** BuildingSMART-compliant naming conventions

---

## [1.0.3.2] - 2026-01-24

### Changed
- Updated embedded icon/logo loading to avoid source-path dependencies in release
- Updated version numbers across manifests and documentation

### Fixed
- Prevented runtime icon loading from resolving to development/source paths

---

## [1.0.2.9] - 2026-01-23

### Changed
- Updated build scripts with improved path handling
- Fixed UploadCommaRH.bat label error
- Synchronized all documentation versions

### Fixed
- Build script now works from any directory
- Upload script properly finds latest .yak file

---

## [1.0.2.8] - 2026-01-23

### Added
- Centralized build system with Directory.Build.props and Directory.Packages.props
- Improved project structure with src/, build/, docs/, tests/ folders
- Enhanced build scripts for better automation
- Updated documentation for better maintainability

### Changed
- Migrated Comma.License to SDK-style project format
- Centralized package version management
- Improved build configuration and dependency management
- Updated project paths in build scripts

### Fixed
- Build script paths for new project structure
- Obfuscation configuration paths
- Documentation links and references

---

## [1.0.2.7] - 2026-01-20

### Added
- Smart CPlane tools (UCPLANE command)
- Enhanced construction plane creation from curves, surfaces, and meshes
- Scope Box creation for clipping planes
- Planarity checking tools

### Changed
- Improved CPlane user interface
- Enhanced selection feedback
- Better error handling in geometry operations

---

## [1.0.2.6] - 2026-01-15

### Added
- Advanced layer management tools
- Color-coded layer panel
- Layer visibility controls
- Batch layer operations

### Changed
- Improved layer performance
- Enhanced layer filtering
- Better layer state management

---

## [1.0.2.5] - 2026-01-10

### Added
- Enhanced IFC import/export functionality
- BIM data management tools
- Attribute management system
- Multi-sheet license support

### Changed
- Improved IFC compatibility
- Better BIM data handling
- Enhanced attribute editing

---

## [1.0.2.4] - 2026-01-05

### Added
- Measurement tools for area and volume
- Dimension calculation tools
- Enhanced geometry analysis
- Quick measurement commands

### Fixed
- Measurement accuracy issues
- Dimension display problems
- Geometry calculation errors

---

## [1.0.2.3] - 2025-12-28

### Added
- Curve editing tools
- Surface modification commands
- Mesh cleanup utilities
- Geometry optimization tools

### Changed
- Improved curve manipulation
- Enhanced surface editing
- Better mesh processing

---

## [1.0.2.2] - 2025-12-20

### Added
- AutoCAD DWG import/export enhancements
- Improved file compatibility
- Better layer mapping
- Enhanced unit conversion

### Fixed
- DWG import issues
- Layer mapping problems
- Unit conversion errors

---

## [1.0.2.1] - 2025-12-15

### Added
- License management system
- Free vs Pro feature differentiation
- Google Sheets integration for licensing
- Hardware-based license verification

### Fixed
- License activation issues
- Feature unlock problems
- License validation errors

---

## [1.0.2.0] - 2025-12-10

### Added
- Initial release of CommaRh plugin
- Basic Rhino integration
- Core command structure
- Foundation architecture

### Changed
- Complete rewrite from legacy plugin system
- Modern .NET Framework 4.8 implementation
- Enhanced Rhino 8 compatibility

---

## [1.0.1.x] - Legacy Versions

### Previous Features
- Basic Rhino plugin functionality
- Legacy command system
- Deprecated architecture

---

## Migration Notes

### From 1.0.2.7 to 1.0.2.8
- No breaking changes
- Build system improvements only
- All existing functionality preserved

### From 1.0.2.x to 1.0.2.8
- All user-facing features remain the same
- Internal architecture improvements
- Better maintainability and performance

---

## Support

For questions about specific versions or migration issues:
- Email: Comma3D.AEC@gmail.com
- Documentation: See [docs/](docs/) folder
- Issues: Report via GitHub Issues

---

*Last updated: January 23, 2026*
