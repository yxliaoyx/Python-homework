class P2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class P1D:
    def __init__(self, x):
        self.x = x


def distance(p1, p2):
    if hasattr(p1, 'x') and hasattr(p1, 'y') and hasattr(p2, 'x') and hasattr(p2, 'y'):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    else:
        raise AttributeError()


p2d1 = P2D(0, 0)
p2d2 = P2D(1, 1)

print(distance(p2d1, p2d2))

p1d1 = P1D(0)
p1d2 = P1D(1)

print(distance(p1d1, p1d2))
