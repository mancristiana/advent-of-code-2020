
def main():
    with open('input.txt') as file:
        [playerData1, playerData2] = file.read().split("\n\n")
    deck1 = getDeckFromPlayerData(playerData1)
    deck2 = getDeckFromPlayerData(playerData2)

    print(solve(deck1, deck2))


def getDeckFromPlayerData(playerData):
    deckData = playerData.split("\n")
    deck = [int(card) for card in deckData[1:]]
    return deck


def solve(deck1, deck2):
    while (len(deck1) > 0 and len(deck2) > 0):
        playRound(deck1, deck2)
    if (len(deck1) > len(deck2)):
        return calculateScore(deck1)
    else:
        return calculateScore(deck2)


def playRound(deck1, deck2):
    playedCard1 = deck1.pop(0)
    playedCard2 = deck2.pop(0)
    if (playedCard1 > playedCard2):
        deck1.append(playedCard1)
        deck1.append(playedCard2)

    if (playedCard2 > playedCard1):
        deck2.append(playedCard2)
        deck2.append(playedCard1)


def calculateScore(deck):
    totalScore = 0
    cardScore = len(deck)
    for card in deck:
        totalScore += card * cardScore
        cardScore -= 1
    return totalScore


if __name__ == "__main__":
    main()
