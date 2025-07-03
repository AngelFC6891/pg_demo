import random
from constants import *
import library
import sound
import globals


def update_buttons(questions : list[dict]=[], buttons : list[dict]=[], events : list[pg.event.Event]=[]) -> None:
    for button in buttons:
        id = button.get(ID)
        image = button.get(IMAGE)
        rect = image.get_rect()
        rect.x = button.get(X)
        rect.y = button.get(Y)
        effects = globals.get_effects()
        
        if library.check_click_pressed(rect, button, events):

            if globals.get_home_on() : update_home_buttons(id, effects.get(CLICK))
            elif globals.get_settings_on() : update_settings_buttons(id, effects)
            elif globals.get_difficulty_on() : update_difficulty_buttons(id, effects)
            elif globals.get_scores_on() : update_scores_buttons(id, effects.get(PASS))
            elif globals.get_stages_on() : update_stages_buttons(id, effects)
            elif globals.get_game_on() : update_game_buttons(id, questions, effects.get(PASS))
            elif globals.get_continue_on() : update_continue_button(id, effects.get(CLICK))
            elif globals.get_username_on() : update_username_buttons(id, effects.get(CLICK))


def update_home_buttons(id : str, effect : dict):
    if id in INSTANCES_BUTTONS.get(HOME):
        globals.disable_instances()

        if id == PLAY_BUTTON:
            globals.set_stages_on(True)
        elif id == SETTINGS_BUTTON:
            globals.set_settings_on(True)
        elif id == SCORES_BUTTON:
            globals.set_scores_on(True)

        sound.play_effect(effect)


def update_stages_buttons(id : str, effects : dict[dict]):
    if id in INSTANCES_BUTTONS.get(STAGES):

        if id == HOME_BUTTON:
            effect = effects.get(PASS)
            globals.disable_instances()
            globals.set_home_on(True)
        else:
            effect = effects.get(CLICK)

            if id == AVENGERS_BUTTON and not globals.get_avengers_complete():
                library.apply_stage_buttons_set(id)

            elif id == SIMPSONS_BUTTON and not globals.get_simpsons_complete():
                library.apply_stage_buttons_set(id)

            elif id == STARWARS_BUTTON and not globals.get_starwars_complete():
                library.apply_stage_buttons_set(id)
            
        sound.play_effect(effect)


def update_game_buttons(id : str, questions : list[dict], effect : dict):
    max_index = len(questions)
    current_question = questions[globals.get_current_question()]
    answer = current_question.get(ANSWER)

    if not globals.get_lives() == INT_0:
        if id in INSTANCES_BUTTONS.get(GAME):
            
            if id == PASS_BUTTON:
                # SI EL JUGADOR REPITIÓ LA PREGUNTA, ACTIVÓ LA BOMBA O DUPLICÓ LA RECOMPENSA,
                # Y LUEGO PASA, PIERDE EL COMODÍN

                if globals.get_pass_on():
                    library.pass_question(False, max_index, events=[])
                    globals.set_is_pass(True)
                    globals.set_pass_on(False)
                    
            elif id == REPEAT_BUTTON:
                # SOLO FUNCIONA SI EL JUGADOR ELIGIÓ PREVIAMENTE UNA OPCION
                
                if globals.get_repeat_on() and globals.get_wrong_answer() and not globals.get_is_bomb():
                    library.repeat_question()
                    globals.set_is_repeat(True)
                    globals.set_repeat_on(False)

            elif id == BOMB_BUTTON:
                # SOLO FUNCIONA SI EL JUGADOR NO ESTÁ REPITIENDO LA PREGUNTA

                if globals.get_bomb_on() and not globals.get_is_repeat():
                    wrong_answers = [key for key in current_question.keys() if type(key) == int and not key == answer]
                    random.shuffle(wrong_answers)
                    globals.set_wrong_answers(wrong_answers[:-1])
                    globals.set_is_bomb(True)
                    globals.set_bomb_on(False)

            elif id == REWARDX2_BUTTON:
                if globals.get_rewardx2_on():
                    globals.set_is_rewardx2(True)
                    globals.set_rewardx2_on(False)
        
            sound.play_effect(effect)


def update_continue_button(id : str, effect : dict):
    if id in INSTANCES_BUTTONS.get(CONTINUE):
        globals.disable_instances()

        if id == YES_BUTTON:
            globals.set_is_continue(True)
            globals.set_reset_on(True)

        elif id == NO_BUTTON:
            globals.set_gameover_on(True)

        sound.play_effect(effect)


