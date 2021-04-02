for row in range(5):
    for col in range(3):
        if col == 0 or row == 2 or row == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()