import random

print("="*15,"NUMBER GUESSING GAME", "="*15)

number = random.randint(1, 9)
chances = 0
print("-"*52)
times = int(input("Enter how many chances you want: "))
print("-"*52)
print("GUESS A NUMBER (Between 1 to 9): ")

while chances < times:
    guess = int(input("ENTER NUMBER: "))
    if guess == number:
        print("="*10, "HURRAY!! YOU WON!! :)", "="*10)
        break
    elif guess < number:
        print(f"Your guess is too low: Guess a higher number than {guess}")
        chances += 1
    else:
        print(f"Your guess is too high: Guess a lower number than {guess}")
        chances += 1
if not chances < times:
    print("="*10, "OOPS! YOU LOOSE!! :(", "="*10)
    print("*"*10, f"The number was {number}", "*"*10)