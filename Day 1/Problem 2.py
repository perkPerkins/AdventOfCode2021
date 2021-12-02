def main():

    f = open('input.txt')
    counter = 0
    currentWindow = []
    windowSize = 3

    for line in f:

        currentWindow.append(int(line))

        if len(currentWindow) > windowSize:

            prev = sum(currentWindow[:-1])
            currentWindow.pop(0)
            counter += 1 if sum(currentWindow) > prev else 0

    print(counter)


if __name__ == '__main__':
    main()
