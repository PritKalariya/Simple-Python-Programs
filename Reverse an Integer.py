def reverse(num):
    string = str(num)
    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])

num = reverse(input("Enter the number: "))
print(f"The reverse of the number is: {num}")