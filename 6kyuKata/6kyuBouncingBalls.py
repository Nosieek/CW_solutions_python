def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window > h:
        return -1
    result = h
    i = 1
    while window < result:
        result *= bounce
        if result > window:
            i+=2
    return i
print(bouncing_ball(30,0.75,1.5))