from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Number, Operator, String, Text


class ICalendarLexer(RegexLexer):
    """Minimal Pygments lexer for iCalendar / jCal source blocks.

    Only used for syntax highlighting in the rare case a builder does not
    go through our HTML visitor (e.g. when inspecting the raw RST).  The
    transform replaces the node entirely for HTML output.
    """

    name = "iCalendar"
    aliases = ["calendar", "icalendar", "ics"]
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
            # numbers (e.g. SEQUENCE:0)
            (r"\b\d+\b", Number),
            # jCal JSON structure tokens
            (r"[\[\]{},]", Operator),
            # comments / unknown
            (r".+", Text),
            (r"\n", Text),
        ],
    }
