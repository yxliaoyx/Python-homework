import itertools

alist = [1, 2, -1, 2, -3, 5, 6, -4]

for item in alist:
    print(item)
# 1
# 2
# -1
# 2
# -3
# 5
# 6
# -4

for index, item in enumerate(alist):
    print(index, item)
# 0 1
# 1 2
# 2 -1
# 3 2
# 4 -3
# 5 5
# 6 6
# 7 -4

for i in range(len(alist) - 1, -1, -1):
    if alist[i] < 0:
        del alist[i]
print(alist)
# [1, 2, 2, 5, 6]

alist = [1, 2, 3, 4]
blist = [6, 7, 8, 9]
clist = [11, 2, 3, 1]
for a, b, c in zip(alist, blist, clist):
    print(a, b, c)
# 1 6 11
# 2 7 2
# 3 8 3
# 4 9 1

for item in itertools.repeat('Sun, Mon,Tue, Wed, Thu, Fri, Sat,', 3):
    print(item)
# Sun, Mon,Tue, Wed, Thu, Fri, Sat,
# Sun, Mon,Tue, Wed, Thu, Fri, Sat,
# Sun, Mon,Tue, Wed, Thu, Fri, Sat,
