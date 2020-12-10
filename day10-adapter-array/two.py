def main():
    with open('input.txt') as file:
        adapters = [int(line.rstrip()) for line in file.readlines()]
    adapters.sort()
    print(solve(adapters))

def solve(adapters):
    adapters = [0] + adapters[:] + [adapters[-1] + 3]
    currentGroup = [0]
    previousAdapter = 0
    totalArrangements = 1

    for adapter in adapters:
        diff = adapter - previousAdapter
        if (diff == 1):
            currentGroup.append(adapter)
        elif (diff == 3):
            currentGroup.append(adapter)
            if (len(currentGroup) >= 3):
                totalArrangements *= getArrangements(currentGroup, 1) 
            currentGroup = [adapter]
        previousAdapter = adapter
    
    return totalArrangements

def getArrangements(adapters, startIndex):
    length = len(adapters)
    if (length <= 3):
        return 1
    sum = 1
    for index in range(startIndex, length - 1):
        if (adapters[index + 1] - adapters[index - 1] <= 3):
            sum += getArrangements(adapters[:index] + adapters[index + 1:], index)
    return sum

main()