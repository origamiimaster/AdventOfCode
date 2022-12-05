total = 0
with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    for line in lines:
        a = line.split(",")[0]
        b = line.split(",")[1]
        a_range = [x for x in range(int(a.split('-')[0]), int(a.split('-')[1]) + 1)]
        b_range = [x for x in range(int(b.split('-')[0]), int(b.split('-')[1]) + 1)]

        for x in a_range + b_range:
            if x in a_range and x in b_range:
                total += 1
                break

print(total)
