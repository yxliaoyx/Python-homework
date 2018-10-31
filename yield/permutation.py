def perm(a):
    if (len(a) > 1):
        for index, item in enumerate(a):
            new_list = a[:]
            del (new_list[index])
            new_list.insert(0, item)
            for resto in perm(new_list[1:]):
                if (new_list[:1] + resto != a):
                    yield new_list[:1] + resto
    yield a


for idx, p in enumerate(perm([1, 2, 3])):
    print(idx, p)
# 0 [1, 3, 2]
# 1 [2, 3, 1]
# 2 [2, 1, 3]
# 3 [3, 2, 1]
# 4 [3, 1, 2]
# 5 [1, 2, 3]