def update_username_buttons(id : str, effect : dict):
    if id in INSTANCES_BUTTONS.get(USERNAME):

        if id == OKAY_BUTTON:
            if globals.get_username_ok():
                user_data = library.get_user_data()
                library.add_user_data(SCORES_JSON, user_data)
                library.get_user_scores(SCORES_JSON)
                globals.disable_instances()
                globals.set_reset_on(True)
        
        elif id == CANCEL_BUTTON:
            globals.disable_instances()
            globals.set_reset_on(True)
        
        sound.play_effect(effect)


def update_scores_buttons(id: str, effect : dict):
    if id == HOME_BUTTON:
        globals.disable_instances()
        globals.set_home_on(True)
        sound.play_effect(effect)


def update_settings_buttons(id : str, effects : dict[dict]):
    if id in [HOME_BUTTON, NEXT_BUTTON]:
        effect = effects.get(PASS)
        globals.disable_instances()

        if id == HOME_BUTTON:
            globals.set_home_on(True)

        elif id == NEXT_BUTTON:
            globals.set_difficulty_on(True)

        sound.play_effect(effect)
    else:
        effect = effects.get(CLICK)

        if id == ON_MUSIC_BUTTON:
            value = not globals.get_music_on()
            globals.set_music_on(value)
        
        elif id == ON_EFFECTS_BUTTON:
            value = not globals.get_effects_on()
            globals.set_effects_on(value)
        
        sound.play_effect(effect)


def update_difficulty_buttons(id : str, effects : dict[dict]):
    if id in [HOME_BUTTON, BACK_BUTTON]:
        effect = effects.get(PASS)
        globals.disable_instances()

        if id == HOME_BUTTON:
            globals.set_home_on(True)

        elif id == BACK_BUTTON:
            globals.set_settings_on(True)

        sound.play_effect(effect)
    else:
        library.reset_difficulty_game()
        effect = effects.get(CLICK)

        if id == EASY_BUTTON:
            globals.set_easy_on(True)
        
        elif id == MIDDLE_BUTTON:
            globals.set_middle_on(True)

        elif id == HARD_BUTTON:
            globals.set_hard_on(True)
        
        library.set_difficulty_game()
        sound.play_effect(effect)


def update_question(question : dict):
    question_blocks = library.get_blocks(question.get(QUESTION), LEN_MAX_BLOCK)
    question_render = []
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_QUEST, BOLD_ENABLE)

    for block in question_blocks:
        question_render.append(font_sys.render(block, True, font_color))

    question[QUESTION_RENDER] = question_render


def update_options(question : dict):
    if not question.get(OPTIONS_RENDER):
        options = []
        font_color = library.get_font_color()
        font_sys = pg.font.SysFont(FONT_COURIER, FONT_SIZE_OPT, BOLD_ENABLE)

        for key in question.keys():
            if type(key) == int:
                option = f'{key}{PARENT_END_STR}{SPACE_STR}{question.get(key)}'
                options.append(font_sys.render(option, True, font_color))

        question[OPTIONS_RENDER] = options


def update_labels(labels : list[dict], max_index : int=0):
    font_color = library.get_font_color()
    font_sys = library.get_font_sys()

    for label in labels:
        key_render = f'{label.get(ID)}{LOW_HYPHEN_STR}{RENDER}'
        label[key_render] = font_sys.render(library.get_label_value(label.get(ID), max_index), True, font_color)


def update_item(is_win : bool, items : dict[str, dict], user_answer : int):
    if user_answer:
        item = items.get(RIGHT) if is_win else items.get(WRONG)
        item[USER_ANSWER] = user_answer
        globals.set_game_item(item)
        globals.set_item_on(True)
    else:
        if not globals.get_item_on() : globals.set_game_item(None)


def update_game(questions : list[dict], labels : list[dict], items : dict[str, dict], events : list[pg.event.Event]):
    if not globals.get_questover_on():
        is_lost = False
        is_win = False
        question = {}
        user_answer = None
        effects = globals.get_effects()
        
        if not globals.get_item_on():
            question = questions[globals.get_current_question()]
            answer = question.get(ANSWER)
            time = globals.get_play_time()

            if time == INT_0:
                is_lost = True
            else:
                for e in events:
                    if e.type == EVENT_1000MS:
                        time -= INT_1
                        globals.set_play_time(time)

                    if e.type == pg.KEYDOWN:
                        if library.is_integer(e.unicode):
                            user_answer = int(e.unicode)
                    
                    elif e.type == pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        user_answer = library.get_user_answer(pos, question, update_options)

                is_lost, is_win = library.check_user_answer(is_lost, is_win, answer, user_answer)
        
        update_item(is_win, items, user_answer)
        if question:
            library.set_question_lost(is_lost, question.get(QUESTION), effects.get(ERROR))
            library.set_question_win(is_win, question.get(QUESTION), effects)

            if is_lost or is_win:
                library.add_stat_data(question.get(QUESTION), USED_QTY)
                library.add_stat_data(question.get(QUESTION), SUCCESS_PERCENT)
        
        library.pass_question(is_lost, len(questions), events)
        question = questions[globals.get_current_question()]
        update_question(question)
        update_options(question)
        update_labels(labels, len(questions))


