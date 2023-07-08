import os
from sys import path

import sphinx_rtd_theme


def setup(app):
    """Forces the auto generation of the documentation at build time."""
    path.insert(0, os.path.abspath("."))
    os.system('sphinx-apidoc src -f -e -M -H "Module Reference" -o docs/autogen')


# ------------------------------------------------------------------------------
# General information about the project.
# ------------------------------------------------------------------------------

project = "{{ cookiecutter.project_full_name }}"
copyright = "{{ cookiecutter.open_source_license }}"

# ------------------------------------------------------------------------------
# General Configuration
# ------------------------------------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "4"

# Add any Sphinx extension module names here, as strings. They can
# be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# See http://www.sphinx-doc.org/en/stable/extensions.html
extensions = [
    "sphinx_autorun",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.graphviz",
]

# -----------------------------------------------------------------------------
# sphinx.ext.intersphinx
# -----------------------------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://doc.python.org/3/", None),
}

# -----------------------------------------------------------------------------
# sphinx.ext.autodoc
# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
# -----------------------------------------------------------------------------
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": None,
    "show-inheritance": None,
    "inherited-members": None,
    "undoc-members": None,
}
autoclass_content = "both"
add_module_names = False

# -----------------------------------------------------------------------------
# 'sphinx.ext.inheritance_diagram',
# -----------------------------------------------------------------------------
inheritance_graph_attrs = dict(rankdir="LR", size='""', fontsize=12, ratio="compress")
inheritance_node_attrs = dict(fontsize=12, style="filled")

# -----------------------------------------------------------------------------
# General information about the project.
# -----------------------------------------------------------------------------

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:

today_fmt = "%Y-%m-%dT%H:%M %Z"
source_suffix = ".rst"

# The extlinks extension simplifies referencing multiple links to a given URL,
# for example links to bug trackers, version control web interfaces, etc.
# See http://www.sphinx-doc.org/en/stable/ext/extlinks.html
# extlinks = {
#     "github": (
#         "{{cookiecutter.project_url}}/tree/master/%s",
#         "{{cookiecutter.project_slug}}/",
#     ),
# }

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ["{{cookiecutter.project_slug}}" + "."]

# ----------------------------------------------------------------------------
# Custom Theme Options
# ----------------------------------------------------------------------------
# The frontpage document.
index_doc = "index"
# The master toctree document.
master_doc = "index"
# Manages todo section
todo_include_todos = True
include_todos = True
# warning will be inserted in the final documentation
keep_warnings = False


# -- Options for HTML output --------------------------------------------------

html_theme_options = {
    "canonical_url": "",
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#2980B9",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# sphinxcontrib.napoleon extension configuration
# see https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# for details
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_favicon = os.path.join("_static", "favicon.ico")
html_title = project
html_last_updated_fmt = today_fmt
html_show_sphinx = False
html_show_copyright = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = project + "-doc"
