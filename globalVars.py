import arcade

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 780
SCREEN_TITLE = "Adventure in Multiplication Land (TM)"
GRAVITY = -1
FRICTION = 1.1
DRAG = 1.023
PLAYER_JUMP_SPEED = 21
PLAYER_MOVEMENT_SPEED = 0.8
PLAYER_MAX_MOVEMENT_SPEED = 12
PLAYER_FACE_LEFT = 1
PLAYER_FACE_RIGHT = 0
PLAYER_UPDATE = 0.8
PLAYER_SCALE = 1
BACKGROUND_WIDTH = 2000
# PATH = "C:/Users/jmp10/Documents/GitHub/Team_2_Project/"
LEVEL_TEMPLATES =  ['Images/map0.png', 
                    'Images/map1.png', 
                    'Images/map2.png', 
                    'Images/map3.png', 
                    'Images/map4.png', 
                    'Images/map5.png', 
                    'Images/map6.png', 
                    'Images/map7.png', 
                    'Images/map8.png', 
                    'Images/map9.png',
                    ]
SOUND_ERROR = arcade.load_sound(":resources:sounds/error5.wav")
SOUND_CORRECT = arcade.load_sound(":resources:sounds/coin1.wav")
SOUND_NO_LIVES = arcade.load_sound(":resources:sounds/gameover2.wav")
WIN_LEVEL = arcade.load_sound(":resources:sounds/secret4.wav")
GAME_VICTORY = arcade.load_sound('Audio/Victory_Fanfare.mp3')
MUSIC_VOLUME = 0.5
