currentGroupArrangements = []

def getArrangements(numbers):
    numbersString = str(numbers)
    if numbersString not in currentGroupArrangements:
        currentGroupArrangements.append(numbersString)
    else:
        return
    
    length = len(numbers)
    for index in range(1, length - 1):
        if (numbers[index + 1] - numbers[index - 1] <= 3):
            getArrangements(numbers[:index] + numbers[index + 1:])

def getArrangementsForCurrentGroup(currentGroup):
    print(currentGroup)
    global currentGroupArrangements
    currentGroupArrangements = []
    getArrangements(currentGroup)
    print(len(currentGroupArrangements))
    return len(currentGroupArrangements) 

# with open('example.txt') as file:
with open('input.txt') as file:
    data = file.read().split("\n")
    numbers = [int(number) for number in data]
    numbers.sort()
    
    numbers = [0] + numbers[:] + [numbers[-1] + 3]
    prevNumber = 0
    currentGroup = [0]
    totalArrangements = 1
    print(numbers)
    for number in numbers:
        diff = number - prevNumber
        if (diff == 1):
            currentGroup.append(number)
        elif (diff == 3):
            currentGroup.append(number)
            if (len(currentGroup) >= 3):
                totalArrangements *= getArrangementsForCurrentGroup(currentGroup) 
            currentGroup = [number]
        
        prevNumber = number
    
    print(totalArrangements)
