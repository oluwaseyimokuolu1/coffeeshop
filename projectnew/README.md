# Coffee Shop Demo

This repository contains a small interactive `coffee.py` script and unit tests.

![CI](https://github.com/oluwaseyimokuolu1/getcoins/actions/workflows/ci.yml/badge.svg)

## CI
- A GitHub Actions workflow is included at `.github/workflows/ci.yml` that runs the tests and linting (Black, Flake8) on push and pull requests for Python 3.10 and 3.11.

## Run tests locally

```bash
python3 -m unittest discover -v tests
```

## Run lint/format checks locally

Install dev dependencies and run Black/Flake8:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m black --check .
python3 -m flake8 .
```

## Commit and push

```bash
git add .
git commit -m "Add CI workflow and README"
git push origin main
```

Notes
- If your default branch is `master`, the workflow also triggers on `master` pushes.
