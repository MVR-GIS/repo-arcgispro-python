from __future__ import annotations

import platform
import sys


def main() -> int:
    print("== ArcGIS Pro Python / arcpy smoke test ==")
    print(f"Python executable: {sys.executable}")
    print(f"Python version:    {sys.version.split()[0]}")
    print(f"Platform:          {platform.platform()}")

    try:
        import arcpy  # type: ignore
    except Exception as e:
        print("\nFAILED: Could not import arcpy.")
        print("Most common causes:")
        print("- You did not activate the per-repo env: conda activate .conda-arcgis")
        print("- VS Code terminal did not initialize ESRI proenv.bat (conda not set up)")
        print("- ArcGIS Pro is not installed correctly")
        print("\nError:")
        print(repr(e))
        return 1

    print("\nImported arcpy successfully.")
    print(f"arcpy.__version__:  {getattr(arcpy, '__version__', 'UNKNOWN')}")

    # Keep this short; we want a fast, readable signal.
    try:
        info = arcpy.GetInstallInfo()
        keys = ["ProductName", "Version", "BuildNumber", "InstallDir"]
        print("\nArcGIS install info (subset):")
        for k in keys:
            if k in info:
                print(f"- {k}: {info[k]}")
    except Exception as e:
        # Non-fatal: arcpy import succeeded, so we still consider environment basically OK.
        print("\nWARNING: arcpy.GetInstallInfo() failed (non-fatal).")
        print(repr(e))

    print("\nPASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
