allArrangements = []

def getArrangements(numbers):
    numbersString = str(numbers)
    if numbersString not in allArrangements:
        allArrangements.append(numbersString)
    else:
        return

    length = len(numbers)
    for index in range(1, length - 1):
        if (numbers[index + 1] - numbers[index - 1] <= 3):
            getArrangements(numbers[:index] + numbers[index + 1:])

# with open('example.txt') as file:
with open('input.txt') as file:
    data = file.read().split("\n")
    numbers = [int(number) for number in data]
    numbers.sort()
    
    numbers = [0] + numbers[:]
    getArrangements(numbers)
    print(len(allArrangements))