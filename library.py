import os
import json
import random
from datetime import date, datetime
import csv
import copy
from constants import *
import globals


def load_config(path : str, key : str) -> dict:
    config = {}
    
    with open(path, R, encoding=UTF) as file:
        data = json.load(file)
        config = data.get(key)
    
    return config


def load_scores(path : str) -> list[dict]:
    with open(f'{SCORES}\{path}', R, encoding=UTF) as file:
        scores = []

        for line in file:
            data = line.strip().split(COMMA_STR)
            user = {}
            user[NAME] = data[INT_0]
            user[SCORE] = data[INT_1]
            user[DATE] = format_date(data[INT_2])
            scores.append(user)

    return scores


def add_user_data(path : str, data : list):
    with open(f'{SCORES}\{path}', A, newline=VOID_STR, encoding=UTF) as file:
        writer = csv.writer(file)
        writer.writerow(data)


def format_date(date : str) -> str:
    date_obj = datetime.strptime(date, STANDAR_FORMAT)
    return date_obj.strftime(FORMAT)


def shuffle_questions(questions : dict[str, list]):
    for list in questions.values():
        random.shuffle(list)


def get_user_data():
    return [globals.get_username(), str(globals.get_score()), get_date()]


def get_date() -> str:
    return str(date.today())


def get_images(path : str) -> dict[str, pg.surface.Surface]:
    images = {}

    for file in os.listdir(path):
        name, _ = os.path.splitext(file)
        images[name] = pg.image.load(f'{path}\{file}')

    return images


def get_backgrounds() -> dict[str, pg.surface.Surface]:
    return get_images(f'{IMAGES}\{BACKGROUNDS}')


def get_questions() -> dict[str, list]:
    questions = {}

    for file_csv in os.listdir(QUESTIONS):
        questions_list = []

        with open(f'{QUESTIONS}\{file_csv}', R, encoding=UTF) as file:
            for line in file:
                data = line.split(',')
                question = {}
                question[QUESTION] = data[INT_0]
                question[INT_1] = data[INT_1]
                question[INT_2] = data[INT_2]
                question[INT_3] = data[INT_3]
                question[INT_4] = data[INT_4]
                question[ANSWER] = int(data[INT_5])
                questions_list.append(question)

        topic, _ = os.path.splitext(file_csv)
        questions[topic] = questions_list
    
    return questions


def get_buttons(config : dict) -> list[dict]:
    buttons = config.get(BUTTONS)

    for button in buttons:
        button[IMAGE] = pg.image.load(f'{IMAGES}/{BUTTONS}/{button.get(FILE)}')

    return buttons


def get_labels(config : dict) -> list[dict]:
    return config.get(LABELS)


def get_label_value(id : str) -> None | str:
    label_value = None

    if id == LIVES : label_value = str(globals.get_lives())
    elif id == TIME : label_value = str(globals.get_play_time())
    elif id == SCORE : label_value = str(globals.get_score())

    return label_value


def get_blocks(string : str, len_max : int) -> list[str]:
    words = string.split(SPACE_STR)
    blocks = []
    block = VOID_STR

    for i, word in enumerate(words):
        
        if block == VOID_STR:
            block = word
        else:
            block_aux = f'{block}{SPACE_STR}{word}'

            if len(block_aux) <= len_max:
                block = block_aux
                if i == len(words) - INT_1 : blocks.append(block)
            else:
                blocks.append(block)

                if not i == len(words) - INT_1:
                    block = word
                else:
                    blocks.append(word)

    return blocks


def get_font_color() -> tuple:
    font_color = WHITE

    if globals.get_avengers_on():
        font_color = YELLOW
    elif globals.get_simpsons_on():
        font_color = BLUE
    elif globals.get_starwars_on():
        font_color = WHITE
    elif globals.get_username_on():
        warning = globals.get_warning()

        if warning in [WARNING_MIN_MAX, WARNING_USE_LETTERS]:
            font_color = RED
        elif warning == WARNING_NAME_OK:
            font_color = GREEN

    return font_color


def set_question_win(is_win : bool, max_index : int):
    if is_win:
        score = globals.get_score()
        score += REWARD
        globals.set_score(score)
        set_question_pass(True, max_index)


def set_question_lost(is_lost : bool, max_index : int):
    lives = globals.get_lives()
    score = globals.get_score()

    if is_lost and not lives == INT_0:
        lives -= INT_1
        if not score == INT_0 : score -= PENALTY
        globals.set_lives(lives)
        globals.set_score(score)
        if not lives == INT_0 : set_question_pass(True, max_index)


def set_question_pass(is_pass : bool, max_index : int):
    if is_pass:
        next_question = globals.get_current_question() + INT_1

        if not next_question == max_index:
            globals.set_current_question(next_question)
            globals.set_play_time(PLAY_TIME)
        else:
            globals.set_questover_on(True)


def check_gameover(events : list[pg.event.Event]):
    lives = globals.get_lives()
    time = globals.get_gameover_delay()

    if lives == INT_0 or globals.get_questover_on():
        for e in events:
            if e.type == EVENT_1000MS:
                time -= INT_1
                globals.set_gameover_delay(time)

        if time == INT_0:
            globals.disable_instances()
            globals.set_gameover_on(True)


def sort_arrays(arrays : list[list], ascending : bool=True):
    array_ref = arrays[0]

    for i in range(len(array_ref)-INT_1):
        for j in range(i+INT_1, len(array_ref)):
            if (ascending and array_ref[i] > array_ref[j]) or (not ascending and array_ref[i] < array_ref[j]):
                array_ref[i], array_ref[j] = array_ref[j], array_ref[i]

                if len(arrays) > INT_1:
                    for k in range(INT_1, len(arrays)):
                        arrays[k][i], arrays[k][j] = arrays[k][j], arrays[k][i]


def sort_scores(scores : list[dict], ascending : bool):
    scores_list = [int(user.get(SCORE)) for user in scores]
    sort_arrays([scores_list, scores], ascending)


def copy_scores(scores : list[dict]):
    scores_copy = copy.deepcopy(scores)
    globals.set_scores_copy(scores_copy)


def get_user_scores(path : str):
    scores = load_scores(path)
    copy_scores(scores)
    sort_scores(globals.get_scores_copy(), ascending=False)

# ------------------------------------------------------------------------------------------- #

def is_letter(char : str) -> bool:
    output = True
    ascii = ord(char)
    
    if not (ascii >= 65 and ascii <= 90) and not (ascii >= 97 and ascii <= 122):
        output = False

    return output


def is_integer(string : str) -> bool:
    output = len(string) > INT_0
    
    for i in range(len(string)):
        ascii = ord(string[i])

        if i == INT_0 and ascii == INT_45:
            if len(string) > INT_1:
                continue
            else:
                output = False
                break
         
        if ascii < INT_48 or ascii > INT_57:
            output = False
            break
    
    return output