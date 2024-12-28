#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time

import sphinx_bootstrap_theme

import yasa

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath("sphinxext"))
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_copybutton",
    "sphinx_panels",
    "numpydoc",
]

# Generate the API documentation when building
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "member-order": "groupwise",
    "undoc-members": False,
    # 'special-members': '__init__',
    # 'exclude-members': '__weakref__'
}

# configure sphinx-copybutton
# https://github.com/executablebooks/sphinx-copybutton
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

numpydoc_show_class_members = False

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "yasa"
author = "Raphael Vallat"
copyright = "2018-{}, Dr. Raphael Vallat, Center for Human Sleep Science, UC Berkeley".format(
    time.strftime("%Y")
)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# The full version, including alpha/beta/rc tags.
sys.path.insert(0, os.path.abspath(os.path.pardir))
version = yasa.__version__
release = yasa.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# Bootstrap theme
html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    "source_link_position": "footer",
    # 'navbar_title': ' ',  # we replace this with an image
    "bootswatch_theme": "flatly",
    "navbar_sidebarrel": False,
    # 'nosidebar': True,
    # 'navbar_site_name': "",
    "navbar_pagenav": False,
    "bootstrap_version": "3",
    "navbar_class": "navbar",
    "navbar_links": [
        ("API", "api"),
        ("Quickstart", "quickstart"),
        ("FAQ", "faq"),
        ("What's new", "changelog"),
        ("Contribute", "contributing"),
    ],
}

html_logo = "pictures/yasa_128x128.png"
html_favicon = "pictures/favicon.ico"

# -- Options for HTML output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "yasadoc"
html_show_sourcelink = False

# -- Intersphinx ------------------------------------------------

intersphinx_mapping = {
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
    "scipy": ("http://docs.scipy.org/doc/scipy/reference/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "mne": ("https://martinos.org/mne/stable/", None),
    "seaborn": ("https://seaborn.pydata.org/", None),
    "pyriemann": ("https://pyriemann.readthedocs.io/en/latest/", None),
    "tensorpac": ("https://etiennecmb.github.io/tensorpac/", None),
}
