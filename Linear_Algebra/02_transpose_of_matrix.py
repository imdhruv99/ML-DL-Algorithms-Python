"""
Write a Python function that computes the transpose of a given matrix.

Example:
        input: a = [[1,2,3],[4,5,6]]
        output: [[1,4],[2,5],[3,6]]
        reasoning: The transpose of a matrix is obtained by flipping rows and columns.

"""

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a)
    columns = len(a[0])
    transpose = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transpose[j][i] = a[i][j]
    return transpose

def transpose_matrix_using_zip(a: list[list[int|float]]) -> list[list[int|float]]:
    return list(map(list, zip(*a)))

# test case 1
print(transpose_matrix([[1,2],[3,4],[5,6]]))

# test case 2
print(transpose_matrix_using_zip([[1,2,3],[4,5,6]]))