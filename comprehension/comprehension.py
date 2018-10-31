import itertools
import time

t = time.time()
print([(a, b, c) for a in range(1, 100) for b in range(1, 100) for c in range(1, 100) if
       (a ** 2 + b ** 2 == c ** 2) and (a <= b <= c)])
print(time.time() - t)

t = time.time()
print([side for side in itertools.combinations(range(1, 100), 3) if
       (side[0] ** 2 + side[1] ** 2 == side[2] ** 2) and (side[0] <= side[1] <= side[2])])
print(time.time() - t)

print({key: 0 for key in [key for r in range(6) for key in itertools.combinations(['A', 'B', 'C', 'D', 'E'], r)]})
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (13, 84, 85), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (16, 63, 65), (18, 24, 30), (18, 80, 82), (20, 21, 29), (20, 48, 52), (21, 28, 35), (21, 72, 75), (24, 32, 40), (24, 45, 51), (24, 70, 74), (25, 60, 65), (27, 36, 45), (28, 45, 53), (30, 40, 50), (30, 72, 78), (32, 60, 68), (33, 44, 55), (33, 56, 65), (35, 84, 91), (36, 48, 60), (36, 77, 85), (39, 52, 65), (39, 80, 89), (40, 42, 58), (40, 75, 85), (42, 56, 70), (45, 60, 75), (48, 55, 73), (48, 64, 80), (51, 68, 85), (54, 72, 90), (57, 76, 95), (60, 63, 87), (65, 72, 97)]
# 0.9035818576812744
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (13, 84, 85), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (16, 63, 65), (18, 24, 30), (18, 80, 82), (20, 21, 29), (20, 48, 52), (21, 28, 35), (21, 72, 75), (24, 32, 40), (24, 45, 51), (24, 70, 74), (25, 60, 65), (27, 36, 45), (28, 45, 53), (30, 40, 50), (30, 72, 78), (32, 60, 68), (33, 44, 55), (33, 56, 65), (35, 84, 91), (36, 48, 60), (36, 77, 85), (39, 52, 65), (39, 80, 89), (40, 42, 58), (40, 75, 85), (42, 56, 70), (45, 60, 75), (48, 55, 73), (48, 64, 80), (51, 68, 85), (54, 72, 90), (57, 76, 95), (60, 63, 87), (65, 72, 97)]
# 0.15358924865722656
# {(): 0, ('A',): 0, ('B',): 0, ('C',): 0, ('D',): 0, ('E',): 0, ('A', 'B'): 0, ('A', 'C'): 0, ('A', 'D'): 0, ('A', 'E'): 0, ('B', 'C'): 0, ('B', 'D'): 0, ('B', 'E'): 0, ('C', 'D'): 0, ('C', 'E'): 0, ('D', 'E'): 0, ('A', 'B', 'C'): 0, ('A', 'B', 'D'): 0, ('A', 'B', 'E'): 0, ('A', 'C', 'D'): 0, ('A', 'C', 'E'): 0, ('A', 'D', 'E'): 0, ('B', 'C', 'D'): 0, ('B', 'C', 'E'): 0, ('B', 'D', 'E'): 0, ('C', 'D', 'E'): 0, ('A', 'B', 'C', 'D'): 0, ('A', 'B', 'C', 'E'): 0, ('A', 'B', 'D', 'E'): 0, ('A', 'C', 'D', 'E'): 0, ('B', 'C', 'D', 'E'): 0, ('A', 'B', 'C', 'D', 'E'): 0}