from latorch.lexer_ import Lexer
from latorch.parser_ import Parser
from latorch.generator_ import PyTorchCodeGenerator

input_string = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} * \sin(\argmax(1, 2))"
input_string_1 = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}"
input_string_2 = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} * \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}"
input_string_3 = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + 5"
input_string_4 = r"\cos(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix})"
input_string_5 = r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} * \sin(\argmin(1, 2))"
input_string_6 = r"\begin{bmatrix} \cos(0) & 2 & 3 \\ 4 & \argmax(\sin(0.5), \cos(0.5)) & 6 \end{bmatrix} * \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix} * \sin(\argmin(2, 1))"

def evaluate(input_string):
    lexer = Lexer(input_string)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    code_generator = PyTorchCodeGenerator(ast)
    result = code_generator.generate()
    return result

for input_string in (input_string, input_string_1, input_string_2, input_string_3, input_string_4, input_string_5, input_string_6):
    print(evaluate(input_string))
