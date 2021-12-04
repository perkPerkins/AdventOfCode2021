def findCO2OrO2(remainingNums, bitCriteria, currentBit):

    if len(remainingNums) == 1:
        return int("".join(str(x) for x in remainingNums), 2)

    oneBits, zeroBits = [], []

    for line in remainingNums:
        oneBits.append(line.strip()) if int(line[currentBit]) == 1 else zeroBits.append(line.strip())

    if bitCriteria == ">":
        return findCO2OrO2(oneBits, bitCriteria, currentBit + 1) if len(oneBits) >= len(zeroBits) else findCO2OrO2(zeroBits, bitCriteria, currentBit + 1)

    else:
        return findCO2OrO2(zeroBits, bitCriteria, currentBit + 1) if len(zeroBits) <= len(oneBits) else findCO2OrO2(oneBits, bitCriteria, currentBit + 1)


def main():

    f = open('input.txt')
    lines = f.readlines()
    print(findCO2OrO2(lines, "<", 0) * findCO2OrO2(lines, ">", 0))


if __name__ == '__main__':
    main()
