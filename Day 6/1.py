input = open("D:\\Code\Advent-of-code-2022\Day 6\input.txt", "r")

marker = []
processed_char = 0
number_of_char = 4

for line in input:
    for char in line:
        processed_char += 1
        
        if char in marker:
            marker = []

        marker.append(char)

        if len(marker) == number_of_char:
            break

print(marker)
print(processed_char)