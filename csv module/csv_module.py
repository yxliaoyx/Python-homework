import csv
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = [Point(np.random.randint(0, 1000) - 500, np.random.randint(0, 1000) - 500) for _ in range(100)]

with open("points.csv", 'w', encoding='Big5', newline='') as csvfile:
    fieldnames = ['x', 'y']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar="'")
    writer.writeheader()

    for i in pt:
        writer.writerow({'x': i.x, 'y': i.y})

with open("points.csv", 'r', encoding='Big5', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar="'")
    pt2 = [Point(row['x'], row['y']) for row in reader]

for p in pt2:
    print('x:{} y:{}'.format(p.x, p.y))
