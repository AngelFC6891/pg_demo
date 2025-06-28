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
music_on = True
effects_on = True
pass_on = True
repeat_on = True
bomb_on = True
rewardx2_on = True
is_click = False
is_pass = False
is_repeat = False
is_rewardx2 = False
is_bomb = False
username_ok = False
play_music = False
wrong_answer = None
current_question = QUEST_INIT
lives = LIVES_INIT
score = SCORE_INIT
username = VOID_STR
warning = VOID_STR
play_time = PLAY_TIME
gameover_time = GAMEOVER_TIME
gameover_delay = GAMEOVER_DELAY
vol_music = VOL_MUSIC_INIT
vol_effects = VOL_EFFECTS_INIT
scores_list = []
scores_copy = []
wrong_answers = []
effects = {}


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


def set_play_music(value : bool) -> None:
    global play_music
    play_music = value


def set_reset_on(value : bool) -> None:
    global reset_on
    reset_on = value


def set_click_on(value : bool) -> None:
    global click_on
    click_on = value


def set_music_on(value : bool) -> None:
    global music_on
    music_on = value


def set_effects_on(value : bool) -> None:
    global effects_on
    effects_on = value


def set_pass_on(value : bool) -> None:
    global pass_on
    pass_on = value


def set_repeat_on(value : bool) -> None:
    global repeat_on
    repeat_on = value


def set_bomb_on(value : bool) -> None:
    global bomb_on
    bomb_on = value


def set_rewardx2_on(value : bool) -> None:
    global rewardx2_on
    rewardx2_on = value


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


def set_username(value : str) -> None:
    global username
    username = value


def set_warning(value : str) -> None:
    global warning
    warning = value


def set_username_ok(value : bool) -> None:
    global username_ok
    username_ok = value


def set_gameover_time(value : int) -> None:
    global gameover_time
    gameover_time = value


def set_gameover_delay(value : int) -> None:
    global gameover_delay
    gameover_delay = value


def set_scores_list(value : list) -> list[dict]:
    global scores_list
    scores_list = value


def set_scores_copy(copy : list[dict]) -> None:
    global scores_copy
    scores_copy = copy


def set_vol_music(value : float) -> None:
    global vol_music
    vol_music = value


def set_vol_effects(value : float) -> None:
    global vol_effects
    vol_effects = value


def set_effects(value : dict) -> None:
    global effects
    effects = value


def set_wrong_answer(value : any) -> None:
    global wrong_answer
    wrong_answer = value


def set_wrong_answers(value : list) -> None:
    global wrong_answers
    wrong_answers = value

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


def get_play_music() -> bool:
    return play_music


def get_reset_on() -> bool:
    return reset_on


def get_click_on() -> bool:
    return click_on


def get_music_on() -> bool:
    return music_on


def get_effects_on() -> bool:
    return effects_on


def get_pass_on() -> bool:
    return pass_on


def get_repeat_on() -> bool:
    return repeat_on


def get_bomb_on() -> bool:
    return bomb_on


def get_rewardx2_on() -> bool:
    return rewardx2_on


def get_current_question() -> int:
    return current_question


def get_lives() -> int:
    return lives


def get_play_time() -> int:
    return play_time


def get_score() -> int:
    return score


def get_username() -> str:
    return username


def get_warning() -> str:
    return warning


def get_username_ok() -> bool:
    return username_ok


def get_gameover_time() -> int:
    return gameover_time


def get_gameover_delay() -> int:
    return gameover_delay


def get_scores_list() -> list[dict]:
    return scores_list


def get_scores_copy() -> list[dict]:
    return scores_copy


def get_vol_music() -> float:
    return vol_music


def get_vol_effects() -> float:
    return vol_effects


def get_effects() -> dict:
    return effects


def get_wrong_answer() -> any:
    return wrong_answer


def get_wrong_answers() -> list:
    return wrong_answers

# ------------------------------------------------------------------------------------------- #

def set_is_click(value : bool) -> None:
    global is_click
    is_click = value


def set_is_pass(value : bool) -> None:
    global is_pass
    is_pass = value


def set_is_repeat(value : bool) -> None:
    global is_repeat
    is_repeat = value


def set_is_rewardx2(value : bool) -> None:
    global is_rewardx2
    is_rewardx2 = value


def set_is_bomb(value : bool) -> None:
    global is_bomb
    is_bomb = value

# ------------------------------------------------------------------------------------------- #

def get_is_click() -> bool:
    return is_click


def get_is_pass() -> bool:
    return is_pass


def get_is_repeat() -> bool:
    return is_repeat


def get_is_rewardx2() -> bool:
    return is_rewardx2


def get_is_bomb() -> bool:
    return is_bomb

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
    set_username_on(False)
    set_questover_on(False)
    set_reset_on(False)