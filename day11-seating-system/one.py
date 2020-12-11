
def main():
    with open('example.txt') as file:
    # with open('input.txt') as file:
        seats = [[seat for seat in line.rstrip()] for line in file.readlines()]
    seats = getFloorAroundSeats(seats)
    print(solve(seats))

def getFloorAroundSeats(seats):
    cols = len(seats[0]) + 2
    floorRow = "." * cols
    return [floorRow] + [["."] + row[:] + ['.'] for row in seats] + [floorRow]

def solve(seats):
    rows = len(seats)
    cols = len(seats[0])
    seatsAfterRound = [[seat for seat in row] for row in seats]
    isChange = False
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            occupiedAdjacentSeats = getOccupiedAdjacentSeats(seats, i, j)
            if (seats[i][j] == 'L' and occupiedAdjacentSeats == 0):
                seatsAfterRound[i][j] = "#"
                isChange = True
            elif (seats[i][j] == '#' and occupiedAdjacentSeats >= 4):
                seatsAfterRound[i][j] = "L"
                isChange = True

    # print("____________________________")
    # printSeats(seatsAfterRound)
    if (isChange):
        return solve(seatsAfterRound)
    else:
        return countOccupiedSeats(seatsAfterRound)

def getOccupiedAdjacentSeats(seats, i, j):
    occupiedAdjacentSeats = 0
    if (seats[i - 1][j - 1] == '#'):
        occupiedAdjacentSeats += 1
    if (seats[i - 1][j] == '#'):
        occupiedAdjacentSeats += 1 
    if (seats[i - 1][j + 1] == '#'):
        occupiedAdjacentSeats += 1
    if (seats[i][j - 1] == '#'):
        occupiedAdjacentSeats += 1
    if (seats[i][j + 1] == '#'):
        occupiedAdjacentSeats += 1
    if (seats[i + 1][j - 1] == '#'):
        occupiedAdjacentSeats += 1 
    if (seats[i + 1][j] == '#'):
        occupiedAdjacentSeats += 1
    if (seats[i + 1][j + 1] == '#'):
        occupiedAdjacentSeats += 1
    return occupiedAdjacentSeats

def printSeats(seats):
    for row in seats:
        print(''.join(row))

def countOccupiedSeats(seats):
    count = 0
    for row in seats:
        for seat in row:
            if (seat == '#'):
                count += 1
    return count

main()