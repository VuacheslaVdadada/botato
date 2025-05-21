import random


def shot(free):
    player = random.randint(1, free)
    bullet = random.randint(1, free)
    if player == bullet:
        return False
    return True
    