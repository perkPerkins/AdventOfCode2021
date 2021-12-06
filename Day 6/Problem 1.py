def main():

    totalDays = 256
    newFishTimer = {n: [] for n in range(0, totalDays + 1)}
    newFishTimer[0] = [int(n) for n in open('input.txt').readline().split(',')]
    
    for n in range(0, totalDays):
        
        for daysToNewFish in newFishTimer[n]:

            reproductionDay = n + daysToNewFish + 1
            while reproductionDay <= totalDays:

                newFishTimer[reproductionDay].append(8)  # new fish
                reproductionDay += 7

            newFishTimer[totalDays].append(reproductionDay - totalDays - 1)

        print(n)

    print(len(newFishTimer[totalDays]))


if __name__ == '__main__':
    main()
