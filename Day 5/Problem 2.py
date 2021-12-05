def getLineSegment(x1, y1, x2, y2):

    dx = bool(x2 > x1) - bool(x2 < x1)
    dy = bool(y2 > y1) - bool(y2 < y1)
    return [(x1 + n * dx, y1 + n * dy) for n in range(max(abs(x2 - x1), abs(y2 - y1)) + 1)]


def main():

    coordinateDict = set()  # stores coordinates hit. If coord already hit, add to overlap
    overlap = set()
    lines = [[int(num) for xy in line.split(' -> ') for num in xy.split(',')]
             for line in open('input.txt')]

    for line in lines:

        for coord in getLineSegment(*line):

            if coord in coordinateDict:
                overlap.add(coord)
            else:
                coordinateDict.add(coord)

    print(len(overlap))


if __name__ == '__main__':
    main()
