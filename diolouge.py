import arcade
import random
from globalVars import *


class Diolouge:
    def __init__(self, level):
        self.level = level
        self.multiplier = random.randint(0, 9)
        self.answer = self.level * self.multiplier
        valid = False
        self.correct_index = random.randint(0, 3)
        self.multiple_choice = [-1, -1, -1, -1]
        while valid == False:
            self.multiple_choice = [-1, -1, -1, -1]
            self.multiple_choice[self.correct_index] = self.answer
            for i in range(4):
                if self.multiple_choice[i] == -1:
                    self.multiple_choice[i] = random.randint(0, 99)
            if len(set(self.multiple_choice)) == len(self.multiple_choice):
                valid = True
