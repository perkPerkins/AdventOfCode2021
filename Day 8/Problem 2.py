def main():

    lines = [line.split("|") for line in open('input.txt')]
    outputTotal = 0

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


        zero = [val for val in knownPanels.values() if val != knownPanels["mid"]]
        one = [knownPanels["topRight"], knownPanels["botRight"]]
        two = [val for val in knownPanels.values() if val != knownPanels["topLeft"] and val != knownPanels["botRight"]]
        three = [val for val in knownPanels.values() if val != knownPanels["topLeft"] and val != knownPanels["botLeft"]]
        four = [knownPanels["topLeft"], knownPanels["mid"], knownPanels["topRight"], knownPanels["botRight"]]
        five = [val for val in knownPanels.values() if val != knownPanels["topRight"] and val != knownPanels["botLeft"]]
        six = [val for val in knownPanels.values() if val != knownPanels["topRight"]]
        seven = [knownPanels["top"], knownPanels["topRight"], knownPanels["botRight"]]
        eight = list(knownPanels.values())
        nine = [val for val in knownPanels.values() if val != knownPanels["botLeft"]]

        zero.sort()
        one.sort()
        two.sort()
        three.sort()
        four.sort()
        five.sort()
        six.sort()
        seven.sort()
        eight.sort()
        nine.sort()

        outputNum = ""
        for num in output:
            num = [char for char in num]
            num.sort()

            if num == zero:
                outputNum += "0"
            elif num == one:
                outputNum += "1"
            elif num == two:
                outputNum += "2"
            elif num == three:
                outputNum += "3"
            elif num == four:
                outputNum += "4"
            elif num == five:
                outputNum += "5"
            elif num == six:
                outputNum += "6"
            elif num == seven:
                outputNum += "7"
            elif num == eight:
                outputNum += "8"
            elif num == nine:
                outputNum += "9"

        outputTotal += int(outputNum)

    print(outputTotal)

 
if __name__ == '__main__':
    main()
