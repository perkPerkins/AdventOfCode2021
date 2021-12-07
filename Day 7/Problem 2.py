def optimizeFuel(target, crabs):
    return sum([(((abs(target - crab) ** 2) + abs(target - crab)) // 2) for crab in crabs])


def main():

    crabs = [int(crab) for crab in open('input.txt').readline().split(',')]
    print(optimizeFuel(int(round(sum(crabs) / len(crabs))) - 1, crabs))


if __name__ == '__main__':
    main()
