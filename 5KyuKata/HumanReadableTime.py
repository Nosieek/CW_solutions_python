def make_readable(seconds):
    return "{}:{}:{}".format("%02d" %int(seconds//3600),
                             "%02d" %int((seconds%3600)//60),
                             "%02d" %int((seconds%3600)%60))


print(make_readable(3700))