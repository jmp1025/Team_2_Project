import arcade

# img original dimensions: 131 x 188
# new dimensions maintain aspect ratio
IMG_WIDTH = 40
IMG_HEIGHT = 57


class Enemy:
    """
    used for creating player object
    """

    def __init__(self):
        super().__init__()
        # x and y coordinates to start the player in the bottom
        # left corner of the screen
        self.x = 1160.0  # x axis coordinate
        self.y = 40.0  # y axis coordinate
        self.move = 2  # contorls the players speed
        self.radius = 30  # used for collision detection
        self.alive = True

    def draw(self):
        """
        draws the player image to the screen
        """
        img = ":resources:images/alien/alienBlue_front.png"
        texture = arcade.load_texture(img)

        # img original dimensions: 131 x 188
        arcade.draw_texture_rectangle(self.x, self.y, IMG_WIDTH,
                                      IMG_HEIGHT, texture, 0, 255)
