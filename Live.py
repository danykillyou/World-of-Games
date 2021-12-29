import CurrencyRouletteGame
import MemoryGame
import GuessGame
def welcome(name):
    return f"""Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play."""


def digit_check(to_print, from_, to_):
    choice = input(to_print)
    while True:
        if not choice.isdigit():
            choice = input("Wrongly entered. try again\n")
        elif not from_ <= int(choice) <= to_:
            choice = input(f"enter number between {from_}-{to_}\n")
        else:
            break
    return choice


def load_game():
    play_again = "y"
    while play_again == "y":
        try:
            game_mode = digit_check("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""", 1, 3)
            game_level = digit_check("Please choose game difficulty from 1 to 5:\n", 1, 5)
            if game_mode == "1":
                GuessGame.play(int(game_level))
            elif game_mode == "2":
                MemoryGame.play(int(game_level))
            elif game_mode == "3":
                CurrencyRouletteGame.play(int(game_level))

        except ValueError:
            print("next time enter a number")
        except Exception as e:
            print(e)
        if input("Do you want to play again? enter y to play").lower() != "y":
            play_again = False
