for row in range(0, 7):
    for col in range(0, 7):
        if col == 0 or col == 6:
            print("*", end="")
        elif row == 1 and (col == 1 or col == 5):
            print("*", end="")
        elif row == 2 and (col == 2 or col == 4):
            print("*", end="")
        elif row == col == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()