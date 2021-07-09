import arcade
from globalVars import *

# img original dimensions: 131 x 188
# new dimensions maintain aspect ratio


def load_texture_pair(filename):
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class Player(arcade.Sprite):
    """
    used for creating player object
    """

    def __init__(self):
        super().__init__()
        self.direction = PLAYER_FACE_RIGHT
        self.current_texture = 0
        self.scale = PLAYER_SCALE
        self.jumping = False
        path = ":resources:images/animated_characters/male_person/malePerson"
        self.idle = load_texture_pair(f"{path}_idle.png")
        self.walk = []
        for i in range(8):
            texture = load_texture_pair(f"{path}_walk{i}.png")
            self.walk.append(texture)
        self.jump = load_texture_pair(f"{path}_jump.png")
        self.fall = load_texture_pair(f"{path}_fall.png")

        self.texture = self.idle[0]
        self.set_hit_box(self.texture.hit_box_points)

    def animate(self, delta_time: float = 1/60):
        if self.change_x < 0 and self.direction == PLAYER_FACE_RIGHT:
            self.direction = PLAYER_FACE_LEFT
        elif self.change_x > 0 and self.direction == PLAYER_FACE_LEFT:
            self.direction = PLAYER_FACE_RIGHT

        if self.change_y > 0:
            self.texture = self.jump[self.direction]
            return
        elif self.change_y < 0:
            self.texture = self.fall[self.direction]
            return

        if self.change_x == 0:
            self.texture = self.idle[self.direction]
            return

        self.current_texture += 1
        if self.current_texture > 7 * PLAYER_UPDATE:
            self.current_texture = 0
        frame = int(self.current_texture // PLAYER_UPDATE)
        direction = self.direction
        self.texture = self.walk[frame][direction]
