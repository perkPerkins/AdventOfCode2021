def main():

    with open('input.txt') as f:

        bitCount = [int(bit) for bit in f.readline().strip()]
        numLines = 1

        for line in f.readlines():

            numLines += 1

            for i in range(len(line.strip())):
                bitCount[i] += int(line[i])

        gamma = [1 if x > numLines // 2 else 0 for x in bitCount]
        epsilon = [1 if x == 0 else 0 for x in gamma]

        print(int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in epsilon), 2))


if __name__ == '__main__':
    main()
