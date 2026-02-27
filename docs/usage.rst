Usage
=====

Write a ``.. code-block:: calendar`` directive anywhere in your
reStructuredText source.  The body may be either:

* `iCalendar <https://www.rfc-editor.org/rfc/rfc5545>`_ (RFC 5545) — the
  classic ``BEGIN:VCALENDAR`` text format, or
* `jCal <https://www.rfc-editor.org/rfc/rfc7265>`_ (RFC 7265) — the JSON
  representation of iCalendar.

The extension detects the format automatically: sources starting with ``[``
are parsed as jCal; everything else is treated as iCalendar.
The extension parses every ``VEVENT`` component and renders the results as
an HTML table.

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


Examples
--------

Below, we use an ICS source a calendar with a name and description:

.. code-block:: calendar

    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:collective/icalendar
    CALSCALE:GREGORIAN
    METHOD:PUBLISH
    X-WR-CALNAME:Holidays
    X-WR-TIMEZONE:Etc/GMT
    X-WR-CALDESC:Three holidays in the year
    BEGIN:VEVENT
    SUMMARY:New Year's Day
    DTSTART:20220101
    DTEND:20220101
    DESCRIPTION:Happy New Year!
    UID:636a0cc1dbd5a1667894465@icalendar
    DTSTAMP:20221108T080105Z
    STATUS:CONFIRMED
    TRANSP:TRANSPARENT
    SEQUENCE:0
    END:VEVENT
    BEGIN:VEVENT
    SUMMARY:Orthodox Christmas
    DTSTART:20220107
    DTEND:20220107
    LOCATION:Russia
    DESCRIPTION:It is Christmas again!
    UID:636a0cc1dbfd91667894465@icalendar
    STATUS:CONFIRMED
    TRANSP:TRANSPARENT
    SEQUENCE:0
    END:VEVENT
    BEGIN:VEVENT
    SUMMARY:International Women's Day
    DTSTART:20220308
    DTEND:20220308
    DESCRIPTION:May the feminine be honoured!
    UID:636a0cc1dc0f11667894465@icalendar
    STATUS:CONFIRMED
    TRANSP:TRANSPARENT
    SEQUENCE:0
    END:VEVENT
    END:VCALENDAR

The example below is specified as jCal JSON:

.. code-block:: calendar

    ["vcalendar",
      [
        ["version", {}, "text", "2.0"],
        ["prodid",  {}, "text", "-//sphinx-icalendar//EN"]
      ],
      [
        ["vevent",
          [
            ["summary",  {}, "text",      "Sprint planning"],
            ["dtstart",  {}, "date-time", "2026-03-02T10:00:00Z"],
            ["dtend",    {}, "date-time", "2026-03-02T11:00:00Z"],
            ["location", {}, "text",      "Room 42"]
          ], []
        ], [
          "vevent",
          [
            ["summary",  {}, "text",      "Sprint review"],
            ["dtstart",  {}, "date-time", "2026-03-13T14:00:00Z"],
            ["dtend",    {}, "date-time", "2026-03-13T15:00:00Z"],
            ["location", {}, "text",      "Room 42"]
          ], []
        ]
      ]
    ]
