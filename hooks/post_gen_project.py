import os

deps = {
    "format": ["black", "isort"],
    "dev": ["tox"],
    "type_check": ["mypy"],
    "test": ["pytest", "pytest-mock", "pytest-cov", "toml"],
    "lint": ["pylint", "pytest"],
}

print(
    "Adding newest versions of dependencies to the project (this may take a while)..."
)

for k in deps:
    deps_str = ""
    for d in deps[k]:
        deps_str += f" {d}"
    os.system(f"poetry add {deps_str} --group {k}")

print("Done adding dependencies. Calculating the lock...")

os.system("poetry lock")

print("Done")
