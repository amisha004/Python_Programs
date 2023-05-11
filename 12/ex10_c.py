# Define two matrices of the same size
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Create an empty matrix to hold the result
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Perform matrix multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result
for row in result:
    print(row)
