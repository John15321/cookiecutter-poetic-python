# cookiecutter-poetic-python

A `Cookiecutter` project template that uses Poetry to manage Python Projects

## Getting started

*WARNING* This template requires Poetry equal `1.2.0` or newer due to the use of dependency groups, and Python at least `3.8`.

Install `cookiecutter`:

```bash
pip install cookiecutter
```

Use the template:

```bash
cookiecutter https://github.com/John15321/cookiecutter-poetic-python
```

Fill out the questions asked by the `cookiecutter` and wait for the project to be created. It dynamically adds and checks dependencies that will be by default added to the project, therefore recomputing the whole dependency graph will take some time, but it will be done only once.

## What this template does

* Sets up sphinx documentation
* Sets up tox configuration
* Sets up basic CI/CD configuration for GitHub that checks:
  * Linting with `pylint`
  * Formatting with `black` and `isort`
  * Building documentation
  * Building the source and built distribution
  * Running tests
* Package structure with the newest and best `pyproject.toml` guidelines
* Dependencies for testing, formatting, linting etc. separated in the `pyproject.toml` file for ease of use and optimization

`Poetry` has very good and extensive documentation so go ahead and read it:

* <https://python-poetry.org/>
