for row in range(0, 7):
    for col in range(0, 7):
        if ((col == 1 or col == 5) and row != 6) or (row == 6 and col > 1 and col < 5):
            print("*", end="")
        else:
            print(" ", end="")
    print()