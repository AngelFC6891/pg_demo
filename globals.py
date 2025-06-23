from constants import *

home_on = True
settings_on = False
scores_on = False
stages_on = False
avengers_on = False
simpsons_on = False
starwars_on = False
game_on = False
gameover_on = False
questover_on = False
username_on = False
reset_on = False
click_on = False
is_click = False
current_question = QUEST_INIT
lives = LIVES_INIT
score = SCORE_INIT
play_time = PLAY_TIME
gameover_time = GAMEOVER_TIME
gameover_delay = GAMEOVER_DELAY


def set_home_on(value : bool) -> None:
    global home_on
    home_on = value


def set_settings_on(value : bool) -> None:
    global settings_on
    settings_on = value


def set_scores_on(value : bool) -> None:
    global scores_on
    scores_on = value


def set_avengers_on(value : bool) -> None:
    global avengers_on
    avengers_on = value


def set_simpsons_on(value : bool) -> None:
    global simpsons_on
    simpsons_on = value


def set_starwars_on(value : bool) -> None:
    global starwars_on
    starwars_on = value


def set_stages_on(value : bool) -> None:
    global stages_on
    stages_on = value


def set_game_on(value : bool) -> None:
    global game_on
    game_on = value


def set_gameover_on(value : bool) -> None:
    global gameover_on
    gameover_on = value


def set_questover_on(value : bool) -> None:
    global questover_on
    questover_on = value


def set_username_on(value : bool) -> None:
    global username_on
    username_on = value


def set_reset_on(value : bool) -> None:
    global reset_on
    reset_on = value


def set_click_on(value : bool) -> None:
    global click_on
    click_on = value


def set_current_question(value : int) -> None:
    global current_question
    current_question = value


def set_lives(value : int) -> None:
    global lives
    lives = value


def set_play_time(value : int) -> None:
    global play_time
    play_time = value


def set_score(value : int) -> None:
    global score
    score = value


def set_gameover_time(value : int) -> None:
    global gameover_time
    gameover_time = value


def set_gameover_delay(value : int) -> None:
    global gameover_delay
    gameover_delay = value

# ------------------------------------------------------------------------------------------- #

def get_home_on() -> bool:
    return home_on


def get_settings_on() -> bool:
    return settings_on


def get_scores_on() -> bool:
    return scores_on


def get_stages_on() -> bool:
    return stages_on


def get_avengers_on() -> bool:
    return avengers_on


def get_simpsons_on() -> bool:
    return simpsons_on


def get_starwars_on() -> bool:
    return starwars_on


def get_game_on() -> bool:
    return game_on


def get_gameover_on() -> bool:
    return gameover_on


def get_questover_on() -> bool:
    return questover_on


def get_username_on() -> bool:
    return username_on


def get_reset_on() -> bool:
    return reset_on


def get_click_on() -> bool:
    return click_on


def get_current_question() -> int:
    return current_question


def get_lives() -> int:
    return lives


def get_play_time() -> int:
    return play_time


def get_score() -> int:
    return score


def get_gameover_time() -> int:
    return gameover_time


def get_gameover_delay() -> int:
    return gameover_delay

# ------------------------------------------------------------------------------------------- #

def set_is_click(value : bool) -> None:
    global is_click
    is_click = value

# ------------------------------------------------------------------------------------------- #

def get_is_click() -> bool:
    return is_click

# ------------------------------------------------------------------------------------------- #

def disable_instances():
    set_home_on(False)
    set_settings_on(False)
    set_scores_on(False)
    set_stages_on(False)
    set_avengers_on(False)
    set_simpsons_on(False)
    set_starwars_on(False)
    set_stages_on(False)
    set_game_on(False)
    set_gameover_on(False)
    set_questover_on(False)
    set_reset_on(False)