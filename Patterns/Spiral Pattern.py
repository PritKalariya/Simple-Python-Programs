def spiral_pattern(n):
    a = 2*n-1

    for i in range(1, a+1):
        for j in range(1, a+1):
            print(max(abs(i-n), abs(j-n))+1, end="")
        print()

spiral_pattern(5)