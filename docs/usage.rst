Usage
=====

Write a ``.. code-block:: calendar`` directive anywhere in your
reStructuredText source.  The body must be valid
`iCalendar <https://www.rfc-editor.org/rfc/rfc5545>`_ (RFC 5545) text.
The extension parses every ``VEVENT`` component and renders the results as
an HTML table with **Summary**, **Start**, **End**, and **Location** columns.

Syntax
------

.. code-block:: rst

    .. code-block:: calendar

        BEGIN:VCALENDAR
        BEGIN:VEVENT
        DTSTART:20260301T090000Z
        DTEND:20260301T100000Z
        SUMMARY:My event
        LOCATION:Somewhere
        END:VEVENT
        END:VCALENDAR

How it works
------------

The extension registers a :class:`~sphinx.transforms.SphinxTransform` that
runs after the RST source is parsed.  It walks the doctree and replaces every
``literal_block`` node whose ``language`` attribute equals ``"calendar"`` with
a custom ``calendar_block`` node.  An HTML visitor then turns that node into
a ``<table>`` — no post-processing step, no separate build stage.

Non-HTML builders (LaTeX, man, plain text) fall back to rendering the raw
iCalendar source as a literal block so the build never breaks.

Example — sphinx-icalendar development milestones
--------------------------------------------------

The table below is produced directly by this extension from the iCalendar
source that follows it.  The extension is documenting itself.

.. code-block:: calendar

    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//sphinx-icalendar//EN

    BEGIN:VEVENT
    DTSTART:20260210T000000Z
    DTEND:20260210T000000Z
    SUMMARY:Project started
    DESCRIPTION:Initial commit – CalendarTransform + HTML visitor.
    END:VEVENT

    BEGIN:VEVENT
    DTSTART:20260224T000000Z
    DTEND:20260224T000000Z
    SUMMARY:v0.1.0 released
    DESCRIPTION:First installable package published to PyPI.
    LOCATION:PyPI
    END:VEVENT

    BEGIN:VEVENT
    DTSTART:20260301T000000Z
    DTEND:20260301T000000Z
    SUMMARY:Docs published
    DESCRIPTION:This very page goes live — the extension documents itself.
    LOCATION:Read the Docs
    END:VEVENT

    END:VCALENDAR
