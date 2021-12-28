def tower_builder(n_floors):
    floors = []
    constructor = (n_floors * 2) -1
    for value in range(1, 2*n_floors, 2):
        stars = value * '*'
        result = stars.center(constructor)
        floors.append(result)
    return floors

print(tower_builder(4))