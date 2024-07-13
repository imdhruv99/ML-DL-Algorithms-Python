"""
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10

"""

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	return [sum(x * y for x, y in zip(row, b)) for row in a] if a and len(a[0]) == len(b) else -1

# test case 1
print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]))

# test case 2
print(matrix_dot_vector([[1,2],[2,4],[6,8],[12,4]],[1,2,3]))