def update_youwin(events : list[pg.event.Event]):
    time = globals.get_youwin_time()
    
    if time == YOUWIN_TIME:
        sound.play_effect(globals.get_effects().get(YOUWIN))

    for e in events:
        if e.type == EVENT_1000MS:
            time -= 1
            globals.set_youwin_time(time)

    if time == 0:
        globals.disable_instances()
        
        if globals.get_avengers_complete() and\
            globals.get_simpsons_complete() and\
            globals.get_starwars_complete():
            globals.set_gameover_on(True)
        else:
            globals.set_continue_on(True)


def update_continue(labels : dict , events : list[pg.event.Event]):
    update_labels(labels, events)
    time = globals.get_continue_time()

    for e in events:
        if e.type == EVENT_1000MS:
            time -= INT_1
            globals.set_continue_time(time)

    if time == -INT_1:
        globals.disable_instances()
        globals.set_gameover_on(True)


def update_gameover(events : list[pg.event.Event]):
    time = globals.get_gameover_time()

    if time == globals.get_gameover_time():
        library.show_stat_data()

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
                header_render = f'{header}{LOW_HYPHEN_STR}{RENDER}'
                user[header_render] = font_sys.render(user.get(header), True, font_color)


def update_username(events : list[pg.event.Event]):
    username = globals.get_username()
    warning = globals.get_warning()
    if warning == VOID_STR : globals.set_warning(WARNING_MIN_MAX)

    for e in events:
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_BACKSPACE:
                if len(username) > 0:
                    username = username[:-1]
                    globals.set_username(username)
                    library.check_username_ok(username)
            else:
                if not e.unicode == VOID_STR:
                    if not library.is_letter(e.unicode):
                        globals.set_warning(WARNING_USE_LETTERS)
                    else:
                        if len(username) < USERNAME_LEN_MAX:
                            username += e.unicode
                            globals.set_username(username.upper())
                            library.check_username_ok(username)
                else:
                    globals.set_warning(WARNING_USE_LETTERS)


def update_sliders(bars : list[dict], sliders : list[dict]):
    bar_x = bars[INT_0].get(X)
    bar_w = bars[INT_0].get(W)

    for slider in sliders:
        id = slider.get(ID)
        rect = slider.get(RECT)
        rect.y = slider.get(Y)
        pos = pg.mouse.get_pos()
        pos_x, _ = pos

        if id == SLIDER_MUSIC:
            volume = globals.get_vol_music()
            
        elif id == SLIDER_EFFECTS:
            volume = globals.get_vol_effects()

        if library.check_slider_pressed(pos, rect):
            
            if pos_x >= bar_x and pos_x <= (bar_x + bar_w):
                rect.centerx = pos_x
            else:
                if pos_x < bar_x : rect.centerx = bar_x
                elif pos_x > (bar_x + bar_w) : rect.centerx = (bar_x + bar_w)

            volume = (rect.centerx - bar_x) / bar_w
            if id == SLIDER_MUSIC:
                pg.mixer.music.set_volume(volume)
                globals.set_vol_music(volume)
            
            elif id == SLIDER_EFFECTS:
                globals.set_vol_effects(volume)

        rect.centerx = bar_x + (bar_w * volume)

# ------------------------------------------------------------------------------------------- #

def draw_background(screen : pg.surface.Surface, backg : pg.surface.Surface):
    screen.blit(backg, SOURCE)


def draw_buttons(screen : pg.surface.Surface, buttons : list[dict]):
    for button in buttons:
        image = button.get(IMAGE)
        rect = image.get_rect()
        rect.x = button.get(X)
        rect.y = button.get(Y)
        id = button.get(ID)
        state = button.get(STATE)

        if globals.get_settings_on() : draw_settings_buttons(screen, image, rect, id)
        elif globals.get_difficulty_on() : draw_difficulty_buttons(screen, image, rect, id)
        elif globals.get_stages_on() : draw_stages_buttons(screen, image, rect, id)
        elif globals.get_game_on() : draw_games_buttons(screen, image, rect, id)
        else : screen.blit(image, rect)
            
        if not state == ST_NORMAL and id not in NO_EFFECT_BUTTONS:
            surface_fill = pg.Surface((rect.width, rect.height), pg.SRCALPHA)

            if state == ST_HOVER:
                surface_fill.fill(BRIGHT_HOVER, special_flags=pg.BLEND_RGBA_ADD)
            elif state == ST_CLICK:
                surface_fill.fill(BRIGHT_CLICK, special_flags=pg.BLEND_RGBA_ADD)

            screen.blit(surface_fill, rect)


