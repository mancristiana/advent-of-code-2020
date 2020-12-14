
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
            memory[memAddress] = getMaskedValue(mask, value)

    sum = 0
    for memAddress in memory:
        sum += memory[memAddress]
    return sum

def getMemAddressAndValue(line):
    line = line.replace("mem[", "")
    [memAddress, value] = line.split("] = ")
    return int(memAddress), int(value)

def getMaskedValue(mask, value):
    maskedValue = value
    bitValue = list(format(value, '036b'))
    for index in range(0, 36):
        if (mask[index] != 'X'):
            bitValue[index] = mask[index]
    maskedValue = int("".join(bitValue), 2)
    return maskedValue

main()