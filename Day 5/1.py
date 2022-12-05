input = open("D:\\Code\Advent-of-code-2022\Day 5\input.txt", "r")
total = 0

stacks = []
#Parsing
for line in input:
    if '[' in line:
        line.replace('[','').replace(']','').replace(' ','')
        print(line)

    