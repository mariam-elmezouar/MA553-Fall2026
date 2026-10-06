"""
MA553 — environment check.

Run this after installing:   python check_setup.py

It checks that Python and the libraries you need are present, and that the
dataset used in Lab 0 loads. It changes nothing on your machine.
"""

import sys

REQUIRED = [
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("sklearn", "scikit-learn"),
    ("matplotlib", "matplotlib"),
    ("pyarrow", "pyarrow"),
]

def main():
    print("MA553 environment check")
    print("-" * 55)

    problems = []

    # 1. Python version
    major, minor = sys.version_info[:2]
    version = f"{major}.{minor}"
    if (major, minor) >= (3, 10):
        print(f"  OK      Python {version}")
    else:
        print(f"  PROBLEM Python {version} is too old (need 3.10 or newer)")
        problems.append("Install Python 3.10 or newer.")

    # 2. Libraries
    for import_name, install_name in REQUIRED:
        try:
            module = __import__(import_name)
            found = getattr(module, "__version__", "unknown version")
            print(f"  OK      {install_name} {found}")
        except ImportError:
            print(f"  PROBLEM {install_name} is not installed")
            problems.append(f"Install it with:  pip install {install_name}")

    # 3. The dataset Lab 0 uses
    try:
        from sklearn.datasets import load_breast_cancer
        data = load_breast_cancer()
        rows, columns = data.data.shape
        print(f"  OK      Lab 0 dataset loads ({rows} rows, {columns} columns)")
    except Exception as error:
        print(f"  PROBLEM the Lab 0 dataset did not load: {error}")
        problems.append("Check that scikit-learn installed correctly.")

    print("-" * 55)

    if problems:
        print("SOME CHECKS FAILED. What to do:")
        for item in problems:
            print(f"  - {item}")
        print("\nIf you are stuck, use the Colab link in lab0/README.md,")
        print("and bring the error message to class.")
        return 1

    print("ALL CHECKS PASSED — you are ready for class.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
