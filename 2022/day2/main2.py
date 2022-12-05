with open("puzzle.txt", "r") as f:
    input_text = f.read()

test = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1,
}

score = 0

for line in input_text.split("\n")[:-1]:
    things = line.split(" ")
    opponent = things[0]
    you = things[1]
    score += test[(opponent, you)]

print(score)
