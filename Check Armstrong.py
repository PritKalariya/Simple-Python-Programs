#Armstrong number is a number that is equal to the sum of cubes of its digits
def isArmstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        sum += rem**3
        temp //= 10

    if num == sum:
        print("Armstrong")
    else:
        print("Not armstrong")

isArmstrong(int(input("Enter to check for armstrong: ")))