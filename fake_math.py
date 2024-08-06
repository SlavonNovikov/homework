from math import inf


def fake_divide(a, b):
    if b == 0:
        return inf
    else:
        return a / b
