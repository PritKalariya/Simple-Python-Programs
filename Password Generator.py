import random

passlen = int(input("Enter the length of the Password:"))

s ="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p = "".join(random.sample(s,passlen))
print(p)