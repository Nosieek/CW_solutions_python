''' https://www.codewars.com/kata/588a00ad70720f2cd9000005/python '''
class Router(object):
    def __init__(self):
        self.routers = {}

    def bind(self, url, method, action):
        self.routers[(url, method)] = action

    def runRequest(self, url, method):
        return self.routers.get((url, method), lambda: 'Error 404: Not Found')()