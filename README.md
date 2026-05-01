# ArcGIS Pro Python Repo Template (VS Code + arcpy)

This repository is a **template** for geospatial Python projects that use **ArcGIS Pro 3.x** (commonly 3.4+ in practice) and **`arcpy`**.

It is designed to get analysts productive quickly with minimal setup:

- VS Code is the IDE (including Git via the VS Code Source Control panel)
- The integrated terminal is configured to initialize ESRI’s Python tooling via `proenv.bat`
- You create a per-repo cloned environment named `.conda-arcgis` from ESRI’s `arcgispro-py3`
- A smoke test verifies `arcpy` is working

Authoritative ESRI guidance:
- https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/installing-python-for-arcgis-pro.htm

## Requirements

- Windows + ArcGIS Pro 3.x installed
- VS Code installed using your organization’s approved workflow
- Git installed using your organization’s approved workflow

## Quickstart (10 minutes)

### 1) Create your project repo from this template

In GitHub:
- Click **Use this template**
- Create a new repository in your approved org/location

### 2) Clone using VS Code (no CLI required)

In VS Code:
- Source Control → **Clone Repository**
- Paste your new repo URL
- Open the cloned repo

### 3) Create the per-repo environment (one-time)

Open **ArcGIS Pro Python Command Prompt** (Start Menu), then run:

    conda create --name .conda-arcgis --clone arcgispro-py3

### 4) Open the ESRI-configured terminal in VS Code

This repo includes a VS Code terminal profile that runs:

- `C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\proenv.bat`

In VS Code:
- Terminal → New Terminal

Activate the project environment:

    conda activate .conda-arcgis

### 5) Run the smoke test

    python scripts/smoke_test_arcpy.py

If this passes, you are ready to work.

## Select the correct Python interpreter in VS Code (required)

Even if the terminal is correct, VS Code still needs the correct interpreter for:
- IntelliSense
- Running scripts via the Python extension
- Jupyter notebooks

Steps:
1. Ctrl+Shift+P → **Python: Select Interpreter**
2. Choose the interpreter for the conda env named: `.conda-arcgis`
3. If you don’t see it:
   - restart VS Code
   - ensure `.conda-arcgis` exists: `conda env list`

Verify (in VS Code terminal):

    python -c "import sys; print(sys.executable)"
    python -c "import arcpy; print(arcpy.__version__)"

## Notebook start (recommended)

Open:
- `notebooks/00_getting_started.ipynb`

When prompted to select a kernel:
- choose `.conda-arcgis`

## Project structure

- `notebooks/` — exploratory analysis + narrative
- `scripts/` — runnable workflows / entry points
- `src/` — reusable functions/modules
- `data/` — project data (use judgment; avoid huge files)
- `outputs/` — generated outputs (ignored by default)
- `env/` — environment metadata capture

## Capture environment metadata (recommended)

Basic metadata (small):

    python env/capture_env_metadata.py

Also write a pip package list (often large):

    python env/capture_env_metadata.py --pip-freeze

## Troubleshooting

- If `conda` is not found in VS Code terminal:
  - open a new terminal (it should use the “ArcGIS Pro Python …” profile)
  - restart VS Code

- If `arcpy` fails to import:
  - `conda activate .conda-arcgis`
  - re-run smoke test

## What to commit (simple rule)

- Commit code, notebooks, and documentation.
- Avoid committing huge data and bulky generated outputs.
