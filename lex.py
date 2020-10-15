import re
from typing import NamedTuple, Iterable

class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    tokens = [
        ("STRING", r"\".*\""),
        ("NUMBER", r"(?:\+|\-|)?\d+(\.\d*)?"),
        ("NAME", r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"),
        ("CHAR", r"#\\[a-zA-Z]*"),
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
        ("BOOL", r"#[t|f]"),
        ("QUOTE", r"\'"),
    ]

    code = re.sub(r";;.*", "", code)

    groups = (f"(?P<{k}>{v})" for k, v in tokens)
    regex = re.compile('|'.join(groups))

    for m in re.finditer(regex, code):
        kind = m.lastgroup
        value = m.group()

        yield Token(kind, value)

    return [Token('INVALIDA', 'valor inválido')]


