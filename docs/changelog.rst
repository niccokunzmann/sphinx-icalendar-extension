Changelog
=========

0.0.1 (2026-02-27)
-------------------

Initial release.

- Render ``.. code-block:: calendar`` directives as HTML event tables.
- Accept both :rfc:`5545` iCalendar (ICS) and :rfc:`7265` jCal (JSON) input,
  with automatic format detection.
- Display three tabs per block: a rendered event table, the ICS source, and
  the jCal source, using :pypi:`sphinx-design`.
- Show calendar name (``X-WR-CALNAME``) as a table caption and description
  (``X-WR-CALDESC``) below the table when present.
- Syntax-highlight ICS blocks with a custom Pygments lexer (aliases:
  ``ics``) and jCal blocks with the built-in
  JSON lexer.
- The lexer is registered as a Pygments entry point so
  ``.. code-block:: ics`` works in any Sphinx project that has the package
  installed, even without adding ``sphinx_icalendar`` to ``extensions``.
