import arcade
import random
from globalVars import *

PRIMES = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]


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
                    prime = True
                    while prime:
                        self.multiple_choice[i] = random.randint(0, 81)
                        if not self.multiple_choice[i] in PRIMES:
                            prime = False
            if len(set(self.multiple_choice)) == len(self.multiple_choice):
                valid = True
