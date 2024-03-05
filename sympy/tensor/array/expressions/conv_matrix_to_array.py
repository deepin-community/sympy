from sympy.tensor.array.expressions import from_matrix_to_array
from sympy.tensor.array.expressions.conv_array_to_indexed import _conv_to_from_decorator

convert_matrix_to_array = _conv_to_from_decorator(from_matrix_to_array.convert_matrix_to_array)
