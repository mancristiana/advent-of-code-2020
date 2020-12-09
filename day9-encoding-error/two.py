
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



def findContinuousSet(numbers, totalSum):
    firstNumber = numbers[0]
    sum = firstNumber
    index = 1
    smallestNumber = firstNumber
    largestNumber = firstNumber
    while sum < totalSum:
        lastNumber = numbers[index]
        sum += lastNumber
        if (lastNumber > largestNumber):
            largestNumber = lastNumber
        if (lastNumber < smallestNumber):
            smallestNumber = lastNumber
        if (sum == totalSum):
            return smallestNumber + largestNumber
        index += 1

    return findContinuousSet(numbers[1:], totalSum)


with open('input.txt') as file:
    data = file.read().split("\n")
    numbers = [int(number) for number in data]
    weakness = findFirstInvalidNumber(numbers, 25)
    print(findContinuousSet(numbers, weakness))


