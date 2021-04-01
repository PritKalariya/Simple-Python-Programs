for row in range(5):
    for col in range(3):
        if (row == 0 and col == 0) or (row ==4 and col == 0):
            print(" ", end="")
        elif row == 0 or row == 4 or col == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()