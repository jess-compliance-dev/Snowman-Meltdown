from game_logic import play_game, BLUE, RESET

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print(BLUE + "Thanks for playing Snowman Meltdown! ❄️" + RESET)
            break

if __name__ == "__main__":
    main()
