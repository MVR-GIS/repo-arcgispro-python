from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_cmd(cmd: list[str]) -> tuple[int, str]:
    """
    Run a command and capture stdout+stderr as text.
    Returns (returncode, combined_output).
    """
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=False,
    )
    return proc.returncode, proc.stdout


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Capture lightweight environment metadata for ArcGIS Pro Python repos."
    )
    parser.add_argument(
        "--pip-freeze",
        action="store_true",
        help="Also write env/pip_freeze.txt (often large).",
    )
    args = parser.parse_args()

    out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().isoformat(timespec="seconds")

    # Basic Python facts (always)
    write_text(out_dir / "timestamp.txt", f"{timestamp}\n")
    write_text(out_dir / "python_executable.txt", f"{sys.executable}\n")
    write_text(out_dir / "python_version.txt", f"{sys.version}\n")

    # arcpy version (best effort)
    try:
        import arcpy  # type: ignore

        write_text(
            out_dir / "arcpy_version.txt",
            f"{getattr(arcpy, '__version__', 'UNKNOWN')}\n",
        )
    except Exception as e:
        write_text(
            out_dir / "arcpy_version.txt",
            "FAILED to import arcpy. Activate .conda-arcgis and try again.\n"
            f"Error: {repr(e)}\n",
        )

    # Conda metadata (best effort)
    # These will only work if the shell session was initialized via proenv.bat.
    conda_cmds: list[tuple[str, list[str]]] = [
        ("conda_version.txt", ["conda", "--version"]),
        ("conda_info.txt", ["conda", "info"]),
        ("conda_env_list.txt", ["conda", "env", "list"]),
    ]

    for filename, cmd in conda_cmds:
        rc, out = run_cmd(cmd)
        header = f"Command: {' '.join(cmd)}\nReturn code: {rc}\n\n"
        write_text(out_dir / filename, header + out)

    # pip freeze is optional and flag-gated
    if args.pip_freeze:
        rc, out = run_cmd([sys.executable, "-m", "pip", "freeze"])
        header = (
            f"Command: {sys.executable} -m pip freeze\n"
            f"Return code: {rc}\n\n"
        )
        write_text(out_dir / "pip_freeze.txt", header + out)

    # Friendly summary
    wrote = [
        "timestamp.txt",
        "python_executable.txt",
        "python_version.txt",
        "arcpy_version.txt",
        "conda_version.txt",
        "conda_info.txt",
        "conda_env_list.txt",
    ]
    if args.pip_freeze:
        wrote.append("pip_freeze.txt")

    summary = "Wrote:\n" + "\n".join([f"- env/{f}" for f in wrote]) + "\n"
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
