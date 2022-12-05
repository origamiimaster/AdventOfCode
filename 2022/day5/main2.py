def remove_crate(col, count):
    removed = col[-1 * count:]
    col = col[:-1 * count:]
    return removed, col


def add_crate(col, crate):
    col += crate
    return col


with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
    cols = ["", "SPWNJZ", "TSG", "HLRQV",
            "DTSV", "JMBDTZQ", "LZCDJTWM",
            "JTGWMPL",
            "HQFBTMGN",
            "WQBPCGDR"]
    cols = [x[::-1] for x in cols]

    for line in lines:
        print(cols)
        # print([len(x) for x in cols])
        # print(line)
        how_many = int(line[5:line.index("from")])
        start = int(line[line.index("from") + 5: line.index(" to ")])
        end = int(line[line.index(" to ") + 4:len(line)])
        # for i in range(how_many):
        print(f"moving {how_many} from {start} to {end}")
        crate, col = remove_crate(cols[start], how_many)
        print(f"removed {crate}")
        cols[start] = col
        new_col = add_crate(cols[end], crate)
        print(f"added {crate}")
        cols[end] = new_col


    print("".join([x[-1] for x in cols[1:]]))
