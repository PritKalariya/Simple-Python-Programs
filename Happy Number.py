def isHappyNumber(num):
    rem = sum = 0
    while(num > 0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10
    return sum

num = 19
result = num

while(result != 1 and result != 4):
    result = isHappyNumber(result)

if(result == 1):
    print("Happy number 😄")
elif(result == 4):
    print("Sad Number 😟")