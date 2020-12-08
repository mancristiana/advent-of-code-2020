
def getCommand(line):
    [command, value] = line.split(" ")
    value = int(value)
    return (command, value)

def getAccumulator(lines):
    lineIndexesVisited = []
    lineIndex = 0
    accumulator = 0
    isCorrectCode = False
    while lineIndex not in lineIndexesVisited:
        if (lineIndex == len(lines)):
            isCorrectCode = True
            return (accumulator, isCorrectCode)
        
        lineIndexesVisited.append(lineIndex)

        (command, value) = getCommand(lines[lineIndex])
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
    
    return (accumulator, isCorrectCode)

def getCodeVariation(lines, index):
    newLines = lines[:]
    command = lines[index]
    if (command[:3] == "nop"):
        newLines[index] = command.replace("nop", "jmp")
    elif (command[:3] == "jmp"):
        newLines[index] = command.replace("jmp", "nop")
    return newLines


with open('input.txt') as file:
    data = file.read()
    lines = data.split("\n")
    index = 0
    for line in lines:
        (command, value) = getCommand(line)
        if (command == "nop" or command == "jmp"):
            newLines = getCodeVariation(lines, index)
            (accumulator, isCorrectCode) = getAccumulator(newLines)
            if (isCorrectCode):
                print(accumulator)

        index += 1
