
with open('input.txt') as file:
    data = file.read().split("\n")
    numbers = [int(number) for number in data]
    numbers.sort()

    diffOfOne = 0
    diffOfThree = 1
    prevNumber = 0
    for number in numbers:
        diff = number - prevNumber
        if (diff == 1):
            diffOfOne += 1
        elif (diff == 3):
            diffOfThree += 1
        
        prevNumber = number

    print(diffOfThree * diffOfOne)
