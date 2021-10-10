import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > x:
            print(f"ERROR! Your guess exceeded the limit {x}!")
        elif guess < 1:
            print(f"ERROR! Your guess is less than 1!")
        elif guess == x or guess == 1:
            print(f"Please guess a number between 1 and {x}!")
        else:
            if guess < random_number:
                print("Sorry, guess again. Too low!")
            elif guess > random_number:
                print("Sorry, guess again. Too high!")
    print(f"Jackpot! You have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    number = int(input("Please choose a random number between 1~10000."))
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct(C)?? Your number: {number}. ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer have guessed your number {guess} correctly!")


guess(10000)
computer_guess(10000)
