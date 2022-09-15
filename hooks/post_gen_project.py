import os

deps = {
    "format": ["black", "isort"],
    "dev": ["tox"],
    "type_check": ["mypy", "types-all"],
    "test": ["pytest", "pytest-mock", "pytest-cov", "toml"],
    "docs": ["sphinx", "sphinx-autorun", "sphinx-rtd-theme"],
    "lint": ["pylint", "pytest"],
}

for k in deps:
    deps_str = ""
    for d in deps[k]:
        deps_str += f" {d}"
    os.system(f"poetry add {deps_str} --group {k}")

os.system("poetry lock")
