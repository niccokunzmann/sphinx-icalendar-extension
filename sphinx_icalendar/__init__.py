"""
sphinx_icalendar
~~~~~~~~~~~~~~~~

Renders ``.. code-block:: calendar`` directives as HTML calendar tables.

Usage in a .rst file::

    .. code-block:: calendar

        BEGIN:VCALENDAR
        BEGIN:VEVENT
        DTSTART:20260301T090000Z
        DTEND:20260301T100000Z
        SUMMARY:Team standup
        END:VEVENT
        END:VCALENDAR
"""

from __future__ import annotations

import html
from datetime import date, datetime

from docutils import nodes
from docutils.parsers.rst import directives
from icalendar import Calendar
from sphinx.transforms import SphinxTransform


# ---------------------------------------------------------------------------
# Custom node
# ---------------------------------------------------------------------------

class calendar_block(nodes.General, nodes.Element):
    """Holds the raw iCalendar source; replaced by visitors during writing."""


# ---------------------------------------------------------------------------
# Transform: literal_block[language=calendar] → calendar_block
# ---------------------------------------------------------------------------

class CalendarTransform(SphinxTransform):
    """Run after the document is read; intercepts code-block:: calendar."""

    default_priority = 400  # before most other transforms

    def apply(self) -> None:
        for node in self.document.traverse(nodes.literal_block):
            if node.get("language") != "calendar":
                continue
            source = node.astext()
            new_node = calendar_block(ical_source=source)
            new_node.source = node.source
            new_node.line = node.line
            node.replace_self(new_node)


# ---------------------------------------------------------------------------
# HTML visitor
# ---------------------------------------------------------------------------

def _fmt_dt(value: date | datetime | None) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M")
    return value.strftime("%Y-%m-%d")


def visit_calendar_html(self, node: calendar_block) -> None:
    source = node["ical_source"]
    try:
        cal = Calendar.from_ical(source)
    except Exception as exc:
        self.body.append(
            f'<div class="calendar-error">Failed to parse calendar: {html.escape(str(exc))}</div>'
        )
        raise nodes.SkipNode from exc

    rows: list[tuple[str, str, str, str]] = []
    for component in cal.walk():
        if component.name != "VEVENT":
            continue
        summary = str(component.get("SUMMARY", "(no title)"))
        dtstart = component.get("DTSTART")
        dtend = component.get("DTEND")
        location = str(component.get("LOCATION", ""))
        rows.append((
            html.escape(summary),
            html.escape(_fmt_dt(dtstart.dt if dtstart else None)),
            html.escape(_fmt_dt(dtend.dt if dtend else None)),
            html.escape(location),
        ))

    self.body.append('<div class="calendar-block">')
    if not rows:
        self.body.append("<p><em>No events found.</em></p>")
    else:
        self.body.append(
            '<table class="calendar-table">'
            "<thead><tr>"
            "<th>Summary</th><th>Start</th><th>End</th><th>Location</th>"
            "</tr></thead>"
            "<tbody>"
        )
        for summary, start, end, location in rows:
            self.body.append(
                f"<tr><td>{summary}</td><td>{start}</td><td>{end}</td><td>{location}</td></tr>"
            )
        self.body.append("</tbody></table>")
    self.body.append("</div>")
    raise nodes.SkipNode


def depart_calendar_html(self, node: calendar_block) -> None:
    pass  # SkipNode is raised in visit, so this is never called


# ---------------------------------------------------------------------------
# Unsupported builder fallback (LaTeX, text, …)
# ---------------------------------------------------------------------------

def visit_calendar_unsupported(self, node: calendar_block) -> None:
    self.visit_literal_block(
        nodes.literal_block(node["ical_source"], node["ical_source"])
    )
    raise nodes.SkipNode


def depart_calendar_unsupported(self, node: calendar_block) -> None:
    pass


# ---------------------------------------------------------------------------
# Sphinx setup
# ---------------------------------------------------------------------------

def setup(app):
    app.add_node(
        calendar_block,
        html=(visit_calendar_html, depart_calendar_html),
        latex=(visit_calendar_unsupported, depart_calendar_unsupported),
        text=(visit_calendar_unsupported, depart_calendar_unsupported),
        man=(visit_calendar_unsupported, depart_calendar_unsupported),
    )
    app.add_transform(CalendarTransform)

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
