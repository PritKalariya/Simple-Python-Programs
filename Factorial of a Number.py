#Python program for factorial of a number
def fact(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fac = 1
        while(num > 1):
            fac = fac * num
            num = num - 1
        return fac

num = fact(int(input("Enter number: ")))
print(f"The factorial of the number is: {num}")