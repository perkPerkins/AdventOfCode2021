data = [int(x) for x in open("input.txt").read().strip().split(',')]


def countFish(d, k):

    fishCount = [d.count(i) for i in range(9)]

    for s in range(k):

      newFish = fishCount[0]
      fishCount[0:8] = fishCount[1:9]
      fishCount[6] += newFish
      fishCount[8] = newFish

    return sum(fishCount)


print(countFish(data, 256))
