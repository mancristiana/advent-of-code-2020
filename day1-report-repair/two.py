# https://adventofcode.com/2020/day/1

def getReportNumber(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                numberI = int(numbers[i])
                numberJ = int(numbers[j])
                numberK = int(numbers[k])
                if numberI + numberJ + numberK == 2020:
                    return numberI * numberJ * numberK

with open('inputExample.txt') as file:
    data = file.read()
    numbers = data.split("\n")
    numbers.pop()
    print(getReportNumber(numbers))
