# env/

This folder stores environment metadata to improve reproducibility and reviewability for ArcGIS Pro Python projects.

Generate/update metadata (recommended):

    python env/capture_env_metadata.py

To also write a (often large) pip package list:

    python env/capture_env_metadata.py --pip-freeze

Notes:
- Run these commands after activating the project environment:

    conda activate .conda-arcgis

- `conda` commands will work best when your VS Code terminal is initialized via ESRI `proenv.bat`.
