def star_triangle(n):
    # Upper triangle
    for i in range(n):
        print((n - i - 1)*" ", end="")
        print((2 * i + 1)*"*")

    # Lower triangle
    for i in range(n - 1, -1, -1):
        print((n - 1 - i)*" ", end="")
        print((2 * i + 1)*"*")

star_triangle(5)