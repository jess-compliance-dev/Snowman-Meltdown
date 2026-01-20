import random

# List of secret words
WORDS = ["version", "python", "git", "github", "snowman", "meltdown", "bubble", "environment", "random"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
    """
]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the current word state."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Game loop (for now, will run until the snowman melts)
    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()


        guessed_letters.append(guess)

        mistakes += 1  # This is just to see snowman stages change

    # Final stage
    display_game_state(mistakes, secret_word, guessed_letters)
    print("You are too hot - GAME OVER! The snowman melted!")


if __name__ == "__main__":
    play_game()
