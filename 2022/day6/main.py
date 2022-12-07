with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    line = lines[0]
    for i in range(len(lines[0]) - 13):
        if len(line[i:i+4]) == len(set(line[i:i+4])):
            print(i + 4)
            break
