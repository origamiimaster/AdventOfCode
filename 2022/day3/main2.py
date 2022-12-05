total = 0
priorities = " abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()

with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    for i in range(0, len(lines), 3):
        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                total += priorities.index(char)
                break

print(total)
