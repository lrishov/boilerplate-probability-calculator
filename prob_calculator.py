import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents = self.contents + ([key] * value)

#    def draw(self, number):
#        if number >= len(self.contents):
#            return self.contents
#
#        return random.sample(self.contents, number)

  
    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
        draws = []
        random.shuffle(self.contents)
        for i in range(0,number):
            draws.append(self.contents.pop())

        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = 0
    for i in range(0, num_experiments):
        val = copy.deepcopy(hat)
        experiment = val.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if experiment.count(key) < value:
                break
            n =  n + 1
    return n/(num_experiments * len(expected_balls))
