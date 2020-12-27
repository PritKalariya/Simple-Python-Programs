def rev_pattern(n):
    for i in range(n, 0, -1):
        for j in range(0, n-i):
            print(end=" ")

        for j in range(0, i):
            print("*", end=" ")
            
        print("\r")

rev_pattern(5)