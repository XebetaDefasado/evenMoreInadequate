import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)


def matrixManipulationOne():
    newMatrix = np.zeros((3, 2))
    for i in range(3):
        for j in range(2):
            newMatrix[i][j] = matrix[j][i]
    print(newMatrix)


def matrixManipulationTwo(matrix):
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
    print(newMatrix)
