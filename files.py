from constants import *
import json


# CODIGO DE RESPALDO EN CASO DE ESCRITURA FALLIDA DEL ARCHIVO JSON

# def load_scores_csv() -> list[dict]:
#     with open(f'{SCORES}\{SCORES_CSV}', R, encoding=UTF) as file:
#         scores = []

#         for line in file:
#             data = line.strip().split(COMMA_STR)
#             user = {}
#             user[NAME] = data[INT_0]
#             user[SCORE] = data[INT_1]
#             user[DATE] = data[INT_2]
#             scores.append(user)

#     return scores


# def write_scores_json():
#     with open(f'{SCORES}\{SCORES_JSON}', W, encoding=UTF) as file:
#         json.dump(scores, file, indent=INT_4)


# scores = load_scores_csv()
# write_scores_json()