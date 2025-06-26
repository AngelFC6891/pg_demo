from constants import *
import json

def load_scores() -> list[dict]:
    with open(f'{SCORES}\{SCORES_CSV}', R, encoding=UTF) as file:
        scores = []

        for line in file:
            data = line.strip().split(COMMA_STR)
            user = {}
            user[NAME] = data[INT_0]
            user[SCORE] = data[INT_1]
            user[DATE] = data[INT_2]
            scores.append(user)

    return scores


scores = load_scores()

def add_user_data():

    with open(f'{SCORES}\{SCORES_JSON}', W, encoding=UTF) as file:
        json.dump(scores, file, indent=INT_4)

add_user_data()