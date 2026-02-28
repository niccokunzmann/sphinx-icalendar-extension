from pygments.lexer import RegexLexer
from pygments.lexers.data import JsonLexer
from pygments.token import Keyword, Literal, Name, Number, Operator, String, Text


class JCalLexer(JsonLexer):
    """Pygments lexer alias for jCal (RFC 7265) source blocks.

    jCal is JSON, so this is a thin subclass of JsonLexer that exposes the
    ``jcal`` and ``jcalendar`` language aliases and registers as a Pygments
    entry point so ``.. code-block:: jcal`` works globally.
    """

    name = "jCal"
    aliases = ["jcal", "jcalendar"]
    filenames: list[str] = []


class ICalendarLexer(RegexLexer):
    """Minimal Pygments lexer for iCalendar / jCal source blocks.

    Only used for syntax highlighting in the rare case a builder does not
    go through our HTML visitor (e.g. when inspecting the raw RST).  The
    transform replaces the node entirely for HTML output.
    """

    name = "iCalendar"
    aliases = ["icalendar", "ics"]
    filenames = ["*.ics"]

    tokens = {
        "root": [
            # iCalendar: property names before the colon
            (r"^(BEGIN|END)(:.+)$", Name.Tag),
            (r"^[A-Z][A-Z0-9-]+(?=[:;])", Keyword),
            # parameter values  key=value
            (r"(;[A-Z][A-Z0-9-]+)(=)", Name.Attribute),
            # colon separator
            (r":", Operator),
            # quoted strings
            (r'"[^"]*"', String),
            # dates and datetimes — longest patterns first, Z optional
            (r"\d{8}T\d{6}Z?", Literal.Date),  # iCal datetime
            (r"\d{8}", Literal.Date),  # iCal date
            # numbers (e.g. SEQUENCE:0)
            (r"\b\d+(\.\d*)?\b", Number),
            # comments / unknown
            (r".+", Text),
            (r"\n", Text),
        ],
    }
