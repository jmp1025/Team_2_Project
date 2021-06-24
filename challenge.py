import random
import arcade


class Challenge:
    def __init__(self):
        super().__init__()
        self.easy = int(random.uniform(1, 4))
        self.medium = [4, 5, 6]
        self.hard = [7, 8, 9]
        self.multiplier = int(random.uniform(1, 10))
        self.answer = 0
    """
    def easy(self):
        self.easy = random.uniform(1, 3)
        self.multiplier = random.uniform(1, 9)
        self.answer = self.easy * self.multiplier

    def medium(self):
        self.medium = random.uniform(4, 6)
        self.multiplier = random.uniform(1, 9)
        self.answer = self.medium * self.multiplier

    def hard(self):
        self.hard = random.uniform(7, 9)
        self.multiplier = random.uniform(1, 9)
        self.answer = self.hard * self.multiplier
    """

    def draw(self):
        arcade.draw_text(str(self.easy) + " * " + str(self.multiplier), 0,
                         200, arcade.color.WHITE, 18, 200, "center")
