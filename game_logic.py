from ascci_art import STAGES
import random

WORDS = ["version", "python", "git", "github", "snowman", "meltdown", "bubble", "environment", "random"]

def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print()

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes >= max_mistakes:
            print("You are too hot - GAME OVER! The snowman melted!")
            print("The word was:", secret_word)
            break

        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False

        if word_guessed:
            print("You saved the snowman! ❄️")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct guess!\n")
        else:
            guessed_letters.append(guess)
            mistakes = mistakes + 1
            print("Wrong guess!\n")

if __name__ == "__main__":
    play_game()
