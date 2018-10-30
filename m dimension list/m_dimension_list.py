def create_mdl(tp, default=None):
    a = []
    if tp:
        for _ in range(tp[0]):
            a.append(create_mdl(tp[1:], default))
    else:
        return default
    return a


a = create_mdl((2, 3), 0)
a[0][0] = 1
print(a)
# [[1, 0, 0], [0, 0, 0]]
a = create_mdl((4, 3, 2), 1)
a[0][0][0] = 0
print(a)
# [[[0, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]]]
