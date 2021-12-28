from itertools import combinations


def choose_best_sum(t, k, ls):
    try:
        return max(sum(x) for x in combinations(ls, k) if sum(x) <= t)
    except:
        return None