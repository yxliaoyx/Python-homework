import numpy as np
import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def convert(obj):
    return {"x": obj.x, "y": obj.y}


def custom_function(obj):
    return Point(obj['x'], obj['y'])


pt = [Point(np.random.randint(0, 1000) - 500, np.random.randint(0, 1000) - 500) for _ in range(100)]

with open('points.txt', 'w') as f:
    json.dump(pt, f, default=convert)

with open('points.txt', 'r') as f:
    pt2 = json.load(f, object_hook=custom_function)

for p in pt2:
    print('x:{} y:{}'.format(p.x, p.y))
