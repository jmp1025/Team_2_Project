import arcade
from gameView2 import GameView
from globalVars import *

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