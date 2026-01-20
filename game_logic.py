from ascci_art import STAGES
import random

WORDS = ["version", "python", "git", "github", "snowman", "meltdown", "bubble", "environment", "random"]

BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(BLUE + STAGES[mistakes] + RESET)

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += BLUE + letter + " " + RESET
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print(BLUE + "Welcome to Snowman Meltdown!" + RESET)

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes >= max_mistakes:
            print(RED + "You are too hot - GAME OVER! The snowman melted!" + RESET)
            print("The word was:", secret_word)
            break

        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False

        if word_guessed:
            print(BLUE + "You saved the snowman! ❄️" + RESET)
            break

        guess = input("Guess a letter: ").lower()

        # Input validation: only a single letter a-z
        if len(guess) != 1 or guess < "a" or guess > "z":
            print(RED + "Please enter ONE letter (a-z).\n" + RESET)
            continue

        if guess in guessed_letters:
            print(RED + "You already guessed that letter.\n" + RESET)
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(RED + "Wrong guess!\n" + RESET)
        else:
            print(BLUE + "Correct guess!\n" + RESET)
