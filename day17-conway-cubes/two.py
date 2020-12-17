
def main():
    with open('input.txt') as file:
        rows = file.read().split("\n")
    initialActiveCubes = getInitialActiveCubes(rows)
    xLen = len(rows)
    yLen = len(rows[0])
    print(solve(initialActiveCubes, xLen, yLen))


def getInitialActiveCubes(rows):
    initialActiveCubes = []
    for x, row in enumerate(rows):
        for y, cube in enumerate(row):
            if (cube == "#"):
                initialActiveCubes.append(getCubeIndex(x, y, 0, 0))
    return initialActiveCubes


def solve(initialActiveCubes, xLen, yLen):
    activeCubes = initialActiveCubes
    for round in range(6):
        activeCubes = getActiveCubes(activeCubes, xLen, yLen, round + 1)
        print("round", round, len(activeCubes))
    
    return len(activeCubes)

def getActiveCubes(activeCubes, xLen, yLen, round):
    newActiveCubes = []
    for x in range(-round, xLen + round):
        for y in range(-round, yLen + round):
            for z in range(-round, round + 1):
                for w in range(-round, round + 1):
                    activeNeighbourCount = getActiveNeighbourCount(x, y, z, w, activeCubes)
                    active = isActive(x, y, z, w, activeCubes)
                    if (active and (activeNeighbourCount == 2 or activeNeighbourCount == 3)):
                        newActiveCubes.append(getCubeIndex(x, y, z, w))
                    elif not active and activeNeighbourCount == 3:
                        newActiveCubes.append(getCubeIndex(x, y, z, w))

    return newActiveCubes

def getActiveNeighbourCount(x, y, z, w, activeCubes):
    activeNeighbourCount = -1 if isActive(x, y, z, w, activeCubes) else 0
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            for nz in range(z-1, z+2):
                for nw in range(w-1, w+2):
                    if (isActive(nx, ny, nz, nw, activeCubes)):
                        activeNeighbourCount += 1
    return activeNeighbourCount

def isActive(x, y, z, w, activeCubes):
    return getCubeIndex(x, y, z, w) in activeCubes

def getCubeIndex(x, y, z, w):
    return f'{x},{y},{z},{w}'

main()
