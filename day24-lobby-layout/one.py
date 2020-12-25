
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
    return len(blackTilesCoords)


def calculateCoords(nw, ne, sw, se, e, w):
    wCoord = 2 * w - 2 * e + sw + nw - se - ne
    nCoord = nw + ne - sw - se
    return nCoord, wCoord


def formatCoords(nCoord, wCoord):
    return f"{str(nCoord)},{str(wCoord)}"


def getCoords(formattedCoords):
    [nCoord, wCoord] = formatCoords.split(",")
    return int(nCoord), int(wCoord)


if __name__ == "__main__":
    main()
