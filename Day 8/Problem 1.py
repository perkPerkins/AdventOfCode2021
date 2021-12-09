def main():

    lines = [line.split("|") for line in open('input.txt')]
    uniqueNums = 0

    for line in lines:
        knownPanels = {}
        midBotPanels = []
        input, output = line[0].strip().split(), line[1].strip().split()
        one, four, seven, eight = "", "", "", ""

        # find numbers w unique number of panels
        for num in input:
            if len(num) == 2:
                one = num
            elif len(num) == 4:
                four = num
            elif len(num) == 3:
                seven = num
            elif len(num) == 7:
                eight = num

        # look at 7 and 1, find top
        for char in seven:
            if char not in one:
                knownPanels["top"] = char

        # look at 3, find mid and bot
        for num in input:         # if this is true, we know the number is 3
            if knownPanels["top"] in num and one[0] in num and one[1] in num and len(num) == 5:
                for char in num:
                    if char not in knownPanels["top"] and char not in one:
                        midBotPanels.append(char)

        # look at 4, find topLeft and mid
        for char in four:
            if char not in one and char not in midBotPanels:
                knownPanels["topLeft"] = char
            elif char not in one and char in midBotPanels:
                knownPanels["mid"] = char

        # look at 5, find bot, botRight, and topRight
        for num in input:       # if this is true, we know the number is 5
            if knownPanels["top"] in num and knownPanels["topLeft"] in num and knownPanels["mid"] in num and len(num) == 5:
                for char in num:
                    if char not in knownPanels.values() and char not in one:
                        knownPanels["bot"] = char
                    if char not in knownPanels.values() and char in one:
                        knownPanels["botRight"] = char
                        knownPanels["topRight"] = one[0] if one[0] != char else one[1]

        # look at 8, find botLeft
        for char in eight:
            if char not in knownPanels.values():
                knownPanels["botLeft"] = char

        for num in output:
            if len(num) in [2, 3, 4, 7]:
                uniqueNums += 1

    print(uniqueNums)


if __name__ == '__main__':
    main()
