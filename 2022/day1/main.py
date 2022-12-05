with open("puzzle.txt", "r") as f:
    text = f.read()

value_list = []
for elf in text.split("\n\n"):
    print(elf)
    values = elf.split("\n")
    total = sum(int(value) for value in values if value != "")
    value_list.append(total)

value_list.sort()
value_list.reverse()
print("Results:")
print(value_list[0]+value_list[1]+value_list[2])
