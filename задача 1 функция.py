
def f(x):
    if x <= -2:
        c = 1 - (x + 2) ** 2
        return c
    elif -2 < x <= 2:
        c = -x / 2
        return c
    elif 2 < x:
        c = (x - 2) ** 2 + 1
        return c



