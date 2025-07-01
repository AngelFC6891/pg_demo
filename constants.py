import pygame as pg

# SCREEN
SCREEN_W, SCREEN_H = 600, 600
SOURCE = (0,0)
CAPTION = 'Funny Quest'

# DATA CONFIG
DATA = 'data'
CONFIG = 'config/config.json'
SCORES_CSV = 'scores.csv'
SCORES_JSON = 'scores.json'
SOUNDS = 'sounds'

# INSTANCES
IMAGES = 'images'
BACKGROUNDS = 'backgrounds'
QUESTIONS = 'questions'
HOME = 'home'
SETTINGS = 'settings'
SCORES = 'scores'
DIFFICULTY = 'difficulty'
STAGES = 'stages'
GAME = 'game'
CONTINUE = 'continue'
YOUWIN = 'youwin'
AVENGERS = 'avengers'
SIMPSONS = 'simpsons'
STARWARS = 'starwars'
GAMEOVER = 'gameover'
USERNAME = 'username'

# GENERIC KEYS
POSITION = 'position'
NAME = 'name'
DATE = 'date'
FILE = 'file'
ID = 'id'
X = 'x'
Y = 'y'
IMAGE = 'image'
QUESTION = 'question'
ANSWER = 'answer'
BUTTON = 'button'
BUTTONS = 'buttons'
LABELS = 'labels'
ITEMS = 'items'
GAME_LABELS = 'game_labels'
GAME_ITEMS = 'game_items'
SETTINGS_LABELS = 'settings_labels'
DIFFICULTY_LABELS = 'difficulty_labels'
CONTINUE_LABELS = 'continue_labels'
RENDER = 'render'
OPTION = 'option'
USER_ANSWER = 'user_answer'
RIGHT = 'right'
WRONG = 'wrong'
BARS = 'bars'
SLIDERS = 'sliders'
W = 'w'
H = 'h'
RECT = 'rect'
COLOR = 'color'
BORDER = 'border'
CENTERX = 'centerx'

# FILES
R = 'r'
A = 'a'
UTF = 'utf-8'

# DATES
STANDAR_FORMAT = f'%Y-%m-%d'
FORMAT = f'%d-%m-%y'

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
INT_10 = 10
INT_45 = 45
INT_48 = 48
INT_57 = 57
INT_100 = 100

# INTEGER VALUES
FPS = 30
MS_1000 = 1000
REWARD = 100
QUEST_INIT = 25 # SE CUENTA A PARTIR DEL CERO
LIVES_INIT = 0
SCORE_INIT = 0
PLAY_TIME_INIT = 0
YOUWIN_TIME = 5
CONTINUE_TIME = 11
GAMEOVER_TIME = 4
GAMEOVER_DELAY = 2
PASS_DELAY = 2
LEN_MAX_BLOCK = 24
USERNAME_LEN_MAX = 8
USERNAME_LEN_MIN = 3

# QUESTION AND OPTIONS INIT POSITIONS
Y_INIT_QUEST = 130
Y_INIT_OPT = 300
X_INIT_OPT = 125
Y_VAR = 40

# USERNAME INIT POSITIONS
Y_USERNAME_SCORE = 100
Y_USERNAME = 310
Y_WARNING = 400

# SCORES TABLE INIT POSITIONS
X_POS = 85
X_NAME = 100
X_SCORE = 355
X_DATE = 390
Y_INIT_TABLE = 145
Y_VAR_TABLE = 34

# GENERIC STRINGS
VOID_STR = ''
SPACE_STR = ' '
PARENT_END_STR = ')'
LOW_HYPHEN_STR = '_'
COMMA_STR = ','
ASTERISK_STR = '*'
PERCENT_STR = '%'
SLASH_STR = '/'

# EVENTS
EVENT_1000MS = pg.USEREVENT

