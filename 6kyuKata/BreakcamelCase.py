def solution(s):
    return "".join(x if x == x.lower() else " " + x for x in s)
