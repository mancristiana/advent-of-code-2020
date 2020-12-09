
def isValid(numbers, sum):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            numberI = int(numbers[i])
            numberJ = int(numbers[j])
            if numberI + numberJ == sum:
                # print(numberI, numberJ)
                return True

def findFirstInvalidNumber(numbers, preamble):
    length = len(numbers)
    for i in range(preamble, length):
        # print(numbers[i], numbers[i-preamble:i])
        if not isValid(numbers[i-preamble:i], numbers[i]):
            return numbers[i]

with open('input.txt') as file:
    data = file.read().split("\n")
    numbers = [int(number) for number in data]
    print(findFirstInvalidNumber(numbers, 25))


