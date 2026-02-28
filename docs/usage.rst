Usage
=====


Calendar rendering
------------------

Write a ``.. code-block:: calendar`` directive anywhere in your reStructuredText source.
The body may be either:

* :rfc:`5545` iCalendar (ICS) — the ``BEGIN:VCALENDAR`` text format, or
* :rfc:`7265` jCal — the JSON representation of iCalendar.

The extension detects the format automatically.

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

Below, we use a different ICS source to show a calendar with a name and description.
The original ICS formatting is preserved.


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


The example below is specified as jCal JSON.
The original JSON formatting is preserved.

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

ICS syntax highlighting
-----------------------

The extension also registers an ``ics`` (and ``icalendar``) language alias for Pygments so you can highlight raw ICS snippets in ordinary code blocks without triggering the calendar rendering:

.. code-block:: rst

    .. code-block:: ics

        BEGIN:VCALENDAR
        BEGIN:VEVENT
        DTSTART;TZID="America/New_York":20260401T090000
        DTEND;TZID="America/New_York":20260401T100000
        SUMMARY:Quarterly review
        END:VEVENT
        END:VCALENDAR

The result is a static, highlighted code block:

.. code-block:: ics

    BEGIN:VCALENDAR
    BEGIN:VEVENT
    DTSTART;TZID="America/New_York":20260401T090000
    DTEND;TZID="America/New_York":20260401T100000
    SUMMARY:Quarterly review
    END:VEVENT
    END:VCALENDAR

jCal syntax highlighting
------------------------

The extension also registers ``jcal`` (and ``jcalendar``) as language aliases that apply JSON highlighting to raw jCal snippets without triggering the calendar rendering:

.. code-block:: rst

    .. code-block:: jcal

        ["vcalendar",
          [["version", {}, "text", "2.0"]],
          [["vevent",
            [
              ["summary",  {}, "text",      "Quarterly review"],
              ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
              ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
            ], []
          ]]
        ]

The result is a static, JSON-highlighted code block:

.. code-block:: jcal

    ["vcalendar",
      [["version", {}, "text", "2.0"]],
      [["vevent",
        [
          ["summary",  {}, "text",      "Quarterly review"],
          ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
          ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
        ], []
      ]]
    ]

The highlighting is provided by Pygments' built-in JSON lexer.
