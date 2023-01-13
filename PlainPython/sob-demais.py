
def listShifting(list: list, int: int):
    for number in range(int):
        desiredNumber = list[len(list) - 1]
        list.pop(len(list) - 1)
        list.insert(0, desiredNumber)
    print(list)
