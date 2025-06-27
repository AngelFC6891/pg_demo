import sys
from constants import *
import instances


def run():

    screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
    pg.display.set_caption(CAPTION)
    pg.init()
    pg.font.init()
    clock = pg.time.Clock()
    pg.time.set_timer(EVENT_1000MS, MS_1000)

    while True:

        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # keys = pg.key.get_pressed()
        clock.tick(FPS)
        instances.execute(screen, events)
        pg.display.flip()