import random
import arcade


class Challenge:
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.multiplier = random.randint(0,9)
        self.answer = self.level * self.multiplier
        multiple_choice = [-1, -1, -1, -1]
        multiple_choice[random.randint(0, 3)] = self.answer
        for i in range(4):
            if multiple_choice[i] == -1:
                multiple_choice[i] = random.randint(0, 99)
        print(self.multiplier)
        print(multiple_choice)
        
