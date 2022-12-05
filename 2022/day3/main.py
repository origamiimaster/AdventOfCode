total = 0
priorities = " abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()

with open("puzzle.txt", "r") as f:
    for line in f.read().split("\n")[:-1]:
        i = len(line) // 2
        c1 = line[:i]
        c2 = line[i:]
        # print(line)
        for item in c1:
            if item in c2:
                # print(item)
                # print(priorities.index(item))
                total += priorities.index(item)
                break

print(total)
