import os

SCORES_FILE_NAME = r"C:\Users\Ofer\PycharmProjects\WorldOfGames\Scores.txt"
BAD_RETURN_CODE = 200


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
