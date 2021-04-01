for row in range(7):
    for col in range(7):
        if (row - col == 3) or (row + col == 3) or col == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()