import sphinx_icalendar

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
