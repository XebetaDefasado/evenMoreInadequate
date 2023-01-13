import numpy as n
import math as mh

l = n.array([[1, 2], [3, 4], [5, 6]])
t = n.array([[1, 2, 3], [4, 5, 6]])

p = n.array([[1, 5], [2, 6], [3, 7], [4, 8]])
k = n.array([[1, 3, 5], [2, 4, 6]])


def MatrixManipulation(matrix, readingType='line' or 'column'):
    if (readingType == 'line'):
        def lineReading(mat):
           # -----------------#
            nLin = len(mat)
            nCol = len(mat[0])
           # -------------------------------------#
            new = n.zeros((nCol, nLin), dtype=int)
           # ---------------------------------------#
            for i in range(nCol):
                for j in range(nLin):
                    new[i][j] = mat.item(nLin*i + j)
           # ---------------------------------------#
            return (new)
        return lineReading(matrix)
    if (readingType == 'column'):
        def columnReading(mat):
           # -----------------#
            nLin = len(mat)
            nCol = len(mat[0])
           # -----------------#
            ind = []
           # -------------------------------------#
            new = n.zeros((nCol, nLin), dtype=int)
           # -------------------------------------#
            for i in range(nCol):
                for j in range(nLin):
                    ind.append(mat.item(nCol*j + i))
           # ---------------------------------------#
            for w in range(nLin):
                for v in range(nCol):
                    new[v][w] = ind[v + (nCol * w)]
           # ---------------------------------------#
            return new
           # ---------------------------------------#
        return columnReading(matrix)
    else:
        print('Incorrect reading style')
