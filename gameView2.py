import arcade
import PIL
import math
from player2 import Player
from globalVars import *
from physicsEngine import PhysicsEngine
from challenge import Challenge
from background import Background

# TODO:
# NPC diolouge: press E to interact, 3 multiple choice questions, if failed lose a life (3 lives total) and exit diolouge
# questions are based on the value of self.level.


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        """
        set all initial conditions to null values to clear the way for a new game
        """
        self.level = -1
        self.questions_wrong = 0

        self.list_of_backgrounds = []
        self.background1 = Background(0)
        self.background1.texture = arcade.load_texture('Images/background.jpg')
        self.list_of_backgrounds.append(self.background1)
        self.background2 = Background(1 * BACKGROUND_WIDTH)
        self.background2.texture = arcade.load_texture('Images/background.jpg')
        self.list_of_backgrounds.append(self.background2)
        self.background3 = Background(2 * BACKGROUND_WIDTH)
        self.background3.texture = arcade.load_texture('Images/background.jpg')
        self.list_of_backgrounds.append(self.background3)

        # Sprite lists
        self.list_of_sprite_lists = []
        self.player_list = None
        self.barrier_list = None
        self.npc_list = None
        self.hazard_list = None
        self.objective_list = None

        self.player = None

        # Keyboard keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """
        set up the initial conditions of the level
        """
        self.level += 1

        # Initialize the sprite lists and add them to the list of sprite lists
        self.player_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()
        self.hazard_list = arcade.SpriteList()
        self.objective_list = arcade.SpriteList()
        self.list_of_sprite_lists.append(self.player_list)
        self.list_of_sprite_lists.append(self.barrier_list)
        self.list_of_sprite_lists.append(self.npc_list)
        self.list_of_sprite_lists.append(self.hazard_list)
        self.list_of_sprite_lists.append(self.objective_list)

        # self.player = Player()
        # self.player_list.append(self.player)

        self.createMap(level_templates[self.level])

        # create a temporary list of objects the player will collide with
        # to be passed as a parameter to the physics engine
        temp_list = arcade.SpriteList()
        for barrier in self.barrier_list:
            temp_list.append(barrier)
        for npc in self.npc_list:
            temp_list.append(npc)

        self.physics_engine = PhysicsEngine(
            self.player, temp_list, GRAVITY, FRICTION, DRAG, max_move_speed=PLAYER_MAX_MOVEMENT_SPEED)

    def on_draw(self):
        """
        Render objects to the screen
        """

        arcade.start_render()

        for background in self.list_of_backgrounds:
            arcade.draw_texture_rectangle(
                background.center_x, background.center_y, BACKGROUND_WIDTH, SCREEN_HEIGHT, background.texture, 0, 255)

        for spriteList in self.list_of_sprite_lists:
            spriteList.draw()

        # self.player_list.draw()

    def on_update(self, delta_time):
        """
        Update the game conditions
        """

        self.move_frame()

        # Calculate speed based on the keys pressed
        self.player.change_x = 0
        self.player.change_y = 0
        if self.up_pressed and not self.down_pressed:
            if not self.physics_engine.in_free_fall:
                self.player.change_y = PLAYER_JUMP_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

        # self.player_list.animate()

        self.physics_engine.update()

    def createMap(self, map_template):
        map = PIL.Image.open(map_template)
        pix = map.load()
        # iterate through each pixel in the map image
        found_player = False
        for x in range(map.size[0]):
            for y in range(map.size[1]):
                if pix[x, y] == (255, 255, 255, 255):
                    # white, do nothing
                    pass
                elif pix[x, y] == (0, 0, 0, 255):
                    # black, place a barrier
                    self.barrier = arcade.Sprite('Images/platform.png')
                    self.barrier.bottom = y * 75
                    self.barrier.left = x * 75
                    self.barrier_list.append(self.barrier)
                elif pix[x, y] == (255, 0, 0, 255):
                    # red, place a npc
                    self.npc = arcade.Sprite(':resources:images/alien/alienBlue_front.png')
                    self.npc.bottom = y * 75
                    self.npc.left = x * 75
                    self.npc_list.append(self.npc)
                elif pix[x, y] == (0, 0, 255, 255) and not found_player:
                    # blue, place the player
                    # self.player = arcade.Sprite(
                    # ":resources:images/animated_characters/male_person/malePerson_idle.png")
                    self.player.bottom = y * 75
                    self.player.left = x * 75
                    self.player_list.append(self.player)
                    found_player = True

    def on_key_press(self, key, modifiers):
        """ User control """
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, mods):
        """ User control """
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def move_frame(self):
        """ move the frame based on player position """
        if self.player.center_x > 500:
            for background in self.list_of_backgrounds:
                background.center_x -= ((self.player.center_x - 500) / 3) / 4
            for spriteList in self.list_of_sprite_lists:
                for sprite in spriteList.sprite_list:
                    sprite.center_x -= (self.player.center_x - 500) / 3
        elif self.player.center_x < 300:
            for background in self.list_of_backgrounds:
                background.center_x += (abs(self.player.center_x - 300) * math.sqrt(3)) / 4
            for spriteList in self.list_of_sprite_lists:
                for sprite in spriteList.sprite_list:
                    sprite.center_x += abs(self.player.center_x - 300) * math.sqrt(3)
