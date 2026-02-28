from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx

from sphinx_icalendar._lexer import ICalendarLexer, JCalLexer
from sphinx_icalendar._nodes import calendar_block
from sphinx_icalendar._transform import CalendarTransform
from sphinx_icalendar._visitors import (
    depart_calendar_html,
    depart_calendar_unsupported,
    visit_calendar_html,
    visit_calendar_unsupported,
)
from sphinx_icalendar.version import __version__


def get_lexers() -> dict[str, type]:
    return {
        "icalendar": ICalendarLexer,
        "ics": ICalendarLexer,
        "jcal": JCalLexer,
        "jcalendar": JCalLexer,
    }


def setup(app: Sphinx) -> dict[str, Any]:
    app.setup_extension("sphinx_design")
    for name, lexer in get_lexers().items():
        app.add_lexer(name, lexer)
    app.add_node(
        calendar_block,
        html=(visit_calendar_html, depart_calendar_html),
        latex=(visit_calendar_unsupported, depart_calendar_unsupported),
        text=(visit_calendar_unsupported, depart_calendar_unsupported),
        man=(visit_calendar_unsupported, depart_calendar_unsupported),
    )
    app.add_transform(CalendarTransform)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
