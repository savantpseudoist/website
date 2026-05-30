import os
import subprocess
import sys


def venv_python(venv_dir: str) -> str:
    if os.name == "nt":
        return os.path.join(venv_dir, "Scripts", "python.exe")
    return os.path.join(venv_dir, "bin", "python")


def main() -> int:
    venv_dir = ".venv"
    python_exe = venv_python(venv_dir)

    if not os.path.exists(python_exe):
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

    subprocess.check_call([python_exe, "-m", "pip", "install", "-r", "requirements.txt"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
