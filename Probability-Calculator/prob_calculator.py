import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        
        drawn = []
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            drawn.append(ball)
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(sum(expected_balls.values()))
        
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
            
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
                
        if success:
            successes += 1
            
    return successes / num_experiments
