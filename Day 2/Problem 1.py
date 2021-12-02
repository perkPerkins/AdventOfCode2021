def main():

    subDepth, subHorizontal = 0, 0

    with open('input.txt') as f:

        for line in f.readlines():

            dir, val = line.strip().split()

            if dir == "forward":
                subHorizontal += int(val)

            elif dir == "up":
                subDepth -= int(val)

            else:
                subDepth += int(val)

    print(subDepth * subHorizontal)


if __name__ == '__main__':
    main()
