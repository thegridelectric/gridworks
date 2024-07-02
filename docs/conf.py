"""Sphinx configuration."""

project = "Gridworks"
author = "GridWorks"
copyright = "2022, GridWorks"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
