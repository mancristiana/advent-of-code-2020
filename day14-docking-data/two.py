
def main():
    with open('input.txt') as file:
        lines = file.read().split("\n")

    print(solve(lines))

def solve(lines):
    memory = {}
    mask = "" 
    for line in lines:
        if (line.startswith("mask")):
            mask = line.replace("mask = ", "")
        else:
            memAddress, value = getMemAddressAndValue(line)
            maskedMemAddresses = getMaskedValues(mask, memAddress)
            for maskedMemAddress in maskedMemAddresses:
                memory[maskedMemAddress] = value

    sum = 0
    for memAddress in memory:
        sum += memory[memAddress]
    return sum

def getMemAddressAndValue(line):
    line = line.replace("mem[", "")
    [memAddress, value] = line.split("] = ")
    return int(memAddress), int(value)

def getMaskedValues(mask, value):
    maskedValues = []
    bitArray = list(format(value, '036b'))
    floatingCount = 0
    for index in range(0, 36):
        if (mask[index] != '0'):
            bitArray[index] = mask[index]
        if (mask[index] == 'X'):
            floatingCount += 1

    if (floatingCount == 0):
        return [getIntFromBitArray(bitArray)]

    for number in range(2 ** floatingCount):
        floatingNumbers = list(format(number, "0" + str(floatingCount) + "b"))
        possibleBitArray = []
        for bit in bitArray:
            if bit == 'X':
                possibleBitArray.append(floatingNumbers.pop())
            else:
                possibleBitArray.append(bit)
        
        maskedValues.append(getIntFromBitArray(possibleBitArray))

    maskedValues

    return maskedValues

def getIntFromBitArray(bitArray):
    return int("".join(bitArray), 2)
main()