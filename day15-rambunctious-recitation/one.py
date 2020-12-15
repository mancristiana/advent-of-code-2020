
def main():
    with open('input.txt') as file:
        numbers = [int(number) for number in file.read().split(",")]

    print(solve(numbers))

def solve(numbers):
    spokenOnTurn = {}
    index = 1
    for number in numbers:
        spokenOnTurn[number] = index
        index += 1
    
    lastNumber = numbers[-1]
    
    for index in range(index - 1, 2020):
        newNumber = index - spokenOnTurn[lastNumber] if lastNumber in spokenOnTurn else 0
        spokenOnTurn[lastNumber] = index
        lastNumber = newNumber

    return lastNumber

main()