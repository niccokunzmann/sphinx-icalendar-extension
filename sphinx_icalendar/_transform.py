from __future__ import annotations

from docutils import nodes
from sphinx.transforms import SphinxTransform

from sphinx_icalendar._nodes import calendar_block


class CalendarTransform(SphinxTransform):
    """Run after the document is read; intercepts code-block:: calendar."""

    default_priority = 400  # before most other transforms

    def apply(self) -> None:
        for node in self.document.findall(nodes.literal_block):
            if node.get("language") != "calendar":
                continue
            source = node.astext()
            new_node = calendar_block(ical_source=source)
            new_node.source = node.source
            new_node.line = node.line
            node.replace_self(new_node)
