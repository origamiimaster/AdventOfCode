DISK_SPACE = 44376732
TOTAL_SIZE = 70000000
REQUIRED = 30000000
NEED_TO_RM = DISK_SPACE - REQUIRED
file_values = []

def mysearch(dictionaries):
    my_sum = 0
    for thing in dictionaries:
        if type(dictionaries[thing]) == int:
            # file
            my_sum += dictionaries[thing]
        else:
            # directory:
            my_sum += mysearch(dictionaries[thing])

    file_values.append(my_sum)
    return my_sum

def get_cur_loc(x):
    temp = stuff
    for a in x:
        temp = temp[a]
    return temp


with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    parents = {"/": set()}
    cur_path = ["/"]
    files = {}
    stuff = {"/": {}}
    loc = get_cur_loc(cur_path)

    for line in lines:
        if line.startswith("$ cd"):
            path = line[line.index("cd") + 3:]
            if path == "/":
                cur_path = ["/"]
                loc = get_cur_loc(cur_path)
            elif path == "..":
                cur_path = cur_path[:-1]
                loc = get_cur_loc(cur_path)
            else:
                if path not in loc:
                    loc[path] = {}
                cur_path.append(path)
                loc = get_cur_loc(cur_path)

        elif line.startswith("dir "):
            pass
        elif line.startswith("$ ls"):
            pass
        else:

            name = line.split(" ")[1]
            loc[name] = int(line.split(" ")[0])

    mysearch(stuff["/"])
