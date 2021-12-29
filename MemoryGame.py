import random
import sys
import time


def generate_sequence(dif):
    nums = random.sample(range(1, 101), dif)
    print(nums,end="")
    sys.stdout.flush()

    time.sleep(0.7)
    print("",end="\r")
    return nums


def get_list_from_user():
    user_nums = input("enter your guess:").split(",")
    user_nums = list(map(int, user_nums))
    return user_nums


def is_list_equal(user_nums, nums):
    return user_nums == nums


def play(dif):
    nums = generate_sequence(dif)
    user_nums = get_list_from_user()
    print(is_list_equal(user_nums, nums))
    print(f"the random sequence was: {nums}")

# play(2)
