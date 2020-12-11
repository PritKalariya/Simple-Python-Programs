#Palindrome is something that read forwards or backwords is the same.
def isPalindrome(s):
    if(s == s[::-1]):
        print("Pladindrome")
    else:
        print("Not palindrome")

isPalindrome(input("Enter to check for palindrome: "))