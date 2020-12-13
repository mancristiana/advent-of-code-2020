
def main():
    with open('input.txt') as file:
        instructions = [line.rstrip() for line in file.readlines()]
    print(solve(instructions))

def solve(instructions):
    directions = ["E", "S", "W", "N"]
    directionIndex = 0
    north = 0
    east = 0
    for instruction in instructions:
        action, value = getActionAndValue(instruction)
        print(instruction, directionIndex)
        direction = directions[directionIndex]
        if (action == "N" or direction == "N" and action == "F"):
            north += value
        elif (action == "S" or direction == "S" and action == "F"):
            north -= value
        elif (action == "E" or direction == "E" and action == "F"):
            east += value
        elif (action == "W" or direction == "W" and action == "F"):
            east -= value
        elif (action == "R"):
            print(instruction, directionIndex)
            directionIndex += value // 90
            directionIndex %= 4
        elif (action == "L"):
            print(instruction, directionIndex)
            directionIndex -= value // 90
            directionIndex %= 4
    
    return abs(north) + abs(east)


def getActionAndValue(instruction):
    return instruction[:1], int(instruction[1:])

main()