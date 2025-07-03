import sys
from constants import *
import instances


def run():

    screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
    pg.display.set_caption(CAPTION)
    pg.init()
    pg.font.init()
    clock = pg.time.Clock()

    while True:

        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()

        clock.tick(FPS)
        instances.execute(screen, events)
        pg.display.flip()