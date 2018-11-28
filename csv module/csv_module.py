import csv
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def convert(obj):
    return {"x": obj.x, "y": obj.y}


pt = [Point(np.random.randint(0, 1000) - 500, np.random.randint(0, 1000) - 500) for _ in range(100)]

with open("points.csv", 'w', encoding='Big5', newline='') as csvfile:
    fieldnames = ['x', 'y']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in pt:
        writer.writerow(convert(i))

pt2 = []
with open("points.csv", 'r', encoding='Big5', newline='') as csvfile:  # encoding='utf-8'
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in reader:
        pt2.append(Point(row[0], row[1]))

for p in pt2:
    print('x:{} y:{}'.format(p.x, p.y))
