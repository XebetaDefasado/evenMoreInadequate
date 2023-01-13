import numpy as np

matrix = np.array([[1, 4], [2, 5], [3, 6]], dtype=int)


def manipulate2(matrix):
    x = len(matrix[0])
    y = len(matrix)

    newMatrix = np.zeros((x, y))
    for i in range(x):
        for j in range(y):
            newMatrix[i][j] = matrix[j][i]
    return (newMatrix)


def manipulate(matrix):
    cont = 0
    x = len(matrix[0])
    y = len(matrix)

    newMatrix = np.zeros((x, y))

    indMatrix = []
    for i in range(y):
        for j in range(x):
            indMatrix.append(matrix[i][j])

    for I in range(x):
        for J in range(y):
            newMatrix[I][J] = indMatrix[cont]
            cont = cont + 1
    return (newMatrix)
