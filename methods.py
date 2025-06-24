from constants import *
import library
import globals
# import pprint


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

                elif id in USERNAME_BUTTONS:

                    if id == ENTER_BUTTON:
                        if globals.get_username_ok():
                            username = globals.get_username()
                            globals.set_username(username[:-1])
                            user_data = library.get_user_data()
                            library.add_user_data(SCORES_CSV, user_data)
                            library.get_user_scores(SCORES_CSV)
                            globals.disable_instances()
                            globals.set_reset_on(True)


def update_question(question : dict):
    question_blocks = library.get_blocks(question.get(QUESTION), LEN_MAX_BLOCK)
    question_render = []
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_QUEST, BOLD_ENABLE)

    for block in question_blocks:
        question_render.append(font_sys.render(block, True, font_color))

    question[QUESTION_RENDER] = question_render


def update_options(question : dict):
    options = []
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_OPT, BOLD_ENABLE)

    for key in question.keys():
        if type(key) == int:
            option = f'{key}.{question.get(key)}'
            options.append(font_sys.render(option, True, font_color))

    question[OPTIONS_RENDER] = options


def update_labels(labels : list[dict]):
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_LAB, BOLD_ENABLE)

    for label in labels:
        key_render = f'{label.get(ID)}{HYPHEN_STR}{RENDER}'
        label[key_render] = font_sys.render(library.get_label_value(label.get(ID)), True, font_color)


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
                    time -= INT_1
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
        globals.set_username_on(True)


def update_scores(scores : list[dict], top : int=1):
    font_color = AQUA
    font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_SCORES, BOLD_ENABLE)

    for i in range(top):
        user = scores[i]
        user[POSITION] = str(i+1)
        headers = list(user.keys())

        for header in headers:
            if header in TABLE_HEADERS:
                header_render = f'{header}{HYPHEN_STR}{RENDER}'
                user[header_render] = font_sys.render(user.get(header), True, font_color)


def update_username(events : list[pg.event.Event]):
    username = globals.get_username()
    warning = globals.get_warning()
    if username == VOID_STR : globals.set_username(HYPHEN_STR)
    if warning == VOID_STR : globals.set_warning(WARNING_MIN_MAX)

    for e in events:
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_BACKSPACE:
                if len(username) > 1:
                    username = username[:-2] + HYPHEN_STR
                    globals.set_username(username)
            else:
                if not e.unicode == VOID_STR:
                    if not library.is_letter(e.unicode):
                        globals.set_warning(WARNING_USE_LETTERS)
                    else:
                        if len(username) - INT_1 < USERNAME_LEN_MAX:
                            username = username[:-1] + e.unicode + HYPHEN_STR
                            globals.set_username(username.upper())
                        
                        if len(username) - INT_1 < USERNAME_LEN_MIN:
                            globals.set_warning(WARNING_MIN_MAX)
                        else:
                            globals.set_warning(WARNING_NAME_OK)
                            globals.set_username_ok(True)
                else:
                    globals.set_warning(WARNING_USE_LETTERS)

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


def draw_scores(screen : pg.surface.Surface, scores : list[dict], top : int=1):
    y = Y_INIT_TABLE

    for i in range(top):
        user = scores[i]
        draw_user_position(screen, user, y)
        draw_user_name(screen, user, y)
        draw_user_score(screen, user, y)
        draw_user_date(screen, user, y)
        y += Y_VAR_TABLE


def draw_user_position(screen : pg.surface.Surface, user : dict, y : int):
    position_render = user.get(f'{POSITION}{HYPHEN_STR}{RENDER}')
    rect = position_render.get_rect()
    rect.right = X_POS
    rect.top = y
    screen.blit(position_render, rect)


def draw_user_name(screen : pg.surface.Surface, user : dict, y : int):
    name_render = user.get(f'{NAME}{HYPHEN_STR}{RENDER}')
    rect = name_render.get_rect()
    rect.left = X_NAME
    rect.top = y
    screen.blit(name_render, rect)


def draw_user_score(screen : pg.surface.Surface, user : dict, y : int):
    score_render = user.get(f'{SCORE}{HYPHEN_STR}{RENDER}')
    rect = score_render.get_rect()
    rect.right = X_SCORE
    rect.top = y
    screen.blit(score_render, rect)


def draw_user_date(screen : pg.surface.Surface, user : dict, y : int):
    date_render = user.get(f'{DATE}{HYPHEN_STR}{RENDER}')
    rect = date_render.get_rect()
    rect.left = X_DATE
    rect.top = y
    screen.blit(date_render, rect)


def draw_game(screen : pg.surface.Surface, questions : list[dict], labels : list[dict]):
    question = questions[globals.get_current_question()]
    draw_question(screen, question)
    draw_options(screen, question)
    draw_labels(screen, labels)
    

def draw_username(screen : pg.surface.Surface):
    draw_username_itself(screen, font_color=VIOLET)
    draw_username_score(screen, font_color=VIOLET)
    draw_warning(screen)
    

def draw_username_itself(screen : pg.surface.Surface, font_color : tuple):
    font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_SCORE, BOLD_ENABLE)
    score = globals.get_score()
    score_render = font_sys.render(str(score), True, font_color)
    rect = score_render.get_rect()
    rect.x = (screen.get_width() - score_render.get_width()) / 2
    rect.y = Y_USERNAME_SCORE
    screen.blit(score_render, rect)


def draw_username_score(screen : pg.surface.Surface, font_color : tuple):
    font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_USERNAME, BOLD_ENABLE)
    username = globals.get_username()
    username_render = font_sys.render(username, True, font_color)
    rect = username_render.get_rect()
    rect.x = (screen.get_width() - username_render.get_width()) / 2
    rect.y = Y_USERNAME
    screen.blit(username_render, rect)


def draw_warning(screen : pg.surface.Surface):
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_MV_BOLI, FONT_SIZE_WARNING)
    warning = globals.get_warning()
    warning_render = font_sys.render(f'{ASTERISK_STR}{warning}', True, font_color)
    rect = warning_render.get_rect()
    rect.x = (screen.get_width() - warning_render.get_width()) / 2
    rect.y = Y_WARNING
    screen.blit(warning_render, rect)