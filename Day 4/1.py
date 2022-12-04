input = open("D:\\Code\Advent-of-code-2022\Day 4\\input.txt", "r")
total = 0

"""
#From 1-4 to 1234
def rangeStr(start, finish):
    result = []
    for i in range(start, finish):
        result.append(str(i))
    result = ''.join(result)
    return result

for pairs in input:
    section = []
    pairs = pairs.replace('\n','').replace('-',',').split(',')
    section.append(rangeStr(int(pairs[0]), int(pairs[1])))
    section.append(rangeStr(int(pairs[2]), int(pairs[3])))

    if (section[0] in section[1]) or (section[1] in section[0]):
        total +=1
"""

for pairs in input:
    pairs = [section for section in pairs.replace('\n','').replace('-',',').split(',')]
    if ((pairs[0] >= pairs[2]) and (pairs[1] <= pairs[3])) or ((pairs[2] >= pairs[0]) and (pairs[3] <= pairs[1])):
        total +=1

print("\n" + str(total))

#522 goal