# BUTTONS
PLAY_BUTTON = 'play_button'
SETTINGS_BUTTON = 'settings_button'
SCORES_BUTTON = 'scores_button'
HOME_BUTTON = 'home_button'
NEXT_BUTTON = 'next_button'
BACK_BUTTON = 'back_button'
PASS_BUTTON = 'pass_button'
REPEAT_BUTTON = 'repeat_button'
BOMB_BUTTON = 'bomb_button'
REWARDX2_BUTTON = 'rewardx2_button'
OKAY_BUTTON = 'okay_button'
CANCEL_BUTTON = 'cancel_button'
YES_BUTTON = 'yes_button'
NO_BUTTON = 'no_button'
AVENGERS_BUTTON = 'avengers_button'
SIMPSONS_BUTTON = 'simpsons_button'
STARWARS_BUTTON = 'starwars_button'
ON_MUSIC_BUTTON = 'on_music_button'
ON_EFFECTS_BUTTON = 'on_effects_button'
EASY_BUTTON = 'easy_button'
MIDDLE_BUTTON = 'middle_button'
HARD_BUTTON = 'hard_button'
INSTANCES_BUTTONS =\
{
    HOME: [PLAY_BUTTON,SETTINGS_BUTTON,SCORES_BUTTON],
    STAGES: [HOME_BUTTON,AVENGERS_BUTTON,SIMPSONS_BUTTON,STARWARS_BUTTON],
    GAME: [PASS_BUTTON, REPEAT_BUTTON, BOMB_BUTTON, REWARDX2_BUTTON],
    CONTINUE: [YES_BUTTON, NO_BUTTON],
    SCORES: [HOME_BUTTON],
    USERNAME: [OKAY_BUTTON, CANCEL_BUTTON],
    SETTINGS: [HOME_BUTTON,NEXT_BUTTON,ON_MUSIC_BUTTON,ON_EFFECTS_BUTTON],
    DIFFICULTY: [HOME_BUTTON,BACK_BUTTON,EASY_BUTTON,MIDDLE_BUTTON,HARD_BUTTON]
}
STATE = 'state'
ST_CLICK = 'state_click'
ST_HOVER = 'state_hover'
ST_NORMAL = 'state_normal'
NO_EFFECT_BUTTONS = [ON_MUSIC_BUTTON,ON_EFFECTS_BUTTON,EASY_BUTTON,MIDDLE_BUTTON,HARD_BUTTON]

# LABELS
PLAY_TIME = 'play_time'
NUMBER = 'number'
LIVES = 'lives'
PENALTY = 'penalty'
TIME = 'time'
SCORE = 'score'
CONTINUE_COUNTDOWN = 'continue_countdown'

# TEXT
FONT_COURIER = 'Courier New'
FONT_SEGOE = 'Segoe Print'
FONT_MV_BOLI = 'MV Boli'
FONT_SIZE_QUEST = 28
FONT_SIZE_OPT = 24
FONT_SIZE_LAB = 20
FONT_SIZE_SCORES = 25
FONT_SIZE_USERNAME = 48
FONT_SIZE_SCORE = 60
FONT_SIZE_WARNING = 24
FONT_SIZE_VOLUME = 24
FONT_SIZE_COUNTDOWN = 90
BOLD_ENABLE = True
OPTIONS = [1,2,3,4]
QUESTION_RENDER = 'question_render'
OPTIONS_RENDER = 'options_render'

# TABLE HEADERS
TABLE_HEADERS = [POSITION, NAME, SCORE, DATE]

# COLORS
YELLOW = (230,233,0)
YELLOW_CAKE = (255,245,150)
BLUE = (10,0,204)
BLUE_BORDER = (34,60,255)
BLUE_INNER = (0,155,219)
WHITE = (255,255,255)
AQUA = (0,190,200)
VIOLET = (145,25,255)
RED = (255,0,0)
GREEN = (0,255,0)
GREEN_CAKE = (130,240,150)
CAKE = (255,205,210)
BRIGHT_HOVER = (125,255,255,64)
BRIGHT_CLICK = (125,255,255,128)

# WARNINGS
WARNING_MIN_MAX = 'Use at least 3 letters and 8 as maximum'
WARNING_USE_LETTERS = 'Use only letters'
WARNING_NAME_OK = 'User name ok'

# MUSIC AND EFFECTS
ON = 1
OFF = 0
MUSIC = 'music'
EFFECTS = 'effects'
EFFECT = 'effect'
VOLUME = 'volume'
LOOP = 'loop'
GAME_MUSIC = 'game_music'
AVENGERS_MUSIC = 'avengers_music'
SIMPSONS_MUSIC = 'simpsons_music'
STARWARS_MUSIC = 'starwars_music'
BAR_MUSIC = 'bar_music'
BAR_EFFECTS = 'bar_effects'
SLIDER_MUSIC = 'slider_music'
SLIDER_EFFECTS = 'slider_effects'
VOL_MUSIC = 'vol_music'
VOL_MUSIC_INIT = 0.15
VOL_EFFECTS = 'vol_effects'
VOL_EFFECTS_INIT = 0.15
CLICK = 'click'
WIN = 'win'
ERROR = 'error'
PASS = 'pass'

# DIFFICULTY: (PLAY TIME, LIVES, PENALTY)
EASY = (12,4,25)
MIDDLE = (9,3,40)
HARD = (6,2,75)