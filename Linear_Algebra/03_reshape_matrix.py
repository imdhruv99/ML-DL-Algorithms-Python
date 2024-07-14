"""
Write a Python function that reshapes a given matrix into a specified shape.

Example:
        input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
        output: [[1, 2], [3, 4], [5, 6], [7, 8]]
        reasoning: The given matrix is reshaped from 2x4 to 4x2.

"""

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    flatten =  [item for sublist in a for item in sublist]

    # check element count between flatten list and new_shape requirement
    if len(flatten) != new_shape[0] * new_shape[1]:
        raise ValueError("The total number of elements does not match the new shape")
    
    reshaped_matrix = []
    for row_index in range(new_shape[0]):
        reshaped_matrix.append(flatten[row_index * new_shape[1]:(row_index + 1) * new_shape[1]])
    return reshaped_matrix

# test case 1
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))

# test case 2
print(reshape_matrix([[1,2,3],[4,5,6]], (3, 2)))
