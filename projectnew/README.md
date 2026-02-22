# Coffee Shop Demo

This repository contains a small interactive `coffee.py` script and unit tests.

CI
- A GitHub Actions workflow is included at `.github/workflows/ci.yml` that runs the tests on push and pull requests for Python 3.10 and 3.11.

Run tests locally

```bash
python3 -m unittest discover -v tests
```

Commit and push

```bash
git add .
git commit -m "Add CI workflow and README"
git push origin main
```

Notes
- If your default branch is `master`, the workflow also triggers on `master` pushes.
- If you want CI to run on other python versions or add linting, I can update the workflow.
