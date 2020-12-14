def main():
    with open('input.txt') as file:
        file.readline()
        busses = file.readline().split(",")
        bussesTuples = [(int(busId), minutes) for minutes, busId in enumerate(busses) if busId != "x"]

    print(solve(bussesTuples))

def solve(bussesTuples):
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    time = 0
    N = 1
    for busId, minutes in bussesTuples:
        N *= busId
    
    for busId, minutes in bussesTuples:
        yi = N // busId
        zi = pow(yi, -1, busId)
        ai = busId - minutes

        time += ai * yi * zi

    return time % N

main()