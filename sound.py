import pygame as pg
import globals
from constants import *
pg.mixer.init()


def play_music(config : dict={}, off : bool=False):
    if globals.get_music_on():
        if not globals.get_play_music():
            volume = globals.get_vol_music()
            pg.mixer.music.load(f'{SOUNDS}/{config.get(FILE)}')
            pg.mixer.music.set_volume(volume)
            pg.mixer.music.play(loops=config.get(LOOP))
            globals.set_play_music(True)
        else:
            if off:
                pg.mixer.music.stop()
    else:
        if pg.mixer.music.get_busy():
            pg.mixer.music.stop()
            globals.set_play_music(False)


def play_effect(effect : dict):
    if globals.get_effects_on():
        volume = globals.get_vol_effects()
        loop = effect.get(LOOP)
        pg_effect = effect.get(EFFECT)
        pg_effect.set_volume(volume)
        pg_effect.play(loop)