def draw_settings_buttons(screen : pg.surface.Surface, image : pg.surface.Surface, rect : pg.rect.Rect, id = str):
    if id == ON_MUSIC_BUTTON:
        if globals.get_music_on():
            screen.blit(image, rect)
    
    elif id == ON_EFFECTS_BUTTON:
        if globals.get_effects_on():
            screen.blit(image, rect)
    else:
        screen.blit(image, rect)


def draw_difficulty_buttons(screen : pg.surface.Surface, image : pg.surface.Surface, rect : pg.rect.Rect, id = str):
    if id == EASY_BUTTON:
        if globals.get_easy_on():
            screen.blit(image, rect)
    
    elif id == MIDDLE_BUTTON:
        if globals.get_middle_on():
            screen.blit(image, rect)

    elif id == HARD_BUTTON:
        if globals.get_hard_on():
            screen.blit(image, rect)
    else:
        screen.blit(image, rect)


def draw_stages_buttons(screen : pg.surface.Surface, image : pg.surface.Surface, rect : pg.rect.Rect, id = str):
    if id == HOME_BUTTON:
        screen.blit(image, rect)
    
    elif id == AVENGERS_BUTTON:
        is_complete = globals.get_avengers_complete()
        library.apply_stage_buttons_shadow(screen, image, rect, is_complete)

    elif id == SIMPSONS_BUTTON:
        is_complete = globals.get_simpsons_complete()
        library.apply_stage_buttons_shadow(screen, image, rect, is_complete)

    elif id == STARWARS_BUTTON:
        is_complete = globals.get_starwars_complete()
        library.apply_stage_buttons_shadow(screen, image, rect, is_complete)


def draw_games_buttons(screen : pg.surface.Surface, image : pg.surface.Surface, rect : pg.rect.Rect, id = str):
    if id == PASS_BUTTON:
        if globals.get_pass_on():
            screen.blit(image, rect)
    
    elif id == REPEAT_BUTTON:
        if globals.get_repeat_on():
            screen.blit(image, rect)

    elif id == BOMB_BUTTON:
        if globals.get_bomb_on():
            screen.blit(image, rect)

    elif id == REWARDX2_BUTTON:
        if globals.get_rewardx2_on():
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
    item = globals.get_game_item()
    y = Y_INIT_OPT
    pos = pg.mouse.get_pos()

    for i, option in enumerate(options_render):
        rect = option.get_rect()
        rect.x = X_INIT_OPT
        rect.y = y
        draw_game_item(screen, item, rect, i)

        if globals.get_is_repeat():
            if not (i + INT_1) == globals.get_wrong_answer():
                screen.blit(option, rect)
                draw_shadow_option(screen, rect, pos)
        
        elif globals.get_is_bomb():
            if not (i + INT_1) in globals.get_wrong_answers():
                screen.blit(option, rect)
                draw_shadow_option(screen, rect, pos)
        
        else:
            screen.blit(option, rect)
            draw_shadow_option(screen, rect, pos)
        
        y += Y_VAR


def draw_shadow_option(screen : pg.surface.Surface, rect : pg.rect.Rect, pos : tuple):
    if rect.collidepoint(pos):
        surface_fill = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
        surface_fill.fill(BRIGHT_HOVER, special_flags=pg.BLEND_RGBA_ADD)
        screen.blit(surface_fill, rect)


def draw_game_item(screen : pg.surface.Surface, item : dict, option_rect : pg.rect.Rect, i : int):
    if item:
        user_answer = item.get(USER_ANSWER)

        if user_answer == (i + INT_1):
            image = item.get(IMAGE)
            rect = image.get_rect()
            rect.x = item.get(X)
            
            if item.get(ID) == RIGHT : rect.bottom = option_rect.bottom
            elif item.get(ID) == WRONG : rect.centery = option_rect.centery

            screen.blit(image, rect)


def draw_labels(screen : pg.surface.Surface, labels : list[dict]):
    for label in labels:
        label_render = label.get(f'{label.get(ID)}{LOW_HYPHEN_STR}{RENDER}')
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
    position_render = user.get(f'{POSITION}{LOW_HYPHEN_STR}{RENDER}')
    rect = position_render.get_rect()
    rect.right = X_POS
    rect.top = y
    screen.blit(position_render, rect)


