def number(bus_stops):
    return sum((stage[0] - stage[1]) for stage in bus_stops)


print(number([[10,0],[3,5],[5,8]]))