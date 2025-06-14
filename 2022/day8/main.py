with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
count = 0
trees = [[int(x) for x in line] for line in lines]
stop = False
trees_transpose = [[trees[x][y] for x in range(len(trees))] for y in range(len(trees))]

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if stop:
            continue

        if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines[0]) - 1:
            count += 1
            # print(row, col)
        else:
            # Not an interior one:
            # Up
            flag = False
            if not flag and all(trees_transpose[col][row - i - 1] < trees[row][col] for i in range(row)):
                count += 1
                print(row, col)
                flag = True

            # Down
            if not flag and all(trees_transpose[col][x] < trees[row][col] for x in range(row + 1, len(lines))):
                count += 1
                print(row, col)
                flag = True

            # Left
            if not flag and all(trees[row][col - i - 1] < trees[row][col] for i in range(col)):
                count += 1
                print(row, col)
                flag = True

            # Right
            if not flag and all(trees[row][x] < trees[row][col] for x in range(col + 1, len(lines))):
                count += 1
                print(row, col)
                flag = True


print(count)
