with open("inputs/day1.txt") as f:
    print(sum([abs(int(x.split("   ")[0]) - int(x.split("   ")[1]))
          for x in f.read().split("\n")]))
