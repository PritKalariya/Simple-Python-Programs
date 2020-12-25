#Python program to check prime number
def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                print("Not prime.")
                break
        else:
            print("Prime number.")
    else:
        print("Not prime.")

isPrime(int(input("Enter number: ")))