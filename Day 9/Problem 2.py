from math import prod

def findBasin(caveMap, y, x, basin):

    if caveMap[y][x] == '9' or (y, x) in basin:
        return basin

    basin.add((y, x))

    if y - 1 >= 0 and (y - 1, x) not in basin:
        findBasin(caveMap, y - 1, x, basin)

    if y + 1 < len(caveMap) and (y + 1, x) not in basin:
        findBasin(caveMap, y + 1, x, basin)

    if x - 1 >= 0 and (y, x - 1) not in basin:
        findBasin(caveMap, y, x - 1, basin)

    if x + 1 < len(caveMap[y]) and (y, x + 1) not in basin:
        findBasin(caveMap, y, x + 1, basin)

    return basin

def main():

    largestBasins = []
    pointsHit = set()
    caveMap = [lines.strip() for lines in open('input.txt').readlines()]

    for y in range(len(caveMap)):

        for x in range(len(caveMap[y])):

            if (y, x) not in pointsHit and caveMap[y][x] != '9':

                newBasin = findBasin(caveMap, y, x, set())
                pointsHit.update(newBasin)
                largestBasins.append(len(newBasin))

                if len(largestBasins) > 3:
                    largestBasins.pop(largestBasins.index(min(largestBasins)))

    print(prod(largestBasins))


if __name__ == '__main__':
    main()
