from __future__ import annotations

from docutils import nodes


class calendar_block(nodes.General, nodes.Element):
    """Holds the raw iCalendar source; replaced by visitors during writing."""
