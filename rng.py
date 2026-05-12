import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou will get chances to guess the correct number.")
number_to_guess = random.randint(1, 100)

print("Please select the difficulty level:\n1. Easy (10 chances) \n2. Medium (5 chances)\n3. Hard (3 chances)")
input_level = input("Enter 1, 2, or 3: ")
if input_level == '1':
    chances = 10
    print("You have chosen Easy mode. You have 10 chances to guess the number.")
elif input_level == '2':
    chances = 5
    print("You have chosen Medium mode. You have 5 chances to guess the number.")
else:
    chances = 3
    print("You have chosen Hard mode. You have 3 chances to guess the number.")
print("Let's begin!")
for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Make a guess: "))
    if guess < number_to_guess:
        print("Too low.")
    elif guess > number_to_guess:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempt} attempts!")
        break
    if attempt == chances:
        print(f"Sorry, you've used all your chances. The correct number was {number_to_guess}.")
    else:
        print("Try again.")


print("Game Over. Thank you for playing!")