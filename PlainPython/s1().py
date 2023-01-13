import numpy as n


def inputMatrixCreation():  # Esse você escreve todos os valores de uma vez
    def matrixCreation(x: int, y: int, items: list):
        cont = 0
        if (len(items) > x*y):
            print('Too much values, insert only X*Y characters at max')
            return inputMatrixCreation()
        else:
            mat = n.zeros((x, y), dtype=int)
            for i in range(x):
                for j in range(y):
                    if (cont == len(items) - 0):
                        break
                    mat[i][j] = items[cont]
                    cont = cont + 1
        return (mat)
    Show = input('Do you want to see the resultant matrix?\n >>>')
    string = input('Enter your matrix dimension \n >>>')
    valX = int(string[0])
    valY = int(string[2])

    values = input('Enter your values, can be separated by commas\n >>>')
    importantValues = values.split(',')
    if (Show.casefold() == 'yes'):
        newMat = matrixCreation(valX, valY, importantValues)
        print(newMat)
    else:
        newMat = matrixCreation(valX, valY, importantValues)
        return (newMat)


inputMatrixCreation()
