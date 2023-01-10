
import math as mh


def findSqrt(number: int, finderStart: int, finderFinal: int):
    for e in range(finderStart, (finderFinal + 1)):
        if (mh.sqrt(number) == mh.sqrt(e)):
            if (mh.sqrt(number) == int(mh.sqrt(number))):
                return (number, int(mh.sqrt(number)))
            else:
                return (number, mh.sqrt(number))
    if (type(number) == float):
        return


findSqrt(10, 0, 10)
