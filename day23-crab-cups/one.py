
def main():
    with open('input.txt') as file:
        cups = [int(cup) for cup in file.read()]
    print(solve(cups))


def solve(cups):
    cupsLen = len(cups)
    for step in range(100):
        print(f"-- move {step + 1} --")
        print("cups:", cups)
        currentCup = cups[0]
        print("current cup:", currentCup)
        destinationCup = findDestinationCup(cups, currentCup - 1)
        pickUp = [
            cups.pop(1),
            cups.pop(1),
            cups.pop(1)
        ]
        print("pick up:", pickUp)
        print("destination:", destinationCup)
        destinationIndex = cups.index(destinationCup) + 1
        if (destinationIndex >= cupsLen):
            cups.extend(pickUp)
        else:
            cups[destinationIndex:destinationIndex] = pickUp
        cups.append(cups.pop(0))
    return getLabels(cups)


def findDestinationCup(cups, destinationCup):
    destinationCup = 9 if (destinationCup < 1) else destinationCup
    if (destinationCup in cups[1:4]):
        return findDestinationCup(cups, destinationCup - 1)

    return destinationCup


def getLabels(cups):
    cup1Index = cups.index(1)
    orderedCups = None
    if (cup1Index == len(cups) - 1):
        orderedCups = cups[:cup1Index]
    else:
        orderedCups = cups[cup1Index + 1:] + cups[:cup1Index]
    return "".join([str(cup) for cup in orderedCups])


if __name__ == "__main__":
    main()
