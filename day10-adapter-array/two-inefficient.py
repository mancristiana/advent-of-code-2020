
def main():
    adapters = [1, 2, 3, 4]
    adapters.sort()
    print(solve(adapters))

def solve(adapters):
    adapters = [0] + adapters[:] + [adapters[-1] + 3]
    return getArrangements(adapters, 1)

def getArrangements(adapters, startIndex):
    print(adapters)
    length = len(adapters)
    if (length <= 3):
        return 1
    sum = 1
    for index in range(startIndex, length - 1):
        if (adapters[index + 1] - adapters[index - 1] <= 3):
            sum += getArrangements(adapters[:index] + adapters[index + 1:], index)
    return sum

main()








