
def main():
    with open('input.txt') as file:
        [cardPublicKey, doorPublicKey] = file.read().split("\n")
    print(solve(int(cardPublicKey), int(doorPublicKey)))


def solve(cardPublicKey, doorPublicKey):
    cardLoopSize = getLoopSize(cardPublicKey)
    # doorLoopSize = getLoopSize(doorPublicKey)
    return transform(doorPublicKey, cardLoopSize)

def getLoopSize(publicKey):
    loopSize = 0
    value = 1
    while publicKey != value:
        loopSize += 1
        value = value * 7 % 20201227
    return loopSize

def transform(subjectNumber, loopSize):
    value = 1
    for step in range(loopSize):
        value = value * subjectNumber % 20201227
    return value


if __name__ == "__main__":
    main()
