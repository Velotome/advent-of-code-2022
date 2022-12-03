elves = open("D:\\Code\Advent-of-code-2022\Day 1\Elves.txt", "r")
total = 0
top3 = [0,0,0]
mintop3 = 0

for food in elves:
    if food == "\n":
        mintop3 = min(top3)
        if total > mintop3:
            top3[top3.index(mintop3)] = total
        total = 0
    else:
        total = total + int(food)

print(sum(top3))