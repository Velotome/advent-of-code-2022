input = open("D:\\Code\Advent-of-code-2022\Day 5\input.txt", "r")

def moveCrate(stacks, number_of_crate, start, end):
    if len(stacks[1 + 4*(int(start)-1)])-int(number_of_crate) > 0:
        for i in range(0,int(number_of_crate)-1):
            crates_to_move.append(stacks[1 + 4*(int(start)-1)].pop())
    
        for i in range(0,int(number_of_crate)-1):
            stacks[1 + 4*(int(end)-1)].append(crates_to_move.pop())

stacks = {}
crates_to_move = []

for line in input:
    #Parsing
    if '[' in line:
        for i in range(1,len(line)):
            if i%4 == 1:
                if i in stacks :
                    stacks[i].append(line[i])
                else:
                    stacks[i] = [line[i]]

    #moving crates
    elif "move" in line:
        line = line.replace("move", "").replace("from","").replace("to","").replace(" ","").replace("\n","")
        moveCrate(stacks, line[0], line[1], line[2])


print(stacks)
