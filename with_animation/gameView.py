import arcade
import math
import random
from player import Player
from enemy import Enemy
from challenge import Challenge


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

GAME_START = 1
GAME_PLAY = 2
GAME_OVER = 3
GAME_WIN = 4












class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        # self.background = arcade.load_texture()
        self.game = GAME_START
        self.held_keys = set()
        # self.s_width = width
        # self.s_height = height
        self.player = Player()
        self.enemy = Enemy()
        self.challenge = Challenge()

    def new_game(self):
        """
        repopulate objects if player wants to play again
        """
        # Needs stuff to draw

        self.game = GAME_PLAY

    def draw_begin(self):
        """
        draw the start screen
        """

        arcade.draw_text("Press \"Enter\" To Play \n\nPress \"Q\" To Quit", 0,
                         SCREEN_HEIGHT//2.6, arcade.color.WHITE, 18,
                         SCREEN_WIDTH, "center")

    def draw_end(self, status):
        """
        end screen dependent on win or lose status
        """
        if status == GAME_WIN:
            arcade.draw_text("You Won!", 0,
                             SCREEN_HEIGHT//1.8, arcade.color.WHITE, 24,
                             SCREEN_WIDTH, "center")
            arcade.draw_text("Press \"Enter\" To Play Again"
                             "\n\nPress \"Q\" To Quit", 0, SCREEN_HEIGHT//2.6,
                             arcade.color.WHITE, 18, SCREEN_WIDTH, "center")

        elif status == GAME_OVER:
            arcade.draw_text("Oh No!  You Lost", 0,
                             SCREEN_HEIGHT//1.8, arcade.color.WHITE, 24,
                             SCREEN_WIDTH, "center")
            arcade.draw_text("Press \"Enter\" To Play Again"
                             "\n\nPress \"Q\" To Quit",
                             0, SCREEN_HEIGHT//2.6, arcade.color.WHITE, 18,
                             SCREEN_WIDTH, "center")

    def on_draw(self):
        arcade.start_render()

        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0,
                                          arcade.color.DARK_SPRING_GREEN)

        if self.game == GAME_START:
            self.draw_begin()
        if self.enemy.challenge:
            # self.challenge.easy()
            self.challenge.draw()
        """
        elif not self.ship.alive:
            self.game = GAME_OVER
            self.draw_end(self.game)
        elif not self.asteroids:
            self.game = GAME_WIN
            self.draw_end(self.game)
        """

        if self.game == GAME_PLAY:
            self.player.draw()
            self.enemy.draw()

    def on_update(self, delta_time):
        self.check_keys()
        if self.game == GAME_PLAY:
            self.check_collisions()

    def check_collisions(self):
        """
        Use this function to check for collisions with the player image
        """
        if self.player.alive and self.enemy.alive:
            too_close = self.player.radius + self.enemy.radius
            if (abs(self.player.x - self.enemy.x) < too_close and
                    abs(self.player.y - self.enemy.y) < too_close):
                self.enemy.challenge = True

    def check_keys(self):
        if arcade.key.LEFT in self.held_keys:
            self.player.move_left()

        if arcade.key.RIGHT in self.held_keys:
            self.player.move_right(self.width)

    def on_key_press(self, key: int, modifiers: int):
        """
        Use this function to setup key control that won't be held down
        """
        self.held_keys.add(key)

        # statement for game view conrols
        if key == arcade.key.ENTER and self.game == GAME_START:
            self.game = GAME_PLAY
        elif key == arcade.key.ENTER and self.game == GAME_OVER:
            self.new_game()
        elif key == arcade.key.ENTER and self.game == GAME_WIN:
            self.new_game()

        #  pressing Q will end the game and close the window
        if key == arcade.key.Q:
            quit()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
