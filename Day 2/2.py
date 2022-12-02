strat = open("D:\\AdventOfCode2022\Day 2\strat.txt", "r")
total = 0
point = 0

for line in strat:
    match line:
        case "A X\n":
            point = 3
        case "A Y\n":
            point = 4
        case "A Z\n":
            point = 8
        case "B X\n":
            point = 1
        case "B Y\n":
            point = 5
        case "B Z\n":
            point = 9
        case "C X\n":
            point = 2
        case "C Y\n":
            point = 6
        case "C Z\n":
            point = 7
    print(str(total) + " + " + str(point))
    total = total + point

print(total)