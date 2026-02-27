import os
import sys
import sphinx_icalendar

# Make the extension importable without installing it first
sys.path.insert(0, os.path.abspath(".."))

project = "sphinx-icalendar"
author = "sphinx-icalendar contributors"
release = sphinx_icalendar.__version__

extensions = [
    "sphinx_icalendar",
]

html_theme = "alabaster"

html_theme_options = {
    "description": "Render iCalendar events directly in your Sphinx docs.",
    "github_user": "niccokunzmann",
    "github_repo": "sphinx-icalendar-extension",
}
