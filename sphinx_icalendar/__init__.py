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

from sphinx_icalendar._setup import setup
from sphinx_icalendar.version import (
    __version__,
    __version_tuple__,
    version,
    version_tuple,
)

__all__ = ["setup", "__version__", "__version_tuple__", "version", "version_tuple"]
