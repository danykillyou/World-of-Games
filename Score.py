from Utils import SCORES_FILE_NAME


def add_score(diff):

    with open(SCORES_FILE_NAME,'a+') as f:
        f.seek(0)
        score = f.read()
        print(score)
        if score != "":
            print("ccc")
            open(SCORES_FILE_NAME, 'w').close()
            f.write(str(int(score)+(diff*3)+5))
        else:
            f.write(str((diff*3)+5))

