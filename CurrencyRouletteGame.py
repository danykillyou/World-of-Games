from forex_python.converter import CurrencyRates
import random


def get_guess_from_user():
    return int(input("Enter your guess in ILS: "))


def get_money_interval(dif):
    currency = CurrencyRates()
    x = currency.get_rate('ILS', 'USD')
    rate = 1 / x
    print(f"1 USD is {rate} ILS")
    rand = random.randint(1, 101)
    the_num = round(rand * rate)
    print(f"The USD amount is {rand}$")
    guess = get_guess_from_user()
    print(f"The ILS was {the_num}")
    if the_num + dif - 5 <= guess <= the_num - dif + 5:
        return "you won!!!!"
    return "you lost"


def play_game(dif):
    # dif = int(input("Enter difficulty from 1 to 5:"))
    assert 1 <= dif <= 5, "wrong choice, next time enter difficulty from 1 to 5"
    print(get_money_interval(dif))

def play(dif):
    try:
        # play_again = "y"
        # while play_again == "y":
            play_game(dif)
             # if input("Do you want to play again? enter y to play").lower() != "y":
            #     play_again = False
    except ValueError as e:
        print("next time enter a number")
    except Exception as e:
        print(e)