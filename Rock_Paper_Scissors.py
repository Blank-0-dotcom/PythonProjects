import random


def play():
    win = 0
    lose = 0
    draw = 0
    print("Welcome to Rock-Paper-Scissors Game! Win twice before your opponent to win the Game!")
    while win < 2 and lose < 2:
        Total = win+lose+draw
        print(f"Game {Total+1}!")
        user = input(
            "What's Your Choice? 'r' for rock. 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            draw += 1
            print(f"{user} vs {computer}. It's a draw! Current Score {win}:{lose}!")

        elif is_win(user, computer):
            win += 1
            print(f"{user} vs {computer}. You won! Current Score {win}:{lose}!")

        elif is_win(computer, user):
            lose += 1
            print(f"{user} vs {computer}. You lose! Current Score {win}:{lose}!")
        else:
            print("ERROR! Invalid Input!")
    if win == 2:
        print(f"{win}:{lose}. CONGRATULATION!")
    elif lose == 2:
        print(f"{win}:{lose}. Try Again! :(")

    again = input("Play again? (y/n): ")
    while again != "y" and again != "n":
        print("ERROR! Invalid Input")
        again = input("Play again? (y/n): ")
    if again == "y":
        play()
    else:
        print("Thanks for playing!")


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


play()
