
def main():
    with open('input.txt') as file:
        numbers = [int(line.rstrip()) for line in file.readlines()]
    numbers.sort()
    print(solve(numbers))

def solve(numbers):
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

    return diffOfOne * diffOfThree

main()