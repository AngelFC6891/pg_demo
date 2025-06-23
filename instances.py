from constants import *
import library
import methods
import globals


config = library.load_config(CONFIG, DATA)
buttons = library.get_buttons(config)
labels = library.get_labels(config)
backgrounds = library.get_backgrounds()
questions = library.get_questions()
library.shuffle_questions(questions)
avengers_questions = questions.get(AVENGERS_QUESTIONS)
simpsons_questions = questions.get(SIMPSONS_QUESTIONS)
starwars_questions = questions.get(STARWARS_QUESTIONS)
home_background = backgrounds.get(HOME)
stages_background = backgrounds.get(STAGES)
gameover_background = backgrounds.get(GAMEOVER)
home_buttons = [button for button in buttons if button.get(ID) in HOME_BUTTONS]
stages_buttons = [button for button in buttons if button.get(ID) in STAGES_BUTTONS]
game_buttons = [button for button in buttons if button.get(ID) in GAME_BUTTONS]


def run_home(screen : pg.surface.Surface, events : list[pg.event.Event]) -> None:
    if globals.get_home_on():
        methods.update_background()
        methods.update_buttons(home_buttons, events)
        methods.draw_background(screen, home_background)
        methods.draw_buttons(screen, home_buttons)


def run_settings(screen : pg.surface.Surface):
    if globals.get_settings_on():
        pass


def run_scores(screen : pg.surface.Surface):
    if globals.get_scores_on():
        pass


def run_stages(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_stages_on():
        methods.update_background()
        methods.update_buttons(stages_buttons, events)
        methods.draw_background(screen, stages_background)
        methods.draw_buttons(screen, stages_buttons)


def run_game(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_game_on():
        if globals.get_avengers_on():
            background = backgrounds.get(AVENGERS)
            current_questions = avengers_questions
        elif globals.get_simpsons_on():
            background = backgrounds.get(SIMPSONS)
            current_questions = simpsons_questions
        elif globals.get_starwars_on:
            background = backgrounds.get(STARWARS)
            current_questions = starwars_questions
        
        methods.update_background()
        methods.update_buttons(game_buttons, events)
        methods.update_game(current_questions, labels, events)
        methods.draw_background(screen, background)
        methods.draw_buttons(screen, game_buttons)
        methods.draw_game(screen, current_questions, labels)


def run_gameover(screen : pg.surface.Surface, events : list[pg.event.Event]):
    if globals.get_gameover_on():
        methods.update_gameover(events)
        methods.draw_background(screen, gameover_background)


def run_username(screen : pg.surface.Surface, events : list[pg.event.Event]):
    pass


def run_reset():
    if globals.get_reset_on():
        library.shuffle_questions(questions)
        globals.set_current_question(QUEST_INIT)
        globals.set_lives(LIVES_INIT)
        globals.set_score(SCORE_INIT)
        globals.set_play_time(PLAY_TIME)
        globals.set_gameover_time(GAMEOVER_TIME)
        globals.disable_instances()
        globals.set_home_on(True)


def execute(screen : pg.surface.Surface, events : list[pg.event.Event]):
    run_home(screen, events)
    # run_settings(screen)
    # run_scores(screen, events)
    run_stages(screen, events)
    run_game(screen, events)
    run_gameover(screen, events)
    run_reset()
