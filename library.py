import os
import json
import random
from datetime import date, datetime
import copy
from typing import Callable
from constants import *
import globals
import sound


def load_config(path : str, key : str) -> dict:
    config = {}
    
    with open(path, R, encoding=UTF) as file:
        data = json.load(file)
        config = data.get(key)
    
    return config


def load_scores(path : str) -> list[dict]:
    users = []

    with open(f'{SCORES}\{path}', R, encoding=UTF) as file:
        users = json.load(file)

    return users


def add_user_data(path : str, user_data : dict):
    scores = globals.get_scores_list()
    scores.append(user_data)

    with open(f'{SCORES}\{path}', W, encoding=UTF) as file:
        json.dump(scores, file, indent=INT_4)


def format_date(date : str, input_standar : bool=True) -> str:
    if input_standar:
        input_f, output_f = STANDAR_FORMAT, FORMAT
    else:
        input_f, output_f = FORMAT, STANDAR_FORMAT

    date_obj = datetime.strptime(date, input_f)
    return date_obj.strftime(output_f)


def shuffle_questions(questions : dict[str, list]):
    for list in questions.values():
        random.shuffle(list)


def get_user_data():
    return\
    {
        NAME: globals.get_username(),
        SCORE: str(globals.get_score()),
        DATE: get_date()
    }


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
                data = line.split(COMMA_STR)
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


def get_buttons(config : dict) -> dict[str, list]:
    buttons = config.get(BUTTONS)
    buttons_dict = {}

    for button in buttons:
        button[IMAGE] = pg.image.load(f'{IMAGES}/{BUTTONS}/{button.get(FILE)}')
    
    for key, value in INSTANCES_BUTTONS.items():
        buttons_dict[key] = [button for button in buttons if button.get(ID) in value]

    return buttons_dict


def get_labels(config : dict, instance : str) -> list[dict]:
    labels_dict = config.get(LABELS)

    if instance == GAME:
        labels = labels_dict.get(GAME_LABELS)
    elif instance == SETTINGS:
        labels = labels_dict.get(SETTINGS_LABELS)
    elif instance == DIFFICULTY:
        labels = labels_dict.get(DIFFICULTY_LABELS)
    elif instance == CONTINUE:
        labels = labels_dict.get(CONTINUE_LABELS)

    return labels


def get_items(config : dict, instance : str) -> dict[str, dict]:
    items = config.get(ITEMS)

    if instance == GAME:
        instance_items = items.get(GAME_ITEMS)

        for item in instance_items.values():
            item[IMAGE] = pg.image.load(f'{IMAGES}/{ITEMS}/{item.get(FILE)}')

    return instance_items


def get_label_value(id : str, max_index : int=0) -> None | str:
    value = None

    if globals.get_game_on():
        if id == NUMBER : value = f'{(globals.get_current_question()+INT_1)}{SLASH_STR}{max_index}'
        elif id == LIVES : value = str(globals.get_lives())
        elif id == TIME : value = str(globals.get_play_time())
        elif id == SCORE : value = str(globals.get_score())
    
    elif globals.get_settings_on():
        if id == VOL_MUSIC:
            vol_music = int(globals.get_vol_music() * INT_100)
            value = f'{vol_music}{PERCENT_STR}'

        elif id == VOL_EFFECTS:
            vol_effects = int(globals.get_vol_effects() * INT_100)
            value = f'{vol_effects}{PERCENT_STR}'

    elif globals.get_difficulty_on():
        if id == PLAY_TIME : value = str(globals.get_play_time_init())
        elif id == LIVES : value = str(globals.get_lives_init())
        elif id == PENALTY : value = str(globals.get_penalty())

    elif globals.get_continue_on():
        if id == CONTINUE_COUNTDOWN : value = str(globals.get_continue_time())

    return value


def get_music(config : dict) -> dict[str, dict]:
    music_list = config.get(MUSIC)
    music_dict = {}

    for music in music_list:
        music_dict[music.get(ID)] = {key: value for key,value in music.items() if not key == ID}
    
    return music_dict


def get_effects(config : dict):
    effects = {}

    for effect in config.get(EFFECTS):
        effect[EFFECT] = pg.mixer.Sound(f'{SOUNDS}/{effect.get(FILE)}')
        effect_id = effect.get(ID)
        effect_key = effect_id.replace(f'{LOW_HYPHEN_STR}{EFFECT}', VOID_STR)
        effects[effect_key] = effect

    globals.set_effects(effects)


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
    
    if globals.get_game_on():

        if globals.get_avengers_on():
            font_color = YELLOW
        elif globals.get_simpsons_on():
            font_color = BLUE
        elif globals.get_starwars_on():
            font_color = WHITE

    elif globals.get_difficulty_on():
        font_color = GREEN_CAKE
    
    elif globals.get_username_on():
        warning = globals.get_warning()

        if warning in [WARNING_MIN_MAX, WARNING_USE_LETTERS]:
            font_color = RED
        elif warning == WARNING_NAME_OK:
            font_color = GREEN

    elif globals.get_settings_on():
        font_color = CAKE

    elif globals.get_continue_on():
        font_color = YELLOW_CAKE

    return font_color


