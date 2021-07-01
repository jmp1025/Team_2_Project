import arcade
import PIL
from globalVars import *
from physicsEngine import PhysicsEngine

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        """
        set all initial conditions to null values to clear the way for a new game
        """
        self.level = -1

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

        self.createMap(level_templates[self.level])

        self.physics_engine = PhysicsEngine(self.player, self.barrier_list, GRAVITY, FRICTION, DRAG, max_move_speed=PLAYER_MAX_MOVEMENT_SPEED)

    def on_draw(self):
        """
        Render objects to the screen
        """
        arcade.start_render()

        for spriteList in self.list_of_sprite_lists:
            spriteList.draw()


    def on_update(self, delta_time):
        """
        Update the game conditions
        """

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

        self.physics_engine.update()

    def createMap(self, map_template):
        map = PIL.Image.open(map_template)
        pix = map.load()
        # iterate through each pixel in the map image
        for x in range(map.size[0]):
            for y in range(map.size[1]):
                if pix[x,y] == (255, 255, 255,255):
                    # white, do nothing
                    pass
                elif pix[x,y] == (0,0,0,255):
                    # black, place a barrier
                    self.barrier = arcade.Sprite('Images/platform.png')
                    self.barrier.bottom = y * 75
                    self.barrier.left = x * 75
                    self.barrier_list.append(self.barrier)
                elif pix[x,y] == (0,0,255,255):
                    # blue, place the player
                    self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png")
                    self.player.bottom = y * 75
                    self.player.left = x * 75
                    self.player_list.append(self.player)

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