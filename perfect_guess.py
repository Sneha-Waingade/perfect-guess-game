import random

print("Welcome to Perfect Guees Game 🧠")
print("Choose the difficulty level:")
print("1. Easy: (15 guesses)")
print("2. Medium: (10 guesses)")
print("3. Hard: (3 guesses)")

choice = input("Enter your choice: ")

if choice == "1":
    guesses = 15
elif choice == "2":
    guesses = 10
elif choice == "3":
    guesses = 3
else:
    print("Invalid Choice.Defaulting to medium level difficulty.")
    guesses = 10

computer = random.randint(0, 101)

i = 0
for i in range(1, guesses+1):
    user = int(input("Enter a number: "))

    if user > computer:
        print("Lower number please.Possibly <=100")
        print(f"Try again.You have {guesses-i} guesses left")

    elif user < computer:
        print("Higher number please.Possibly >=0")
        print(f"Try again.You have {guesses-i} guesses left")

    else:
        print(
            f"😎 🤩 🤩 You guessed right!\nNumber of guesses used to arrive at the number: {i}")
        break
else:
    print(
        f"😢 Out of guesses.\nThe number was {computer}.Better luck next time🤗")
