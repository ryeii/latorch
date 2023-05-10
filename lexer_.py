import re

# Token types
TOKEN_TYPES = [
    ("NUMBER", r"\d+(\.\d+)?"),
    ("ARGMAX", r"\\argmax"),
    ("ARGMIN", r"\\argmin"),
    ("SIN", r"\\sin"),
    ("COS", r"\\cos"),
    ("TAN", r"\\tan"),
    ("MATRIX_BEGIN", r"\\begin\{bmatrix\}"),
    ("MATRIX_END", r"\\end\{bmatrix\}"),
    ("ROW_SEPARATOR", r"\\\\"),
    ("COLUMN_SEPARATOR", r"&"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("WS", r"\s+"),
]

# Combine patterns into a single regex
TOKEN_PATTERN = re.compile("|".join("(?P<%s>%s)" % pair for pair in TOKEN_TYPES))


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type}: {self.value}"
    

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = []

    def tokenize(self):
        for match in re.finditer(TOKEN_PATTERN, self.input_string):
            for token_type, token_regex in TOKEN_TYPES:
                token_value = match.group(token_type)
                if token_value is not None:
                    # Ignore whitespace tokens
                    if token_type != "WS":
                        self.tokens.append(Token(token_type, token_value))
                    break
        return self.tokens