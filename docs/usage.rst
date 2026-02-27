Usage
=====

Write a ``.. code-block:: calendar`` directive anywhere in your
reStructuredText source. The body must be valid
`iCalendar <https://www.rfc-editor.org/rfc/rfc5545>`_ (RFC 5545) text.
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


Example — sphinx-icalendar development milestones
--------------------------------------------------

The table below is produced directly by this extension from the iCalendar
source that follows it. 

.. code-block:: calendar

    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:collective/icalendar
    CALSCALE:GREGORIAN
    METHOD:PUBLISH
    X-WR-CALNAME:Holidays
    X-WR-TIMEZONE:Etc/GMT
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
