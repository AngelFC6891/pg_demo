from constants import *
import library
import sound
import methods
import globals
# import pprint


config = library.load_config(CONFIG, DATA)
buttons = library.get_buttons(config)
game_labels = library.get_labels(config, GAME)
game_items = library.get_items(config, GAME)
settings_labels = library.get_labels(config, SETTINGS)
difficulty_labels = library.get_labels(config, DIFFICULTY)
backgrounds = library.get_backgrounds()
questions = library.get_questions()
bars = library.get_settings_bars(config)
sliders = library.get_settings_sliders(config)
music = library.get_music(config)
library.get_effects(config)
library.shuffle_questions(questions)
library.get_user_scores(SCORES_JSON)
library.set_difficulty_game()


def run_home(screen : pg.surface.Surface, events : list[pg.event.Event]) -> None:
    if globals.get_home_on():
        sound.play_music(music.get(GAME_MUSIC))
        methods.update_buttons(buttons=buttons.get(HOME), events=events)
        methods.draw_background(screen, backgrounds.get(HOME))
        methods.draw_buttons(screen, buttons.get(HOME))
        

def run_settings(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_settings_on():
        sound.play_music(music.get(GAME_MUSIC))
        methods.update_labels(settings_labels)
        methods.update_buttons(buttons=buttons.get(SETTINGS), events=events)
        methods.update_sliders(bars, sliders, events)
        methods.draw_background(screen, backgrounds.get(SETTINGS))
        methods.draw_buttons(screen, buttons.get(SETTINGS))
        methods.draw_bars(screen, bars)
        methods.draw_sliders(screen, sliders)
        methods.draw_labels(screen, settings_labels)


def run_difficulty(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_difficulty_on():
        methods.update_labels(difficulty_labels)
        methods.update_buttons(buttons=buttons.get(DIFFICULTY), events=events)
        methods.draw_background(screen, backgrounds.get(DIFFICULTY))
        methods.draw_buttons(screen, buttons.get(DIFFICULTY))
        methods.draw_labels(screen, difficulty_labels)


def run_scores(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_scores_on():
        scores_copy = globals.get_scores_copy()
        methods.update_buttons(buttons=buttons.get(SCORES), events=events)
        methods.update_scores(scores_copy, top=INT_10)
        methods.draw_background(screen, backgrounds.get(SCORES))
        methods.draw_buttons(screen, buttons.get(SCORES))
        methods.draw_scores(screen, scores_copy, top=INT_10)
        

def run_stages(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_stages_on():
        methods.update_buttons(buttons=buttons.get(STAGES), events=events)
        methods.draw_background(screen, backgrounds.get(STAGES))
        methods.draw_buttons(screen, buttons.get(STAGES))


def run_game(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_game_on():

        if globals.get_avengers_on():
            background = backgrounds.get(AVENGERS)
            current_questions = questions.get(AVENGERS_QUESTIONS)
            current_music = music.get(AVENGERS_MUSIC)
        
        elif globals.get_simpsons_on():
            background = backgrounds.get(SIMPSONS)
            current_questions = questions.get(SIMPSONS_QUESTIONS)
            current_music = music.get(SIMPSONS_MUSIC)
        
        elif globals.get_starwars_on():
            background = backgrounds.get(STARWARS)
            current_questions = questions.get(STARWARS_QUESTIONS)
            current_music = music.get(STARWARS_MUSIC)
        
        sound.play_music(current_music)
        methods.update_buttons(current_questions, buttons.get(GAME), events)
        methods.update_game(current_questions, game_labels, game_items, events)
        methods.draw_background(screen, background)
        methods.draw_buttons(screen, buttons.get(GAME))
        methods.draw_game(screen, current_questions, game_labels)
        library.check_endgame(events)


def run_youwin(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_youwin_on():
        pass


def run_continue(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_continue_on():
        pass


def run_gameover(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_gameover_on():
        sound.play_music(music.get(GAME_MUSIC))
        methods.update_gameover(events)
        methods.draw_background(screen, backgrounds.get(GAMEOVER))


def run_username(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_username_on():
        methods.update_buttons(buttons=buttons.get(USERNAME), events=events)
        methods.update_username(events)
        methods.draw_background(screen, backgrounds.get(USERNAME))
        methods.draw_buttons(screen, buttons.get(USERNAME))
        methods.draw_username(screen)


def run_reset():
    if globals.get_reset_on():
        library.shuffle_questions(questions)
        globals.set_current_question(QUEST_INIT)
        globals.set_score(SCORE_INIT)
        globals.set_gameover_time(GAMEOVER_TIME)
        globals.set_username(VOID_STR)
        globals.disable_instances()
        globals.set_game_item(None)
        globals.set_item_on(False)
        globals.set_username_ok(False)
        globals.set_home_on(True)
        globals.set_pass_on(True)
        globals.set_repeat_on(True)
        globals.set_bomb_on(True)
        globals.set_rewardx2_on(True)
        globals.set_is_repeat(False)
        globals.set_is_bomb(False)
        globals.set_is_rewardx2(False)
        library.set_difficulty_game()


def execute(screen : pg.surface.Surface, events : list[pg.event.Event]):
    run_home(screen, events)
    run_settings(screen, events)
    run_difficulty(screen, events)
    run_scores(screen, events)
    run_stages(screen, events)
    run_game(screen, events)
    run_youwin(screen, events)
    run_continue(screen, events)
    run_gameover(screen, events)
    run_username(screen, events)
    run_reset()
