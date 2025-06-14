def mysearch(dictionaries):
    my_sum = 0
    for thing in dictionaries:
        if type(dictionaries[thing]) == int:
            # file
            my_sum += dictionaries[thing]
        else:
            # directory:
            my_sum += mysearch(dictionaries[thing])
    if my_sum <= 100000:
        print(my_sum)

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
                print("Current location stuff: ")
                print(loc)
        elif line.startswith("dir "):
            pass
        elif line.startswith("$ ls"):
            pass
        else:
            # TODO: add files here
            print(path)
            name = line.split(" ")[1]
            print(name)
            loc[name] = int(line.split(" ")[0])

    dir_counts = {x: 0 for x in parents}
    # DFS?
    print(mysearch(stuff))
