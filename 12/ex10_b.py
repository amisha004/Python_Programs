# Define two matrices of the same size
matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Create an empty matrix to hold the result
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Perform matrix addition
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the result
for row in result:
    print(row)
