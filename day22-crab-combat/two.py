
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
    global gameConfigs
    game1 = 1
    gameConfigs[game1] = []
    winner = playRecursiveCombat(deck1, deck2, game1)
    if (winner == 1):
        return calculateScore(deck1)
    else:
        return calculateScore(deck2)


def playRecursiveCombat(deck1, deck2, game):
    global gameConfigs
    global gameId

    while (len(deck1) > 0 and len(deck2) > 0):
        gameConfig = getGameConfiguration(deck1, deck2)
        if (gameConfig in gameConfigs[game]):
            return 1
        else:
            gameConfigs[game].append(gameConfig)
        playedCard1 = deck1.pop(0)
        playedCard2 = deck2.pop(0)
        winner = 0
        if (playedCard1 <= len(deck1) and playedCard2 <= len(deck2)):
            gameId += 1
            gameConfigs[gameId] = []
            winner = playRecursiveCombat(
                deck1[:playedCard1], deck2[:playedCard2], gameId)
        elif(playedCard1 > playedCard2):
            winner = 1
        else:
            winner = 2

        if (winner == 1):
            deck1.append(playedCard1)
            deck1.append(playedCard2)
        else:
            deck2.append(playedCard2)
            deck2.append(playedCard1)

    if (len(deck1) > len(deck2)):
        return 1
    else:
        return 2
        

def getGameConfiguration(deck1, deck2):
    return "Player 1's deck: " + str(deck1) + "\nPlayer 2's deck: " + str(deck2)


def calculateScore(deck):
    totalScore = 0
    cardScore = len(deck)
    for card in deck:
        totalScore += card * cardScore
        cardScore -= 1
    return totalScore


gameConfigs = {}
gameId = 1
if __name__ == "__main__":
    main()
