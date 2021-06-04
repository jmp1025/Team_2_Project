import arcade
import math
import random


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
        # self.held_keys = set()
    self.game = GAME_START

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

        # more stuff here

        if self.game == GAME_START:
            self.draw_begin()

        elif not self.ship.alive:
            self.game = GAME_OVER
            self.draw_end(self.game)
        elif not self.asteroids:
            self.game = GAME_WIN
            self.draw_end(self.game)

        elif self.game == GAME_PLAY:
            # more stuff here

    def update(self, delta_time):
        self.check_keys()
        # if self.game == GAME_PLAY:

    def check_keys(self):
        pass

    def on_key_press(self, key: int, modifiers: int):
        pass

    def on_key_release(self, key: int, modifiers: int):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
