from datetime import datetime
def period_is_late(last,today,cycle_length):
    return (today - last).days > cycle_length



print(period_is_late(datetime(2016, 6, 13), datetime(2016, 8, 6), 35))