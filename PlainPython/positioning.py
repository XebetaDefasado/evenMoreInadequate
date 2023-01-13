import numpy as n

x = n.array([[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]])
l = n.array([[1, 2], [5, 6], [9, 10], [13, 14]])


def columnRead(mat):
    totalLines = int(len(x))
    totalColumns = int(len(x[0]))
    columnLines = int(len(x))

    new = n.zeros((totalColumns, totalLines), dtype=int)
    ind = []
    ind2 = []
    for i in range(totalLines):
        for j in range(totalColumns):
            for k in range(int(columnLines / 2)):
                ind.append(mat[i][j])
    for k in range(totalColumns):
        for w in range(totalLines):
            ind2.append(ind[totalColumns*w + k])
    for v in range(totalLines):
        for u in range(totalColumns):
            new[u][v] = ind2[u + v*totalColumns]
    return (new)


def lineRead(mat):
    x = len(mat)
    y = len(mat[0])

    new = n.zeros((y, x), dtype=int)
    ind = []
    for i in range(x):
        for j in range(y):
            ind.append(mat[i][j])
    for u in range(y):
        for v in range(x):
            new[u][v] = ind[v + x*u]
    return (new)
