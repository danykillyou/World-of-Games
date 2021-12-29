from random import randint


def generate_number(dif):
    num = randint(1, dif)
    return num


def get_guess_from_user():
    guess = int(input("enter your guess "))
    return guess


def compare_results(guess, generated_num):
    print(str(guess) + " guess")
    print(generated_num)
    return guess == generated_num


def play(dif):
    gen_num = generate_number(dif)
    guess = get_guess_from_user()
    print(compare_results(guess, gen_num))
    print(f"the generated number was {gen_num}")
