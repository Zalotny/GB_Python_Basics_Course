from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            raise ValueError('fail initialization matrix')
        rows = len(matrix[0])
        for line in matrix:
            if len(line) != rows:
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        matrix_lst = [f"| {' '.join(map(lambda numb: str(numb), line))} |" for line in self.matrix]
        matrix_str = '\n'.join(matrix_lst)

        return matrix_str

    def __add__(self, other):
        self_lines = len(self.matrix)
        self_rows = len(self.matrix[0])
        other_lines = len(other.matrix)
        other_rows = len(other.matrix[0])
        max_lines = max(self_lines, other_lines)
        max_rows = max(self_rows, other_rows)

        matrix_sum = []
        for i in range(max_lines):
            line_self = (self.matrix[i] + [0] * (max_rows - self_rows) if i < self_lines else [0] * max_rows)
            line_other = (other.matrix[i] + [0] * (max_rows - other_rows) if i < other_lines else [0] * max_rows)

            line_sum = list(map(lambda num_self, num_other: num_self + num_other, line_self, line_other))
            matrix_sum.append(line_sum)

        return Matrix(matrix_sum)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
