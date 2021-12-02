def main():

    f = open('input.txt')
    counter = 0
    prev = int(f.readline())

    for line in f:

        counter += 1 if int(line) > prev else 0
        prev = int(line)

    print(counter)


if __name__ == '__main__':
    main()
