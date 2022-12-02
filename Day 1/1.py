elves = open("D:\\AdventOfCode2022\Day 1\Elves.txt", "r")
total = 0
biggest = 0

for food in elves:
    if food == "\n":
        if total > biggest:
            biggest = total
        total = 0
    else:
        total = total + int(food)

print(biggest)