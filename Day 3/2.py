import string

bags = open("D:\\Code\Advent-of-code-2022\Day 3\\input.txt", "r").readlines()
item_value = list(string.ascii_lowercase + string.ascii_uppercase)
total = 0

for i in range(0, len(bags), 3):

    bag1 = set([item for item in bags[i] if item != "\n"])
    bag2 = set([item for item in bags[i+1] if item != "\n"])
    bag3 = set([item for item in bags[i+2] if item != "\n"])

    id = bag1.intersection(bag2).intersection(bag3)
    print(id)

    total += item_value.index(list(id)[0]) + 1

print(total)
