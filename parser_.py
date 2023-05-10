class Node:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __str__(self):
        return f"{self.type}: {self.value} -> {self.children}"

    def __repr__(self):
        return self.__str__()

    def pretty_print(self, indent=0):
        result = "  " * indent + f"{self.type}: {self.value}\n"
        for child in self.children:
            if isinstance(child, Node):
                result += child.pretty_print(indent + 1)
            else:
                result += "  " * (indent + 1) + repr(child) + "\n"
        return result


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        node = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ("PLUS", "MINUS"):
            operator = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            node = Node("OPERATOR", operator.value, [node, right])
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ("MULTIPLY", "DIVIDE"):
            operator = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_factor()
            node = Node("OPERATOR", operator.value, [node, right])
        return node

    def parse_factor(self):
        token = self.tokens[self.pos]
        if token.type == "LPAREN":
            self.pos += 1
            node = self.parse_expression()
            self.pos += 1  # Skip the closing parenthesis
            return node
        elif token.type in ("SIN", "COS", "TAN"):
            self.pos += 1
            node = Node("FUNCTION", token.value, [self.parse_factor()])
            return node
        elif token.type in ("ARGMAX", "ARGMIN"):
            self.pos += 1
            self.pos += 1  # Skip the opening parenthesis
            args = []
            while self.tokens[self.pos].type != "RPAREN":
                args.append(self.parse_expression())
                if self.tokens[self.pos].type == "COMMA":
                    self.pos += 1
            self.pos += 1  # Skip the closing parenthesis
            return Node("FUNCTION", token.value, args)
        elif token.type == "NUMBER":
            self.pos += 1
            return Node("NUMBER", token.value)
        elif token.type == "MATRIX_BEGIN":
            self.pos += 1
            matrix_rows = []
            while self.tokens[self.pos].type != "MATRIX_END":
                matrix_row = self.parse_matrix_row()
                matrix_rows.append(matrix_row)
                if self.tokens[self.pos].type == "ROW_SEPARATOR":
                    self.pos += 1
            self.pos += 1  # Skip the MATRIX_END token
            return Node("MATRIX", None, matrix_rows)
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_matrix_row(self):
        row_elements = []
        while self.tokens[self.pos].type not in ("ROW_SEPARATOR", "MATRIX_END"):
            element = self.parse_expression()
            row_elements.append(element)
            if self.tokens[self.pos].type == "COLUMN_SEPARATOR":
                self.pos += 1
        return Node("MATRIX_ROW", None, row_elements)