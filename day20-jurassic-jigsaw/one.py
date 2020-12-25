
def main():
    with open('input.txt') as file:
        tiles = file.read().split("\n\n")
    tileDictionary = {}
    for tile in tiles:
        tileId, tileEdges = getTileIdAndEdges(tile)
        tileDictionary[tileId] = tileEdges

    print(solve(tileDictionary))

def getTileIdAndEdges(tile):
    tileRows = tile.split("\n")
    tileId = int(tileRows[0].replace("Tile", "").replace(":", ""))
    tileRows = tileRows[1:]
    topEdge = tileRows[0]
    bottomEdge = tileRows[-1][::-1]
    leftEdge = ""
    rightEdge = ""
    for tileRow in tileRows:
        leftEdge += tileRow[0]
        rightEdge += tileRow[-1]
    leftEdge = leftEdge[::-1]

    return tileId, [topEdge, rightEdge, bottomEdge, leftEdge]


def solve(tileDictionary):
    cornersProduct = 1
    for tile in tileDictionary:
        isCorner = isOutermostTile(tileDictionary, tile)
        if (isCorner):
            print(tile)
            cornersProduct *= tile
    return cornersProduct

def isOutermostTile(tileDictionary, tile):
    [topEdge, rightEdge, bottomEdge, leftEdge] = tileDictionary[tile]
    foundMatches = [False, False, False, False]
    for otherTile in tileDictionary:
        if otherTile != tile:
            otherTileEdges = tileDictionary[otherTile]
            for otherTileEdge in otherTileEdges:
                if (topEdge == otherTileEdge or topEdge == otherTileEdge[::-1]):
                    foundMatches[0] = True
                if (rightEdge == otherTileEdge or rightEdge == otherTileEdge[::-1]):
                    foundMatches[1] = True
                if (bottomEdge == otherTileEdge or bottomEdge == otherTileEdge[::-1]):
                    foundMatches[2] = True
                if (leftEdge == otherTileEdge or leftEdge == otherTileEdge[::-1]):
                    foundMatches[3] = True

    return sum(foundMatches) == 2

            





if __name__ == "__main__":
    main()
