def main():
    f = open('input.txt')
    numbersToBoardNum = {}  # key: number being called. value: list of boards that have that number
    boardBingoTracker = {}  # key: board number. value: tuple of two lists that track row, col counts
    numsCalledEachBoard = {}  # key: board number. value: list of numbers called on that board
    boards = []  # index acts as key. Key: board number. value: dictionary. dict key: numbers on board. value: num coord

    numbersCalled = [x.strip() for x in f.readline().split(',')]
    boardNum = -1
    row, col = 0, 0

    for line in f.readlines():

        if line == '\n':

            boardNum += 1
            boards.append({})
            boardBingoTracker[boardNum] = ([0] * 5, [0] * 5)  # bad practice but the alternative is ugly
            numsCalledEachBoard[boardNum] = set()
            row, col = 0, 0

        else:

            for num in line.split():

                num = num.strip()
                boards[boardNum][num] = [row, col]

                if numbersToBoardNum.get(num) is None:
                    numbersToBoardNum[num] = [boardNum]

                else:
                    numbersToBoardNum[num].append(boardNum)

                col += 1

            row += 1
            col = 0

    winningNum = -1
    winningBoard = 0
    for num in numbersCalled:

        for board in numbersToBoardNum[num]:

            coords = boards[board][num]
            boardBingoTracker[board][0][coords[0]] += 1
            boardBingoTracker[board][1][coords[1]] += 1
            numsCalledEachBoard[board].add(num)

            if 5 in boardBingoTracker[board][0] or 5 in boardBingoTracker[board][1]:

                winningNum = int(num)
                winningBoard = board
                break

        if winningNum != -1:
            break

    unmarkedSum = 0  # nums not called on winning board
    for num in boards[winningBoard].keys():

        if num not in numsCalledEachBoard[winningBoard]:
            unmarkedSum += int(num)

    print(unmarkedSum * winningNum)


if __name__ == '__main__':
    main()
