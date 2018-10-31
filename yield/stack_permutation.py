def stackperm(a, stack=[], out=[]):
    if stack or a:
        if stack:
            yield from stackperm(a, stack[1:], out + stack[:1])
        if a:
            yield from stackperm(a[1:], a[:1] + stack, out)
    else:
        yield out


for idx, p in enumerate(stackperm([1, 2, 3])):
    print(idx, p)
# 0 [1, 2, 3]
# 1 [1, 3, 2]
# 2 [2, 1, 3]
# 3 [2, 3, 1]
# 4 [3, 2, 1]
