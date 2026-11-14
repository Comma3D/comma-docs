---
title: Contribute to the guide
weight: 6
---

The guide source lives in the public repository [Comma3D/comma-docs](https://github.com/Comma3D/comma-docs). Plugin source stays private.

1. Clone `https://github.com/Comma3D/comma-docs.git`.
2. Edit markdown under `content/` (Rhino pages are under `content/rhino/docs/`).
3. Commit on a branch and open a pull request into `main`, or push to `main` if you are a collaborator.
4. The **Deploy Pages** workflow builds Hugo and publishes https://comma3d.github.io/comma-docs/.

Local check (optional):

```powershell
git clone --depth 1 --branch v0.13.0 https://github.com/imfing/hextra.git themes/hextra
hugo server
```

Do not commit `public/`, `themes/`, or `.tools/`.
