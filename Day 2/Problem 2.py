def main():

    subDepth, subHorizontal, aim = 0, 0, 0

    with open('input.txt') as f:

        for line in f.readlines():

            subDir, val = line.strip().split()

            if subDir == "forward":
                subHorizontal += int(val)
                subDepth += aim * int(val)

            elif subDir == "up":
                aim -= int(val)

            else:
                aim += int(val)

    print(subHorizontal * subDepth)


if __name__ == '__main__':
    main()
