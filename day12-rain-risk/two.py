
def main():
    with open('input.txt') as file:
        instructions = [line.rstrip() for line in file.readlines()]
    print(solve(instructions))

def solve(instructions):
    # E, S, W, N
    waypoint = [10, 0, 0, 1] 
    north = 0
    east = 0
    for instruction in instructions:
        action, value = getActionAndValue(instruction)
        if action == "F":
            north += waypoint[3] * value - waypoint[1] * value
            east += waypoint[0] * value - waypoint[2] * value
        elif (action == "N"):
            waypoint[3] += value
        elif (action == "S"):
            waypoint[1] += value
        elif (action == "E"):
            waypoint[0] += value
        elif (action == "W"):
            waypoint[2] += value
        elif (action == "R"):
            waypoint = rotate(waypoint, -(value // 90) % 4)
        elif (action == "L"):
            waypoint = rotate(waypoint, (value // 90) % 4)
        print(instruction, waypoint, north, east)
    
    return abs(north) + abs(east)

def rotate(l, n):
    return l[n:] + l[:n]

def getActionAndValue(instruction):
    return instruction[:1], int(instruction[1:])

main()