# -*- coding: utf-8 -*-
"""Basic tests on the package."""

import os
from pathlib import Path

import toml

from {{ cookiecutter.project_slug }} import __version__

def get_version() -> str:
    """Get version of the package from the ``pyproject.toml`` file.

    Returns:
        Pcakge version.
    """
    Path(os.path.dirname(__file__))
    root_project_directory = "../"

    pyproject_file: Path = root_project_directory + "pyproject.toml"

    return str(toml.load(pyproject_file)["tool"]["poetry"]["version"])

def test_version():
    """Checks that package version matches ``__version__`` in ``__init__.py``."""
    assert __version__ == get_version()
