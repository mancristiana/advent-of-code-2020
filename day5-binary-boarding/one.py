# https://adventofcode.com/2020/day/4

def getNumber(boardingPass, start, end):
    half = (end - start) // 2
    if (start == end):
        return start;
    elif (boardingPass[0] == "F" or boardingPass[0] == "L"):
        return getNumber(boardingPass[1:], start, start + half)
    else:
        return getNumber(boardingPass[1:], start + half + 1, end)


def getSeatId(boardingPass):
    row = getNumber(boardingPass[:-3], 0, 127)
    column = getNumber(boardingPass[-3:], 0, 7)

    return row * 8 + column

with open('input.txt') as file:
    data = file.read()
    boardingPasses = data.split("\n")

    highest = 0
    for boardingPass in boardingPasses:
        seatId = getSeatId(boardingPass)
        if (seatId > highest):
            highest = seatId

    print(highest)