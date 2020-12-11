import random
import emoji

print("="*15,"\N{WHITE RIGHT POINTING BACKHAND INDEX} NUMBER GUESSING GAME \N{WHITE LEFT POINTING BACKHAND INDEX}", "="*15)

number = random.randint(1, 9)
chances = 0
print("\n")
times = int(input("\N{BOMB} Enter how many chances you want: "))
print("\n")
print("GUESS A NUMBER (Between 1 to 9): ")

while chances < times:
    print("\n")
    guess = int(input("ENTER NUMBER: "))
    if guess == number:
        print("\n")
        print("="*10, "\N{party popper} HURRAY!! YOU WON!! \N{party popper}", "="*10)
        print("\n")
        break
    elif guess < number:
        print("\n")
        print(f"\t \N{CROSS MARK} Your guess is too low: Guess a higher number than {guess}")
        chances += 1
    else:
        print("\n")
        print(f"\t \N{CROSS MARK} Your guess is too high: Guess a lower number than {guess}")
        chances += 1
if not chances < times:
    print("\n")
    print("="*10, "\N{DISAPPOINTED FACE} OOPS! YOU LOOSE!! \N{DISAPPOINTED FACE}", "="*10)
    print("\n")
    print("*"*10, f"\N{EYES} The number was {number} \N{EYES}", "*"*10)
    print("\n")