def draw_user_name(screen : pg.surface.Surface, user : dict, y : int):
    name_render = user.get(f'{NAME}{LOW_HYPHEN_STR}{RENDER}')
    rect = name_render.get_rect()
    rect.left = X_NAME
    rect.top = y
    screen.blit(name_render, rect)


def draw_user_score(screen : pg.surface.Surface, user : dict, y : int):
    score_render = user.get(f'{SCORE}{LOW_HYPHEN_STR}{RENDER}')
    rect = score_render.get_rect()
    rect.right = X_SCORE
    rect.top = y
    screen.blit(score_render, rect)


def draw_user_date(screen : pg.surface.Surface, user : dict, y : int):
    date_render = user.get(f'{DATE}{LOW_HYPHEN_STR}{RENDER}')
    rect = date_render.get_rect()
    rect.left = X_DATE
    rect.top = y
    screen.blit(date_render, rect)


def draw_game(screen : pg.surface.Surface, questions : list[dict], labels : list[dict]):
    question = questions[globals.get_current_question()]
    draw_question(screen, question)
    draw_options(screen, question)
    draw_labels(screen, labels)


def draw_continue(screen : pg.surface.Surface, labels : list[dict]):
    for label in labels:
        label_render = label.get(f'{label.get(ID)}{LOW_HYPHEN_STR}{RENDER}')
        rect = label_render.get_rect()
        rect.x = (screen.get_width() - label_render.get_width()) / 2
        rect.y = (screen.get_height() - label_render.get_height()) / 2
        screen.blit(label_render, rect)


def draw_username(screen : pg.surface.Surface, events : list[pg.event.Event]):
    draw_username_itself(screen, events, font_color=VIOLET)
    draw_username_score(screen, font_color=VIOLET)
    draw_warning(screen)
    

def draw_username_itself(screen : pg.surface.Surface, events : list[pg.event.Event], font_color : tuple):
    font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_USERNAME, BOLD_ENABLE)
    username = globals.get_username()
    username_render = font_sys.render(username, True, font_color)
    rect = username_render.get_rect()
    rect.x = X_USERNAME
    rect.y = Y_USERNAME
    screen.blit(username_render, rect)
    draw_blink_pointer(screen, events, font_sys, font_color, rect)


def draw_blink_pointer(screen : pg.surface.Surface, events : list[pg.event.Event],\
                       font_sys : pg.font.Font, font_color : tuple, rect : pg.rect.Rect):
    for e in events:
        if e.type == EVENT_500MS:
            if not globals.get_pointer_on() : globals.set_pointer_on(True)
            else : globals.set_pointer_on(False)

    if globals.get_pointer_on():
        cursor_render = font_sys.render(LOW_HYPHEN_STR, True, font_color)
        cursor_rect = cursor_render.get_rect()
        cursor_rect.x = rect.right
        cursor_rect.y = rect.top
        screen.blit(cursor_render, cursor_rect)


def draw_username_score(screen : pg.surface.Surface, font_color : tuple):
    font_sys = pg.font.SysFont(FONT_SEGOE, FONT_SIZE_SCORE, BOLD_ENABLE)
    score = globals.get_score()
    score_render = font_sys.render(str(score), True, font_color)
    rect = score_render.get_rect()
    rect.x = (screen.get_width() - score_render.get_width()) / 2
    rect.y = Y_USERNAME_SCORE
    screen.blit(score_render, rect)


def draw_warning(screen : pg.surface.Surface):
    font_color = library.get_font_color()
    font_sys = pg.font.SysFont(FONT_MV_BOLI, FONT_SIZE_WARNING)
    warning = globals.get_warning()
    warning_render = font_sys.render(f'{ASTERISK_STR}{warning}', True, font_color)
    rect = warning_render.get_rect()
    rect.x = (screen.get_width() - warning_render.get_width()) / 2
    rect.y = Y_WARNING
    screen.blit(warning_render, rect)


def draw_bars(screen : pg.surface.Surface, bars : list[dict]):
    for bar in bars:
        rect = bar.get(RECT)
        color = BLUE_BORDER
        border = bar.get(BORDER)
        pg.draw.rect(screen, color, rect, border)


def draw_sliders(screen : pg.surface.Surface, sliders : list[dict]):
    for slider in sliders:
        rect = slider.get(RECT)
        color = BLUE_BORDER
        border = slider.get(BORDER)
        screen.fill(BLUE_INNER, rect)
        pg.draw.rect(screen, color, rect, border)