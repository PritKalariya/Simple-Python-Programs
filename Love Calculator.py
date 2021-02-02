print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

combined_name = cn = name1 + name2

t = cn.count("t")
r = cn.count("r")
u = cn.count("u")
e = cn.count("e")
true = t + r + u + e

l = cn.count("l")
o = cn.count("o")
v = cn.count("v")
e = cn.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")