
def main():
    with open('input.txt') as file:
        tiles = file.read().split("\n")
    print(solve(tiles))


def solve(tiles):
    blackTilesCoords = []
    for tile in tiles:
        nw = tile.count("nw")
        ne = tile.count("ne")
        sw = tile.count("sw")
        se = tile.count("se")
        tile = tile.replace("nw", "").replace(
            "ne", "").replace("sw", "").replace("se", "")
        e = tile.count("e")
        w = tile.count("w")
        nCoord, wCoord = calculateCoords(nw, ne, sw, se, e, w)
        coords = formatCoords(nCoord, wCoord)
        if (coords in blackTilesCoords):
            blackTilesCoords.remove(coords)
        else:
            blackTilesCoords.append(coords)
    for day in range(100):
        print(f"Day {day}:", len(blackTilesCoords))
        blackTilesCoords = getTileCoordsToFlip(blackTilesCoords)
    return len(blackTilesCoords)


def getTileCoordsToFlip(blackTileCoords):
    blackTileCoordsAfterFlip = []
    checkedTiles = []
    for tile in blackTileCoords:
        nCoord, wCoord = getCoords(tile)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord, wCoord)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord, wCoord + 2)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord, wCoord - 2)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord + 1, wCoord + 1)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord + 1, wCoord - 1)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord - 1, wCoord + 1)
        flipIfNeeded(blackTileCoords, blackTileCoordsAfterFlip,
                     checkedTiles, nCoord - 1, wCoord - 1)

    return blackTileCoordsAfterFlip


def flipIfNeeded(blackTileCoords, tileCoordsToFlip, checkedTiles, nCoord, wCoord):
    tile = formatCoords(nCoord, wCoord)
    if (tile in checkedTiles):
        return

    checkedTiles.append(tile)
    isBlack = tile in blackTileCoords
    isFlip = hasToFlip(blackTileCoords, isBlack, nCoord, wCoord)
    # either black tile which doesn't need to flip or white tile which needs to flip
    if (isBlack != isFlip):
        tileCoordsToFlip.append(tile)


def hasToFlip(blackTileCoords, isBlack, nCoord, wCoord):
    count = 0
    if (formatCoords(nCoord, wCoord + 2) in blackTileCoords):
        count += 1
    if (formatCoords(nCoord, wCoord - 2) in blackTileCoords):
        count += 1
    if (formatCoords(nCoord + 1, wCoord + 1) in blackTileCoords):
        count += 1
    if (formatCoords(nCoord + 1, wCoord - 1) in blackTileCoords):
        count += 1
    if (formatCoords(nCoord - 1, wCoord + 1) in blackTileCoords):
        count += 1
    if (formatCoords(nCoord - 1, wCoord - 1) in blackTileCoords):
        count += 1

    if (isBlack):
        return count == 0 or count > 2
    else:
        return count == 2


def calculateCoords(nw, ne, sw, se, e, w):
    wCoord = 2 * w - 2 * e + sw + nw - se - ne
    nCoord = nw + ne - sw - se
    return nCoord, wCoord


def formatCoords(nCoord, wCoord):
    return f"{str(nCoord)},{str(wCoord)}"


def getCoords(formattedCoords):
    [nCoord, wCoord] = formattedCoords.split(",")
    return int(nCoord), int(wCoord)


if __name__ == "__main__":
    main()
