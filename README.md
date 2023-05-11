# latorch - Latex to Pytorch Translator

Welcome to the Latex to Pytorch Translator! This tool allows you to evaluate equations in Latex with Pytorch.

## Supported Operations

- Special functions: argmax, argmin
- Trigonometry: sin, cos, tan
- Matrix operations: addition, subtraction, and multiplication
- Scalar operations: addition and multiplication with matrices
- Basic scaler operations

## Examples

Here are some examples of LaTeX equations and their corresponding PyTorch code generated by our tool:

1. Matrix addition:

Input:

$$
\begin{bmatrix} 1 & 2 \ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \ 7 & 8 \end{bmatrix}
$$

```
\begin{bmatrix} 1 & 2 \ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \ 7 & 8 \end{bmatrix}
```

Output: 

```
tensor([[6., 7.],
        [8., 9.]])
```