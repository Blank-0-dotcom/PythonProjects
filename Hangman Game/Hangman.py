import random
import string
from words import words
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # A~Z
    used_letters = set()  # alphabet guessed by user

    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print(
            "You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        # print("Current word: ", " ".join(word_list))
        # Current word:  - - - -
        # print("Current word: ", word_list)
        # Current word:  ['-', '-', '-', '-', '-', '-']

        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Your letter", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try other letters.")
        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was ", word, ".")
    else:
        print("YAY! You guessed the word", word, "!!")


hangman()