def get_font_sys() -> pg.font.Font:
    if globals.get_game_on():
        font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_LAB, BOLD_ENABLE)
    elif globals.get_settings_on():
        font_sys = pg.font.SysFont(FONT_MV_BOLI, FONT_SIZE_VOLUME, BOLD_ENABLE)
    elif globals.get_difficulty_on():
        font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_VOLUME, BOLD_ENABLE)
    elif globals.get_continue_on():
        font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_COUNTDOWN, BOLD_ENABLE)

    return font_sys


def get_user_answer(pos : tuple, question : dict, update_options : Callable) -> int | None:
    update_options(question)
    user_answer = None
    options_render = question.get(OPTIONS_RENDER)
    y = Y_INIT_OPT

    for i, option_render in enumerate(options_render):
        rect = option_render.get_rect()
        rect.x = X_INIT_OPT
        rect.y = y

        if rect.collidepoint(pos):
            user_answer = i + INT_1

        y += Y_VAR

    return user_answer


def set_difficulty_game():
    if globals.get_easy_on():
        play_time, lives, penalty = EASY
        
    elif globals.get_middle_on():
        play_time, lives, penalty = MIDDLE

    elif globals.get_hard_on():
        play_time, lives, penalty = HARD

    globals.set_play_time_init(play_time)
    globals.set_play_time(play_time)
    
    if not globals.get_is_continue():
        globals.set_lives_init(lives)
        globals.set_lives(lives)
    
    globals.set_penalty(penalty)


def set_question_win(is_win : bool, effect : dict):
    if is_win:
        score = globals.get_score()
        score += REWARD
        if globals.get_is_rewardx2():
            score += REWARD
            globals.set_is_rewardx2(False)
        globals.set_score(score)
        # pass_question(max_index, events)
        sound.play_effect(effect)


def set_question_lost(is_lost : bool, effect : dict):
    if is_lost:
        lives = globals.get_lives()
        score = globals.get_score()

        if not lives == INT_0:
            lives -= INT_1
            if not score == INT_0 : score -= globals.get_penalty()
            globals.set_lives(lives)
            globals.set_score(score)
            # if not lives == INT_0 : pass_question(max_index, events)
            sound.play_effect(effect)


def set_next_question( max_index : int):
    next_question = globals.get_current_question() + INT_1
    play_time = globals.get_play_time_init()

    if not next_question == max_index:
        globals.set_current_question(next_question)
        globals.set_play_time(play_time)
    else:
        globals.set_questover_on(True)

    if globals.get_is_repeat() : globals.set_is_repeat(False)
    if globals.get_is_bomb() : globals.set_is_bomb(False)
    if globals.get_is_rewardx2() : globals.set_is_rewardx2(False)


def apply_stage_buttons_set(id : str):
    globals.disable_instances()
    if id == AVENGERS_BUTTON : globals.set_avengers_on(True)
    elif id == SIMPSONS_BUTTON : globals.set_simpsons_on(True)
    elif id == STARWARS_BUTTON : globals.set_starwars_on(True)
    globals.set_game_on(True)
    sound.play_music(off=True)
    globals.set_play_music(False)


def apply_stage_buttons_shadow\
    (screen : pg.surface.Surface, image : pg.surface.Surface,rect : pg.rect.Rect, is_complete : bool):
    if not is_complete:
        screen.blit(image, rect)
    else:
        surface_fill = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
        surface_fill.fill(BRIGHT_CLICK, special_flags=pg.BLEND_RGBA_ADD)
        screen.blit(image, rect)
        screen.blit(surface_fill, rect)


def reset_difficulty_game():
    globals.set_easy_on(False)
    globals.set_middle_on(False)
    globals.set_hard_on(False)


def pass_question(is_lost : bool, max_index : int, events : list[pg.event.Event]):
    if not globals.get_lives() == INT_0:

        if globals.get_is_pass(): # EL JUGADOR ACTIVÓ PASAR PREGUNTA
            globals.set_wrong_answer(None)
            globals.set_is_pass(False)
            set_next_question(max_index)
        else:
            if globals.get_item_on(): # EL JUGADOR RESPONDIÓ
                time = globals.get_pass_delay()

                for e in events:
                    if e.type == EVENT_1000MS:
                        time -= INT_1
                        globals.set_pass_delay(time)

                if time == 0:
                    globals.set_pass_delay(PASS_DELAY)
                    globals.set_item_on(False)
                    set_next_question(max_index)

            else: # SE TERMINÓ EL TIEMPO DE JUEGO Y EL JUGADOR NO RESPONDIÓ
                if is_lost : set_next_question(max_index)


def repeat_question():
    previous_question = globals.get_current_question() - INT_1
    play_time = globals.get_play_time_init()
    globals.set_current_question(previous_question)
    globals.set_play_time(play_time)


