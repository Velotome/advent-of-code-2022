strat = open("D:\\Code\Advent-of-code-2022\Day 2\strat.txt", "r")
total = 0
point = 0

for line in strat:
    match line:
        case "A X\n":
            point = 4
        case "A Y\n":
            point = 8
        case "A Z\n":
            point = 3
        case "B X\n":
            point = 1
        case "B Y\n":
            point = 5
        case "B Z\n":
            point = 9
        case "C X\n":
            point = 7
        case "C Y\n":
            point = 2
        case "C Z\n":
            point = 6
    print(str(total) + " + " + str(point))
    total = total + point

print(total)