import numpy as n
s = n.array([[19, 22, 34], [48, 59, 63], [7, 4, 2]], dtype=int)


def formatting(list: list):
    denominator = len(list)
    stored = 0
    for e in list:
        stored = e + stored
    result = '{0} / {1}'
    result = result.format(stored, denominator)
    return result


def average(list: list):
    stored = 0
    # Se a lista tiver n elementos, você irá somar n elementos, den = len(list)
    denominator = len(list)
    for e in list:
        stored = e + stored
    result = stored / denominator
    return result


def calcAvg(mat):

    x = len(mat)
    y = len(mat[0])

    global aesthetic
    aestheticL = []
    aestheticC = []
    sumL = []
    compareLn = []
    for i in range(x):
        for j in range(y):
            sumL.append(mat[i][j])
        newAvg = average(sumL)
        compareLn.append(newAvg)
        format = formatting(sumL)
        aestheticL.append(format)
        sumL.clear()
    newAvg = float(0)
    format = ''
   # -----------------------------#
    sumC = []
    compareCol = []
    for u in range(x):
        for w in range(y):
            sumC.append(mat[w][u])
        newAvg = average(sumC)
        compareCol.append(newAvg)
        format = formatting(sumC)
        aestheticC.append(format)
        sumC.clear()
    newAvg = float(0)
    format = ''
   # -----------------------------#
    storedLn = 0
    for e in compareLn:
        if (e > storedLn):
            storedLn = e
            indx = compareLn.index(storedLn)
        else:
            pass
    formattLn = aestheticL[indx]
    finalLn = 'line {}: {}'
    finalLn = finalLn.format(indx + 1, (formattLn, storedLn))
   # ----------------------------------------#
    storedCol = 0
    for e in compareCol:
        if (e > storedCol):
            storedCol = e
            indx = compareCol.index(storedCol)
        else:
            pass
    formStdCol = aestheticC[indx]
    finalCol = 'column {0}: {1}'
    finalCol = finalCol.format(indx + 1, (formStdCol, storedCol))
   # -------------------------------------------#
    Champions = 'Highest averages:\n{0}\n{1}'
    Champions = Champions.format(finalLn, finalCol)
    print(Champions)


calcAvg(s)
