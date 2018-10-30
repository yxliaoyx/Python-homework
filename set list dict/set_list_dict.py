s = {}
print(s)

s = {1, 2, 3}
print(s)

s.add(5)
print(s)

s.remove(1)
print(s)

s = [1, 2, 3, 4]
print(s)

s.extend([5, 6, 7])
print(s)

s.append([5, 6, 7])
print(s)

t = s.copy()
print(t)


def flatten(s):
    return flatten(s[0]) + (flatten(s[1:]) if len(s) > 1 else []) if type(s) is list else [s]


print(flatten(s).count(2))
print(sum(flatten(s)))
print(max(flatten(s)))
print(min(flatten(s)))
print(sorted(flatten(s)))

x = {'a': 1, 'b': 2, 'c': 3}
print(x)

del x['a']
print(x)
# {}
# {1, 2, 3}
# {1, 2, 3, 5}
# {2, 3, 5}
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, [5, 6, 7]]
# [1, 2, 3, 4, 5, 6, 7, [5, 6, 7]]
# 1
# 46
# 7
# 1
# [1, 2, 3, 4, 5, 5, 6, 6, 7, 7]
# {'a': 1, 'b': 2, 'c': 3}
# {'b': 2, 'c': 3}
