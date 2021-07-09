import arcade
import random
from arcade.texture import load_texture

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "text_box"

OPTION_COUNT = 4
TEXT_BOX_SCALING = 1
CHOOSE_OPTION_SCALING = 0.5


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # sprite lists
        self.text_box_list = None
        self.choose_option_list = None

        # set up text box
        self.text_box = None

    def setup(self):
        position = 90
        option_1 = True
        option_2 = True
        option_3 = True
        self.text_box_list = arcade.SpriteList()
        self.choose_option_list = arcade.SpriteList()

        # set up text box
        self.text_box = arcade.Sprite("text_box.png", scale=1.5)

        self.text_box.center_x = SCREEN_WIDTH // 2
        self.text_box.center_y = SCREEN_HEIGHT // 2
        self.text_box.scale = 1.5

        self.text_box_list.append(self.text_box)

        for x in range(OPTION_COUNT):
            option = arcade.Sprite("option_choice.png", scale=0.5)
            if option.center_x == self.text_box.center_x and  \
                    option.center_y == self.text_box.center_y + position or option_1:

                option.center_x = self.text_box.center_x
                option.center_y = self.text_box.center_y + position

                self.choose_option_list.append(option)
                print("pass")
                option_1 = False
            elif option.center_x == self.text_box.center_x + position and \
                    option.center_y == self.text_box.center_y or option_2:

                option.center_x = self.text_box.center_x + position
                option.center_y = self.text_box.center_y

                print("dog")

                self.choose_option_list.append(option)
                option_2 = False
            elif option.center_x == self.text_box.center_x - position and \
                    option.center_y == self.text_box.center_y or option_3:

                option.center_x = self.text_box.center_x - position
                option.center_y = self.text_box.center_y
                print("cat")

                self.choose_option_list.append(option)
                option_3 = False
            else:
                option.center_x = self.text_box.center_x
                option.center_y = self.text_box.center_y - position

                self.choose_option_list.append(option)

                # back ground color
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def on_draw(self):

        # needs to happen before drawing
        arcade.start_render()
        self.text_box_list.draw()
        self.choose_option_list.draw()

        arcade.draw_text(f"{random.randint(0, 200)}", random.randint(
            0, 200), random.randint(0, 200), arcade.color.BLACK, 20)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
