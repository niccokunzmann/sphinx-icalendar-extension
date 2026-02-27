from __future__ import annotations

import hashlib
import html as html_mod
from collections.abc import Sequence
from datetime import date, datetime

from docutils import nodes
from icalendar import Calendar
from icalendar.cal import Component
from icalendar.timezone import tzid_from_dt
from sphinx.util.docutils import SphinxTranslator
from sphinx.writers.html5 import HTML5Translator

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


def _tab_id(source: str) -> str:
    return hashlib.sha256(source.encode()).hexdigest()[:8]


def _render_table(occurrences: Sequence[Component]) -> str:
    if not occurrences:
        return "<p><em>No events found.</em></p>"
    body = "".join(
        f"<tr>"
        f"<td>{html_mod.escape(str(occurrence.summary))}</td>"
        f"<td>{html_mod.escape(_fmt_dt(occurrence.start))}</td>"
        f"<td>{html_mod.escape(_fmt_dt(occurrence.end))}</td>"
        f"</tr>"
        for occurrence in occurrences
    )
    return (
        '<table class="calendar-table">'
        "<thead><tr><th>Summary</th><th>Start</th><th>End</th></tr></thead>"
        f"<tbody>{body}</tbody></table>"
    )


def visit_calendar_html(self: HTML5Translator, node: calendar_block) -> None:
    source = node["ical_source"]
    cal = Calendar.from_ical(source)
    occurrences = recurring_ical_events.of(cal).all()

    tid = _tab_id(source)
    table_html = _render_table(occurrences)
    source_html = html_mod.escape(source)

    self.body.append(
        f'<div class="sd-tab-set">'
        f'<input checked="checked" id="cal-{tid}-input--1" name="cal-{tid}" type="radio">'
        f'<label for="cal-{tid}-input--1">Calendar</label>'
        f'<div class="sd-tab-content docutils">{table_html}</div>'
        f'<input id="cal-{tid}-input--2" name="cal-{tid}" type="radio">'
        f'<label for="cal-{tid}-input--2">Source</label>'
        f'<div class="sd-tab-content docutils"><pre>{source_html}</pre></div>'
        f"</div>"
    )
    raise nodes.SkipNode


def depart_calendar_html(self: HTML5Translator, _: calendar_block) -> None:
    pass  # SkipNode is raised in visit, so this is never called


def visit_calendar_unsupported(self: SphinxTranslator, node: calendar_block) -> None:
    self.visit_literal_block(
        nodes.literal_block(node["ical_source"], node["ical_source"])
    )
    raise nodes.SkipNode


def depart_calendar_unsupported(self: SphinxTranslator, _: calendar_block) -> None:
    pass
