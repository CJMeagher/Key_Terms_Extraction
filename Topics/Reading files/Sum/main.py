with open("sums.txt", "r") as sums:
    for line in sums:
        print(sum(map(int, line.split())))
