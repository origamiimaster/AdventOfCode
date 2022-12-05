total = 0
with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    for line in lines:
        a = line.split(",")[0]
        b = line.split(",")[1]
        if int(a.split("-")[0]) <= int(b.split("-")[0]) and int(a.split("-")[1]) >= int(b.split("-")[1]):
            total += 1
            continue
        a, b = b, a
        if int(a.split("-")[0]) <= int(b.split("-")[0]) and int(a.split("-")[1]) >= int(b.split("-")[1]):
            total += 1
            continue
print(total)
