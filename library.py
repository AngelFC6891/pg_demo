import os
import json
import random
from constants import *
import globals


def load_config(path : str, key : str) -> dict:
    config = {}
    
    with open(path, R, encoding=UTF) as file:
        data = json.load(file)
        config = data.get(key)
    
    return config


def shuffle_questions(questions : dict[str, list]):
    for list in questions.values():
        random.shuffle(list)


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


def get_font_color() -> None | tuple:
    font_color = None

    if globals.get_avengers_on():
        font_color = YELLOW
    elif globals.get_simpsons_on():
        font_color = BLUE
    elif globals.get_starwars_on():
        font_color = WHITE

    return font_color


def set_question_win(is_win : bool):
    if is_win:
        score = globals.get_score()
        score += REWARD
        next_question = globals.get_current_question() + INT_1
        globals.set_score(score)
        globals.set_current_question(next_question)
        globals.set_play_time(PLAY_TIME)


def set_question_lost(is_lost : bool):
    lives = globals.get_lives()
    score = globals.get_score()

    if is_lost and not lives == INT_0:
        lives -= INT_1
        score -= PENALTY
        globals.set_lives(lives)
        globals.set_score(score)
        
        if not lives == INT_0:
            next_question = globals.get_current_question() + INT_1
            globals.set_current_question(next_question)
            globals.set_play_time(PLAY_TIME)


def set_question_pass(is_pass : bool):
    if is_pass:
        next_question = globals.get_current_question() + INT_1
        globals.set_current_question(next_question)
        globals.set_play_time(PLAY_TIME)


def check_gameover(max_index : int, events : list[pg.event.Event]):
    lives = globals.get_lives()
    time = globals.get_gameover_delay()

    if lives == INT_0 or globals.get_current_question == max_index:
        for e in events:
            if e.type == EVENT_1000MS:
                time -= 1
                globals.set_gameover_delay(time)

        if time == INT_0:
            globals.disable_instances()
            globals.set_gameover_on(True)


def is_integer(string : str) -> bool:
    output = len(string) > INT_0
    
    for i in range(len(string)):
        ascii = ord(string[i])

        if i == INT_0 and ascii == INT_45:
            if len(string) > 1:
                continue
            else:
                output = False
                break
         
        if ascii < INT_48 or ascii > INT_57:
            output = False
            break
    
    return output


# #ESPECIFICA --> SOLO CONSOLA
# def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
#     numero_ingresado = int(input(mensaje))
#     while numero_ingresado > maximo or numero_ingresado < minimo:
#         numero_ingresado = int(input(mensaje_error))
#     return numero_ingresado

# #GENERAL (PUEDE SERVIRME EN PYGAME)
# def mezclar_lista(lista_preguntas:list) -> None:
#     random.shuffle(lista_preguntas)
    
# def mostrar_datos_juego(datos_juego:dict) -> None:
#     print(f"PUNTUACION: {datos_juego["puntuacion"]}")
#     print(f"VIDAS RESTANTES: {datos_juego["vidas"]}")
    
# def mostrar_pregunta(pregunta_actual:dict) -> None:
#     print(f"\n{pregunta_actual["pregunta"]}")
#     print(f"1.{pregunta_actual["respuesta_1"]}")
#     print(f"2.{pregunta_actual["respuesta_2"]}")
#     print(f"3.{pregunta_actual["respuesta_3"]}")
    
# def terminar_juego(datos_juego:dict) -> None:
#     print(f"TERMINO EL JUEGO\nPUNTUACION: {datos_juego["puntuacion"]} PUNTOS")
    
#     nombre_usuario = input("Ingrese su nombre: ")
#     datos_juego["nombre"] = nombre_usuario
    
#     confirmacion = input("¿Desea guardar la puntuacion? (si/no) ")
    
#     if confirmacion == "si":
#         #GUARDAN LOS RANKING
#         pass
        
# #ESPECIFICA --> SOLO CONSOLA
# def jugar_preguntados_consola(lista_preguntas:list,datos_juego:dict) -> None:
#     contador = 0
#     lapso = 1 / FPS
#     indice = 0
#     # actual = time.time() 
#     #tiempo_juego = 30   
#     mezclar_lista(lista_preguntas)
    
#     while datos_juego["vidas"] != 0:
#         if indice >= len(lista_preguntas):
#             mezclar_lista(lista_preguntas)
#             indice = 0
        
#         pregunta_actual = lista_preguntas[indice]
#         # fin = time.time()
#         # tiempo_juego -= int(fin - actual)
#         # actual = time.time()
        
#         mostrar_datos_juego(datos_juego)
#         #print(f"TIEMPO JUEGO: {tiempo_juego} SEGUNDOS")
#         contador+=1        
    
#         mostrar_pregunta(pregunta_actual)
#         respuesta = pedir_numero("Su respuesta:","Reingrese su respuesta (1-3):",1,3)

#         os.system("clear")
#         if verificar_respuesta(pregunta_actual,datos_juego,respuesta) == True:
#             print("RESPUESTA CORRECTA")
#         else:
#             print("RESPUESTA INCORRECTA")
        
#         indice += 1
#         time.sleep(lapso)
#         os.system("clear")
        
#     terminar_juego(datos_juego)

# #GENERAL (FUNCIONA TANTO EN PYGAME COMO EN CONSOLA)
# def verificar_respuesta(pregunta_actual:dict,datos_juego:dict,respuesta:int) -> bool:
#     if respuesta == pregunta_actual["respuesta_correcta"]:
#         retorno = True
#         datos_juego["puntuacion"] += REWARD
#     else:
#         retorno = False
#         datos_juego["puntuacion"] -= PENALTY
#         datos_juego["vidas"] -=1
        
#     return retorno

# #GENERAL 
# def reiniciar_estadisticas(datos_juego:dict) -> None:#(FUNCIONA TANTO EN PYGAME COMO EN CONSOLA)
#     datos_juego["vidas"] = LIVES
#     datos_juego["puntuacion"] = 0