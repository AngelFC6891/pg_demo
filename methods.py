from copy import deepcopy
from constants import *
import library
import globals


def update_background():
    pass


def update_buttons(buttons : list[dict], events : list[pg.event.Event], max_index : int=0) -> None:
    for button in buttons:
        id = button.get(ID)
        image = button.get(IMAGE)
        rect = image.get_rect()
        rect.x = button.get(X)
        rect.y = button.get(Y)
        pos = pg.mouse.get_pos()
        
        if rect.collidepoint(pos):
            if pg.mouse.get_pressed()[INT_0]:
                globals.set_is_click(True)
            else:
                globals.set_is_click(False)
        
        if not globals.get_click_on():
            for e in events:
                if e.type == pg.MOUSEBUTTONDOWN:
                    if rect.collidepoint(e.pos):
                        globals.set_click_on(True)
        else:
            if not globals.get_is_click():
                globals.set_click_on(False)

                if id == HOME_BUTTON:
                    globals.disable_instances()
                    globals.set_home_on(True)
                
                elif id in HOME_BUTTONS:
                    globals.disable_instances()

                    if id == PLAY_BUTTON:
                        globals.set_stages_on(True)
                    elif id == SETTINGS_BUTTON:
                        globals.set_settings_on(True)
                    elif id == SCORES_BUTTON:
                        globals.set_scores_on(True)
                
                elif id in STAGES_BUTTONS:
                    globals.disable_instances()
                    globals.set_game_on(True)

                    if id == AVENGERS_BUTTON:
                        globals.set_avengers_on(True)
                    elif id == SIMPSONS_BUTTON:
                        globals.set_simpsons_on(True)
                    elif id == STARWARS_BUTTON:
                        globals.set_starwars_on(True)

                elif id in GAME_BUTTONS:

                    if id == PASS_BUTTON:
                        if not globals.get_lives() == 0 : library.set_question_pass(True, max_index)
                        

def update_question(question : dict):
    question_blocks = library.get_blocks(question.get(QUESTION), LEN_MAX)
    question_render = []
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT, FONT_SIZE_QUEST, BOLD_ENABLE)

    for block in question_blocks:
        question_render.append(font_sys.render(block, True, font_color))

    question[QUESTION_RENDER] = question_render


def update_options(question : dict):
    options = []
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT, FONT_SIZE_OPT, BOLD_ENABLE)

    for key in question.keys():
        if type(key) == int:
            option = f'{key}.{question.get(key)}'
            options.append(font_sys.render(option, True, font_color))

    question[OPTIONS_RENDER] = options


def update_labels(labels : list[dict]):
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT, FONT_SIZE_LAB, BOLD_ENABLE)

    for label in labels:
        if label.get(ID) == LIVES:
            label[LIVES_RENDER] = font_sys.render(str(globals.get_lives()), True, font_color)
        
        elif label.get(ID) == TIME:
            label[TIME_RENDER] = font_sys.render(str(globals.get_play_time()), True, font_color)
        
        elif label.get(ID) == SCORE:
            label[SCORE_RENDER] = font_sys.render(str(globals.get_score()), True, font_color)


def update_game(questions : list[dict], labels : list[dict], events : list[pg.event.Event]):
    is_lost = False
    is_win = False

    if not globals.get_questover_on():
        answer = questions[globals.get_current_question()].get(ANSWER)
        time = globals.get_play_time()

        if time == INT_0:
            is_lost = True
        else:
            for e in events:
                if e.type == EVENT_1000MS:
                    time -= 1
                    globals.set_play_time(time)

                if e.type == pg.KEYDOWN:
            
                    if library.is_integer(e.unicode) and int(e.unicode) in OPTIONS:

                        if not int(e.unicode) == answer:
                            is_lost = True
                        else:
                            is_win = True
    
    library.set_question_lost(is_lost, len(questions))
    library.set_question_win(is_win, len(questions))
    question = questions[globals.get_current_question()]
    update_question(question)
    update_options(question)
    update_labels(labels)
    library.check_gameover(events)


def update_gameover(events : list[pg.event.Event]):
    time = globals.get_gameover_time()

    for e in events:
        if e.type == EVENT_1000MS:
            time -= 1
            globals.set_gameover_time(time)

    if time == 0:
        globals.disable_instances()
        globals.set_reset_on(True)
        # globals.set_username_on(True)


def update_scores(scores : list[dict], top : int=1):
    library.sort_scores(scores, ascending=False)
    font_color = WHITE
    font_sys = pg.font.SysFont(FONT, FONT_SIZE_LAB, BOLD_ENABLE)


# ------------------------------------------------------------------------------------------- #

def draw_background(screen : pg.surface.Surface, backg : pg.surface.Surface):
    screen.blit(backg, SOURCE)


def draw_buttons(screen : pg.surface.Surface, buttons : list[dict]):
    for button in buttons:
        image = button.get(IMAGE)
        rect = image.get_rect()
        rect.x = button.get(X)
        rect.y = button.get(Y)
        screen.blit(image, rect)


def draw_question(screen : pg.surface.Surface, question : dict):
    question_render = question.get(QUESTION_RENDER)
    y = Y_INIT_QUEST

    for block in question_render:
        rect = block.get_rect()
        rect.x = (screen.get_width() - block.get_width()) / 2
        rect.y = y
        screen.blit(block, rect)
        y += Y_VAR


def draw_options(screen : pg.surface.Surface, question : dict):
    options_render = question.get(OPTIONS_RENDER)
    y = Y_INIT_OPT

    for option in options_render:
        rect = option.get_rect()
        rect.x = X_INIT_OPT
        rect.y = y
        screen.blit(option, rect)
        y += Y_VAR


def draw_labels(screen : pg.surface.Surface, labels : list[dict]):
    for label in labels:
        label_render = label.get(f'{label.get(ID)}{HYPHEN_STR}{RENDER}')
        rect = label_render.get_rect()
        rect.x = label.get(X)
        rect.y = label.get(Y)
        screen.blit(label_render, rect)


def draw_scores(screen : pg.surface.Surface, scores : list[dict]):
    for score in scores:
        score_render = score.get(f'{SCORE}{HYPHEN_STR}{RENDER}')
        rect = score_render.get_rect()
        rect.x = score.get(X)
        rect.y = score.get(Y)
        screen.blit(score_render, rect)


def draw_scores_themself(score : dict):
    pass


def draw_scores_names(score : dict):
    pass


def draw_scores_dates(score : dict):
    pass


def draw_game(screen : pg.surface.Surface, questions : list[dict], labels : list[dict]):
    question = questions[globals.get_current_question()]
    draw_question(screen, question)
    draw_options(screen, question)
    draw_labels(screen, labels)
    