def check_user_answer(lost : any, win : any, answer : int, user_answer: int) -> tuple:
    is_lost = lost
    is_win = win

    if user_answer in OPTIONS:

        if not user_answer == answer:
            is_lost = True
            if not globals.get_is_repeat() : globals.set_wrong_answer(user_answer)
        else:
            is_win = True
            if not globals.get_is_repeat() : globals.set_wrong_answer(None)
        
        if globals.get_is_repeat():
            is_lost = check_repeat_question(is_lost, user_answer)

        if globals.get_is_bomb():
            is_lost = check_bomb_question(is_lost, user_answer)

    return is_lost, is_win


def check_repeat_question(is_lost : bool, user_answer : int) -> bool:
    lost_ok = is_lost

    if is_lost and user_answer == globals.get_wrong_answer():
        lost_ok = False

    return lost_ok


def check_bomb_question(is_lost : bool, user_answer : int):
    lost_ok = is_lost
    wrong_answers = globals.get_wrong_answers()

    if is_lost and user_answer in [wrong_answers[INT_0], wrong_answers[INT_1]]:
        lost_ok = False

    return lost_ok


def check_endgame(id_questions : str, events : list[pg.event.Event]):
    lives = globals.get_lives()
    time = globals.get_gameover_delay()

    if lives == INT_0 or globals.get_questover_on():
        for e in events:
            if e.type == EVENT_1000MS:
                time -= INT_1
                globals.set_gameover_delay(time)

        if time == INT_0:
            globals.disable_instances()

            if lives == INT_0:
                globals.set_gameover_on(True)
            else:
                globals.set_youwin_on(True) # EL JUGADOR GANA SI TERMINÓ EL CUESTIONARIO Y AUN TIENE VIDAS
                
                if id_questions == AVENGERS_QUESTIONS : globals.set_avengers_complete(True)
                elif id_questions == SIMPSONS_QUESTIONS : globals.set_simpsons_complete(True)
                elif id_questions == STARWARS_QUESTIONS : globals.set_starwars_complete(True)

    if globals.get_gameover_on() or globals.get_youwin_on():
        sound.play_music(off=True)
        globals.set_play_music(False)


def check_username_ok(username : str):
    if len(username) - INT_1 < USERNAME_LEN_MIN:
        globals.set_warning(WARNING_MIN_MAX)
    else:
        globals.set_warning(WARNING_NAME_OK)
        globals.set_username_ok(True)


def check_slider_pressed(pos : tuple, rect : pg.rect.Rect):
    click_pressed = False

    if rect.collidepoint(pos) and pg.mouse.get_pressed()[INT_0]:
        click_pressed = True
    
    return click_pressed


def check_click_pressed(rect : pg.rect.Rect, button : dict, events : list[pg.event.Event]) -> bool:
    click_pressed = False
    pos = pg.mouse.get_pos()

    if rect.collidepoint(pos):

        if pg.mouse.get_pressed()[INT_0]:
            globals.set_is_click(True)
            button[STATE] = ST_CLICK
        else:
            globals.set_is_click(False)
            button[STATE] = ST_HOVER
    else:
        button[STATE] = ST_NORMAL
        
    if not globals.get_click_on():
        for e in events:
            if e.type == pg.MOUSEBUTTONDOWN:
                if rect.collidepoint(e.pos):
                    globals.set_click_on(True)
    else:
        if not globals.get_is_click():
            globals.set_click_on(False)
            click_pressed = True

    return click_pressed


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

    for user in scores_copy:
        user[DATE] = format_date((user.get(DATE)))

    globals.set_scores_copy(scores_copy)


def get_user_scores(path : str):
    scores = load_scores(path)
    globals.set_scores_list(scores)
    copy_scores(scores)
    sort_scores(globals.get_scores_copy(), ascending=False)


def get_settings_bars(config : dict) -> list[dict]:
    bars = config.get(BARS)

    for bar in bars:
        x = bar.get(X)
        y = bar.get(Y)
        w = bar.get(W)
        h = bar.get(H)
        bar[RECT] = pg.Rect(x,y,w,h)

    return bars


def get_settings_sliders(config : dict) -> list[dict]:
    sliders = config.get(SLIDERS)

    for slider in sliders:
        x = slider.get(X)
        y = slider.get(Y)
        w = slider.get(W)
        h = slider.get(H)
        slider[RECT] = pg.Rect(x,y,w,h)

    return sliders

# ------------------------------------------------------------------------------------------- #

def is_letter(char : str) -> bool:
    is_letter = True
    ascii = ord(char)
    
    if not (ascii >= 65 and ascii <= 90) and not (ascii >= 97 and ascii <= 122):
        is_letter = False

    return is_letter


def is_integer(string : str) -> bool:
    is_integer = len(string) > INT_0
    
    for i in range(len(string)):
        ascii = ord(string[i])

        if i == INT_0 and ascii == INT_45:
            if len(string) > INT_1:
                continue
            else:
                is_integer = False
                break
         
        if ascii < INT_48 or ascii > INT_57:
            is_integer = False
            break
    
    return is_integer