with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    count = 0
    prev = int(lines[0]) + int(lines[1]) + int(lines[2])
    for i in range(len(lines) - 2):
        if int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) > prev:
            count += 1
        prev = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
print(count)


