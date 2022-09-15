# -*- coding: utf-8 -*-
"""Basic tests on the package."""
import toml

from {{ cookiecutter.project_slug }} import __version__


def get_version() -> str:
    """
    Gets version of the package from the ``pyproject.toml`` file.

    Returns
    --------
        Pacakge version.
    """
    pyproject_file = "pyproject.toml"

    return str(toml.load(pyproject_file)["tool"]["poetry"]["version"])


def test_version():
    """
    Checks that package version matches ``__version__`` in ``__init__.py``.

    This test must be run from the root of the repository.
    """
    assert __version__ == get_version()
    # Eq.: assert __version__ == "0.1.0"
