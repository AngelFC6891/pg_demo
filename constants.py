import pygame as pg

# SCREEN
SCREEN_W, SCREEN_H = 600, 600
SOURCE = (0,0)
CAPTION = 'Funny Quest'

# DATA CONFIG
DATA = 'data'
CONFIG = 'config/config.json'

# INSTANCES
IMAGES = 'images'
BACKGROUNDS = 'backgrounds'
QUESTIONS = 'questions'
HOME = 'home'
SETTINGS = 'settings'
SCORES = 'scores'
STAGES = 'stages'
AVENGERS = 'avengers'
SIMPSONS = 'simpsons'
STARWARS = 'starwars'
GAMEOVER = 'gameover'

# GENERIC KEYS
FILE = 'file'
ID = 'id'
X = 'x'
Y = 'y'
IMAGE = 'image'
QUESTION = 'question'
ANSWER = 'answer'
BUTTONS = 'buttons'
LABELS = 'labels'
RENDER = 'render'

# FILES
R = 'r'
UTF = 'utf-8'

# QUESTIONS
AVENGERS_QUESTIONS = 'avengers_questions'
SIMPSONS_QUESTIONS = 'simpsons_questions'
STARWARS_QUESTIONS = 'starwars_questions'

# INTEGERS
INT_0 = 0
INT_1 = 1
INT_2 = 2
INT_3 = 3
INT_4 = 4
INT_5 = 5
INT_45 = 45
INT_48 = 48
INT_57 = 57

# INTEGER VALUES
FPS = 20
MS_1000 = 1000
REWARD = 100
PENALTY = 25
QUEST_INIT = 0
LIVES_INIT = 3
SCORE_INIT = 0
PLAY_TIME = 10
GAMEOVER_TIME = 4
GAMEOVER_DELAY = 2
LEN_MAX = 24
Y_INIT_QUEST = 130
Y_INIT_OPT = 300
X_INIT_OPT = 125
Y_VAR = 40

# GENERIC STRINGS
VOID_STR = ''
SPACE_STR = ' '
BREAK_STR = '\n'
HYPHEN_STR = '_'

# EVENTS
EVENT_1000MS = pg.USEREVENT

# BUTTONS
PLAY_BUTTON = 'play_button'
SETTINGS_BUTTON = 'settings_button'
SCORES_BUTTON = 'scores_button'
HOME_BUTTONS = [PLAY_BUTTON, SETTINGS_BUTTON, SCORES_BUTTON]
HOME_BUTTON = 'home_button'
PASS_BUTTON = 'pass_button'
AVENGERS_BUTTON = 'avengers_button'
SIMPSONS_BUTTON = 'simpsons_button'
STARWARS_BUTTON = 'starwars_button'
STAGES_BUTTONS = [HOME_BUTTON, AVENGERS_BUTTON, SIMPSONS_BUTTON, STARWARS_BUTTON]
GAME_BUTTONS = [PASS_BUTTON]

# LABELS
LIVES = 'lives'
LIVES_RENDER = 'lives_render'
TIME = 'time'
TIME_RENDER = 'time_render'
SCORE = 'score'
SCORE_RENDER = 'score_render'

# TEXT
FONT = 'Courier New'
FONT_SIZE_QUEST = 28
FONT_SIZE_OPT = 24
FONT_SIZE_LAB = 20
BOLD = True
OPTION = 'option'
OPTIONS = [1,2,3,4]
QUESTION_RENDER = 'question_render'
OPTIONS_RENDER = 'options_render'

# COLORS
YELLOW = (230,233,0)
BLUE = (10,0,204)
WHITE = (255,255,255)