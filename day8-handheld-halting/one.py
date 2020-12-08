
def getAccumulator(lines):
    lineIndexesVisited = []
    lineIndex = 0
    accumulator = 0
    while lineIndex not in lineIndexesVisited:
        lineIndexesVisited.append(lineIndex)
        currentInstruction = lines[lineIndex]
        [command, value] = currentInstruction.split(" ")
        value = int(value)
        if (command == "nop"):
            lineIndex += 1
        elif (command == "jmp"):
            lineIndex += value
        elif (command == "acc"):
            accumulator += value
            lineIndex += 1
        else:
            print("Unknown instruction", command)
            break
    
    return accumulator


with open('input.txt') as file:
    data = file.read()
    instructions = data.split("\n")
    print(getAccumulator(instructions))
