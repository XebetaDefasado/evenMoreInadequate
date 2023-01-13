import numpy as n

m = n.array([[1, 4], [2, 5], [3, 6]])
m2 = n.array([[1, 5], [2, 6], [3, 7], [4, 8]])
m3 = n.array([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]])
m4 = n.array([[1, 2], [3, 4], [5, 6]])


def manip(matrix: any):
   # -----------------#
    x = len(matrix)
    y = len(matrix[0])
   # --------------------#
    if (x == y):
        return (matrix)
   # --------------------#
    new = n.zeros((y, x))
    ind = []
    contagem = int(0)
   # ----------------------------------------------------------#
    for i in range(y):
        for j in range(int(n.ceil(x / 2)) - (x % 2) * (i % 2)):
            ind.append(matrix[2*j + (x % 2) * (i % 2)][i])
   # -----------------------------------------------------------#
    for w in range(y):
        for v in range(int(n.floor(x / 2)) + (x % 2) * (w % 2)):
            ind.append(matrix[(2*v + 1) - (x % 2) * (w % 2)][w])
   # ------------------------------------------------------------#
    for I in range(y):
        for J in range(x):
            new[I][J] = ind[contagem]
            contagem = contagem + 1
    return (new)
   # --------------------------------#


print(m4)
print('')
print(manip(m4))
