# https://adventofcode.com/2020/day/3

def getEncounteredTrees(map, right, down):
    treeCount = 0
    xLen = len(map)
    yLen = len(map[0])
    x = down
    y = right
    
    while x < xLen:
        if map[x][y] == '#':
            treeCount += 1

        x = x + down
        y = (y + right) % yLen
    
    return treeCount

def getMapFromData(data):
    lines = data.split("\n")
    map = []
    for line in lines:
        map.append([char for char in line])

    return map

with open('input.txt') as file:
    data = file.read()
    map = getMapFromData(data)

    multiply = getEncounteredTrees(map, 1, 1)
    multiply *= getEncounteredTrees(map, 3, 1)
    multiply *= getEncounteredTrees(map, 5, 1)
    multiply *= getEncounteredTrees(map, 7, 1)
    multiply *= getEncounteredTrees(map, 1, 2)
    
    print(multiply)
