from __future__ import annotations

from datetime import date, datetime

from docutils import nodes
from icalendar import Calendar
from icalendar.timezone import tzid_from_dt

from sphinx_icalendar._nodes import calendar_block

import recurring_ical_events


def _fmt_dt(value: date | datetime | None) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        s = value.strftime("%Y-%m-%d %H:%M")
        if datetime.tzinfo is not None:
            tz = tzid_from_dt(value)
            if tz is not None:
                s += f" {tz}"
        return s
    return value.strftime("%Y-%m-%d")


def visit_calendar_html(self, node: calendar_block) -> None:
    source = node["ical_source"]
    cal = Calendar.from_ical(source)  # TODO use icalendar.parse

    body = []

    for occurrence in recurring_ical_events.of(cal).all():
        summary = occurrence.summary
        start = occurrence.start
        end = occurrence.end
        body.append(
            f"<tr><td>{summary}</td><td>{_fmt_dt(start)}</td><td>{_fmt_dt(end)}</td></tr>"
        )

    self.body.append('<div class="calendar-block">')
    if not body:
        self.body.append("<p><em>No events found.</em></p>")
    else:
        self.body.append(
            '<table class="calendar-table">'
            "<thead><tr>"
            "<th>Summary</th><th>Start</th><th>End</th>"
            "</tr></thead>"
            "<tbody>"
        )
        self.body.extend(body)
        self.body.append("</tbody></table>")
    self.body.append("</div>")
    raise nodes.SkipNode


def depart_calendar_html(self, node: calendar_block) -> None:
    pass  # SkipNode is raised in visit, so this is never called


def visit_calendar_unsupported(self, node: calendar_block) -> None:
    self.visit_literal_block(
        nodes.literal_block(node["ical_source"], node["ical_source"])
    )
    raise nodes.SkipNode


def depart_calendar_unsupported(self, node: calendar_block) -> None:
    pass
