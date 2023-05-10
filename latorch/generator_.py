import torch

class PyTorchCodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        return self._process_node(self.ast)

    def _process_node(self, node):
        if node.type == "NUMBER":
            return torch.tensor(float(node.value))
        elif node.type == "OPERATOR":
            left = self._process_node(node.children[0])
            right = self._process_node(node.children[1])
            if node.value == "+":
                return torch.add(left, right)
            elif node.value == "-":
                return torch.sub(left, right)
            elif node.value == "*":
                if left.dim() == 0 or right.dim() == 0:
                    return torch.mul(left, right)
                else:
                    return torch.matmul(left, right)
            elif node.value == "/":
                return torch.div(left, right)
        elif node.type == "FUNCTION":
            if node.value in ("\\sin", "\\cos", "\\tan"):
                child = self._process_node(node.children[0])
                if node.value == "\\sin":
                    return torch.sin(child)
                elif node.value == "\\cos":
                    return torch.cos(child)
                elif node.value == "\\tan":
                    return torch.tan(child)
            elif node.value == "\\argmax":
                args = [self._process_node(arg) for arg in node.children]
                return torch.argmax(torch.tensor(args))
            elif node.value == "\\argmin":
                args = [self._process_node(arg) for arg in node.children]
                return torch.argmin(torch.tensor(args))
        elif node.type == "MATRIX":
            rows = [self._process_node(row) for row in node.children]
            return torch.stack(rows)
        elif node.type == "MATRIX_ROW":
            elements = [self._process_node(element) for element in node.children]
            return torch.tensor(elements)
        else:
            raise ValueError(f"Unsupported node type: {node.type}")