with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    count = 0
    prev = int(lines[0])
    for line in lines[1:]:
        # print(prev)
        # print(int(line))
        if int(line) > prev:
            count += 1
        prev = int(line)
print(count)


