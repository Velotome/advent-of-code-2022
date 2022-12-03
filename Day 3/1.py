import string

bags = open("D:\\Code\Advent-of-code-2022\Day 3\\input.txt", "r")

#Making a list with each lowercase letter and each uppercase letter to match them with a value which is the index + 1
item_value = list(string.ascii_lowercase + string.ascii_uppercase)
total = 0

for bag in bags:
    #split bag in 2 compartments
    bag_size = len(bag)
    compartment1 = set([bag[i] for i in range(0,bag_size//2)])
    compartment2 = set([bag[i] for i in range(bag_size//2,bag_size-1)])

    #Find item in both compartment and add its value to total
    total += item_value.index(list(compartment1.intersection(compartment2))[0]) + 1

print(total)
