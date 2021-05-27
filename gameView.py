import arcade
import math
import random


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        # self.background = arcade.load_texture()
        # self.held_keys = set()
        # self.game = GAME_START

    def on_draw(self):
        arcade.start_render()
        pass

    def update(self, delta_time):
        self.check_keys()
        pass

    def check_keys(self):
        pass

    def on_key_press(self, key: int, modifiers: int):
        pass

    def on_key_release(self, key: int, modifiers: int):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
