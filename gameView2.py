from diolouge import Diolouge
import arcade
import PIL
import math
import time
from arcade.arcade_types import Color
from arcade.key import F
from globalVars import *
from physicsEngine import PhysicsEngine
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
        self.in_diolouge = False
        self.near_npc = None
        self.diolouge = None
        self.show_correct = False
        self.show_incorrect = False
        self.show_level = False

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
        self.objective = None

        # Textures
        self.diolouge_box_texture = arcade.load_texture('Images/text_box.png')

        # Keyboard keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.interact_pressed = False


    def setup(self):
        """
        set up the initial conditions of the level
        """
        self.level += 1

        self.in_diolouge = False
        self.near_npc = None
        self.diolouge = None
        self.show_correct = False
        self.show_incorrect = False
        self.show_level = True
        self.lives = 3

        # Sprite lists
        self.list_of_sprite_lists = []
        self.player_list = None
        self.barrier_list = None
        self.npc_list = None
        self.hazard_list = None
        self.objective_list = None
        self.player = None
        self.objective = None

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

        # Initialize the sprite lists and add them to the list of sprite lists
        self.player_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()
        self.hazard_list = arcade.SpriteList()
        self.objective_list = arcade.SpriteList()
        self.list_of_sprite_lists.append(self.player_list)
        self.list_of_sprite_lists.append(self.wall_list)
        self.list_of_sprite_lists.append(self.npc_list)
        self.list_of_sprite_lists.append(self.hazard_list)
        self.list_of_sprite_lists.append(self.objective_list)

        self.createMap(level_templates[self.level])

        # create a temporary list of objects the player will collide with
        # to be passed as a parameter to the physics engine

        self.physics_engine = PhysicsEngine(self.player, GRAVITY, FRICTION, DRAG, max_move_speed=PLAYER_MAX_MOVEMENT_SPEED)

    def on_draw(self):
        """
        Render objects to the screen
        """

        arcade.start_render()

        for background in self.list_of_backgrounds:
            arcade.draw_texture_rectangle(background.center_x, background.center_y, BACKGROUND_WIDTH, SCREEN_HEIGHT, background.texture, 0, 255)

        for spriteList in self.list_of_sprite_lists:
            spriteList.draw()

        if self.in_diolouge:
            arcade.draw_texture_rectangle(1000, 300, 400, 500, self.diolouge_box_texture)
            arcade.draw_text(f'{self.diolouge.multiplier} x {self.level}', 1000, 475, arcade.color.BLACK, 35)
            arcade.draw_text(str(self.diolouge.multiple_choice[0]), 1000, 400, arcade.color.BLACK, 35, width=45, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text(str(self.diolouge.multiple_choice[1]), 1150, 250, arcade.color.BLACK, 35, width=45, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text(str(self.diolouge.multiple_choice[2]), 1000, 100, arcade.color.BLACK, 35, width=45, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text(str(self.diolouge.multiple_choice[3]), 850, 250, arcade.color.BLACK, 35, width=45, align="center", anchor_x="center", anchor_y="center")

        arcade.draw_text(f'Lives: {self.lives}', 10, 680, arcade.color.DARK_RED, 35)

        if self.near_npc != None and self.in_diolouge != True:
            arcade.draw_text('Press E to interact with NPC', 400, 600, arcade.color.BLACK, 24)

        if self.show_correct:
            arcade.draw_text('Correct!', 350, 400, arcade.color.GREEN, 40)
            self.show_correct = False

        if self.show_incorrect:
            arcade.draw_text('Incorrect!', 350, 400, arcade.color.CRIMSON, 40)
            self.show_incorrect = False

        if self.show_level:
            arcade.draw_text(f'Level {self.level}', 350, 400, arcade.color.BLACK, 90)
        


    def on_update(self, delta_time):
        """
        Update the game conditions
        """

        self.move_frame()

        if self.near_npc != None and self.interact_pressed:
            self.in_diolouge = True
            self.diolouge = Diolouge(self.level)

        # diolouge and game logic
        if self.in_diolouge:
            selection = None
            if self.up_pressed:
                selection = 0
            elif self.right_pressed:
                selection = 1
            elif self.down_pressed:
                selection = 2
            elif self.left_pressed:
                selection = 3
            if selection == self.diolouge.correct_index:
                self.show_correct = True
                self.on_draw()
                arcade.finish_render()
                time.sleep(1.3)
                self.npc_list.remove(self.near_npc)
                self.barrier_list.remove(self.near_npc)
                self.near_npc = None
                self.in_diolouge = False
            elif selection != None:
                self.lives -= 1
                self.show_incorrect = True
                self.on_draw()
                arcade.finish_render()
                time.sleep(1.3)
                self.in_diolouge = False

        else:
            if self.npc_list.__len__() < 1:
                self.near_npc = None
            shortest_distance = 99999999
            shortest_distance_npc = None
            for npc in self.npc_list:
                current_distance = math.sqrt((self.player.center_x - npc.center_x)**2 + (self.player.center_y - npc.center_y)**2)
                if current_distance < shortest_distance:
                    shortest_distance = current_distance
                    shortest_distance_npc = npc
            if shortest_distance < 250:
                self.near_npc = shortest_distance_npc
            else:
                self.near_npc = None

                # Calculate speed based on keys pressed
            self.player.change_x = 0
            self.player.change_y = 0
            if self.up_pressed and not self.down_pressed:
                if not self.physics_engine.in_free_fall:
                    self.player.change_y = PLAYER_JUMP_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player.change_x = -PLAYER_MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player.change_x = PLAYER_MOVEMENT_SPEED

        if self.show_level and (self.left_pressed or self.right_pressed or self.up_pressed or self.down_pressed):
            self.show_level = False

        if self.player.center_y < 10:
            self.lives = 0

        if self.lives < 1:
            self.level = self.level - 1
            self.setup()

        if math.sqrt((self.player.center_x - self.objective.center_x)**2 + (self.player.center_y - self.objective.center_y)**2) < 100:
            if len(level_templates) - 1 <= self.level:
                victory = VictoryView()
                self.window.show_view(victory)
            else:
                self.setup()

        self.physics_engine.update(self.barrier_list)

    def createMap(self, map_template):
        map = PIL.Image.open(map_template)
        pix = map.load()
        # iterate through each pixel in the map image
        found_player = False
        for x in range(map.size[0]):
            for y in range(map.size[1]):
                if pix[x,y] == (255, 255, 255, 255):
                    # white, do nothing
                    pass
                elif pix[x,y] == (0,0,0,255):
                    # black, place a barrier
                    self.barrier = arcade.Sprite('Images/platform.png')
                    self.barrier.bottom = y * 75
                    self.barrier.left = x * 75
                    self.barrier_list.append(self.barrier)
                    self.wall_list.append(self.barrier)
                elif pix[x,y] == (255,0,0,255):
                    # red, place a npc
                    self.npc = arcade.Sprite(':resources:images/alien/alienBlue_front.png')
                    self.npc.bottom = y * 75
                    self.npc.left = x * 75
                    self.npc_list.append(self.npc)
                    self.barrier_list.append(self.npc)
                elif pix[x,y] == (0,0,255,255) and not found_player:
                    # blue, place the player
                    self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png")
                    self.player.bottom = y * 75
                    self.player.left = x * 75
                    self.player_list.append(self.player)
                    found_player = True
                elif pix[x,y] == (0,255,0,255):
                    # green, place the objective
                    self.objective = arcade.Sprite("Images/objective.png")
                    self.objective.bottom = y * 75
                    self.objective.left = x * 75
                    self.objective_list.append(self.objective)

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
        elif key == arcade.key.E:
            self.interact_pressed = True

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
        elif key == arcade.key.E:
            self.interact_pressed = False

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


class VictoryView(arcade.View):
    """ Class for the victory menu view """
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('Images/victory.png')
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
    def on_draw(self):
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
    def on_mouse_press(self, x, y, btn, mod):
        start_menu = StartMenuView()
        self.window.show_view(start_menu)

class StartMenuView(arcade.View):
    """ Class for the main menu view """
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('Images/title.png')
        self.mouse_pressed = False
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
    def on_draw(self):
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
    def on_mouse_press(self, x, y, btn, mod):
        if self.mouse_pressed:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        else:
            self.texture = arcade.load_texture('Images/tutorial.png')
            self.mouse_pressed = True
    def on_key_release(self, key, mods):
        if key == arcade.key.L:
            user_input = arcade.gui.UIInputBox(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 300)
            user_input.render()