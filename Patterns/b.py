for row in range(5):
    for col in range(3):
        if col == 0 or (col == 1) and (row == 0 or row == 2 or row == 4) or (col == 2) and (row == 1 or row == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()