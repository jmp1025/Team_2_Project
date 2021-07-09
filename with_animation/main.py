import arcade
from gameView2 import StartMenuView
from globalVars import *

def main():
    """ Main method """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartMenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()