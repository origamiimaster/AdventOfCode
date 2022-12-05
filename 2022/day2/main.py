with open("puzzle.txt", "r") as f:
    input_text = f.read()

test = {
    ("A", "X"): 3 + 1,
    ("A", "Y"): 6 + 2,
    ("A", "Z"): 0 + 3,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 6 + 1,
    ("C", "Y"): 0 + 2,
    ("C", "Z"): 3 + 3,
}

score = 0

for line in input_text.split("\n")[:-1]:
    things = line.split(" ")
    opponent = things[0]
    you = things[1]
    score += test[(opponent, you)]

print(score)
