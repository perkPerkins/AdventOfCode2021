def main():

    riskLevel = 0
    caveMap = [lines.strip() for lines in open('input.txt').readlines()]

    for y in range(len(caveMap)):

        for x in range(len(caveMap[y])):

            if y - 1 >= 0:
                if caveMap[y-1][x] <= caveMap[y][x]:
                    continue

            if y + 1 < len(caveMap):
                if caveMap[y+1][x] <= caveMap[y][x]:
                    continue

            if x - 1 >= 0:
                if caveMap[y][x-1] <= caveMap[y][x]:
                    continue

            if x + 1 < len(caveMap[y]):
                if caveMap[y][x+1] <= caveMap[y][x]:
                    continue

            riskLevel += int(caveMap[y][x]) + 1

    print(riskLevel)

if __name__ == '__main__':
    main()
