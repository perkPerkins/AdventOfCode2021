def optimizeFuel(mid, crabs):
    return sum([abs(mid - x) for x in crabs])

def main():

    crabs = [int(crab) for crab in open('input.txt').readline().split(',')]
    crabs.sort()

    print(optimizeFuel(crabs[len(crabs) // 2], crabs))
    if len(crabs) % 2 == 0:
        print(optimizeFuel(crabs[(len(crabs) // 2) - 1], crabs))

if __name__ == '__main__':
    main()
