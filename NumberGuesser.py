import random

print("Welcome to the Number Guesser Game!")
print("I am thinking of a number between 22 and 31.")
print("You have to guess the number I am thinking of.")
print("You have 3 chances to guess the number.")
print("Let's start!")
random_number = random.randint(22, 31)

for i in range(3):
    guess = int(input("Enter your guess: "))
    if guess == random_number:
            print("Correct! You guessed the number in the " + str(i + 1) + " try!")
            exit()
    else: 
        if guess < random_number:
            print("Your guessed low.")
            print("lets try again.")
        else:
            print("You guessed high.")
            if i < 2:
                print("lets try again.")

print("The number I was thinking of was: " + str(random_number))