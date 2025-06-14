with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
count = 0
max_pos = (None, None)
trees = [[int(x) for x in line] for line in lines]
stop = False
trees_transpose = [[trees[x][y] for x in range(len(trees))] for y in range(len(trees))]

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if stop:
            continue


        # Up
        flag = False
        up = 0
        for i in range(row):
            up += 1
            if not trees_transpose[col][row - i - 1] < trees[row][col]:
                break
        # if not flag and all(trees_transpose[col][row - i - 1] < trees[row][col] for i in range(row)):
        #     count += 1
        #     print(row, col)
        #     flag = True

        # Down
        down = 0
        for x in range(row + 1, len(lines)):
            down += 1
            if not trees_transpose[col][x] < trees[row][col]:
                break
        # if not flag and all(trees_transpose[col][x] < trees[row][col] for x in range(row + 1, len(lines))):
        #     count += 1
        #     print(row, col)
        #     flag = True

        # Left
        left = 0
        for i in range(col):
            left += 1
            if not trees[row][col - i - 1] < trees[row][col]:
                break
        # if not flag and all(trees[row][col - i - 1] < trees[row][col] for i in range(col)):
        #     count += 1
        #     print(row, col)
        #     flag = True

        # Right
        right = 0
        for x in range(col + 1, len(lines)):
            right += 1
            if not trees[row][x] < trees[row][col]:
                break
        # if not flag and all(trees[row][x] < trees[row][col] for x in range(col + 1, len(lines))):
        #     count += 1
        #     print(row, col)
        #     flag = True

        if count <= down * up * left * right:
            print(row, col)
            print(down, up, left, right)
            count = down * up * left * right
        # count = max(count, down * up * left * right)
print(count)
