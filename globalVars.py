import arcade

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Adventure in Multiplication Land (TM)"
PYGUYS = ":resources:images/pyGuys/"
GRAVITY = -1
FRICTION = 1.15
DRAG = 1.023
PLAYER_JUMP_SPEED = 20
PLAYER_MOVEMENT_SPEED = 0.8
PLAYER_MAX_MOVEMENT_SPEED = 23
PLAYER_FACE_LEFT = 1
PLAYER_FACE_RIGHT = 0
PLAYER_UPDATE = 5
PLAYER_SCALE = 1
BACKGROUND_WIDTH = 2000

LEVEL_TEMPLATES = ['C:/Users/jmp10/Documents/GitHub/Team_2_Project/Images/map0.png', 'C:/Users/jmp10/Documents/GitHub/Team_2_Project/Images/map2.png',
                   'C:/Users/jmp10/Documents/GitHub/Team_2_Project/Images/map3.png', 'C:/Users/jmp10/Documents/GitHub/Team_2_Project/Images/map4.png']

SOUND_ERROR = arcade.load_sound(":resources:sounds/error5.wav")
SOUND_CORRECT = arcade.load_sound(":resources:sounds/coin1.wav")
SOUND_NO_LIVES = arcade.load_sound(":resources:sounds/gameover2.wav")
WIN_LEVEL = arcade.load_sound(":resources:sounds/secret4.wav")
GAME_VICTORY = arcade.load_sound(":resources:sounds/upgrade5.wav")
MUSIC_VOLUME = 0.5
