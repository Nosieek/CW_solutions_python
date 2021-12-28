import math

def tor(friends, friends_towns, home_to_town_distancec):
    x = 0
    last_x = 0
    friends_towns = [[friend, town] for friend, town in friends_towns if friend in friends]
    for f, t in friends_towns:
        if t in home_to_town_distancec:
            _x = home_to_town_distancec[t]
            if x == 0:
                x = _x
                last_x = _x
            else:
                x += math.sqrt(_x ** 2 - last_x ** 2)
                last_x = _x
    x += home_to_town_distancec[t]
    return int(math.floor(x))
