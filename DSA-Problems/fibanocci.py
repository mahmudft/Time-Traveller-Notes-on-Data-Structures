

def fibanocci(num: int):
    if num == 1:
        return num
    value1, value2 = 0, 1

    for x in range(2, num+1):
        nextValue = value1 + value2

        value1 = value2
        value2 = nextValue

    return value2


print(fibanocci(4))