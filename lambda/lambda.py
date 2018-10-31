import math
from functools import reduce

a = [1, -2, 3, -4, 5, -6, -7, -8, 9, 10]

for i in filter(lambda x: x > 0 and x % 3 == 0, a):
    print(i)
# 3
# 9

for i in map(lambda x: math.exp(-x), a):
    print(i)
# 0.36787944117144233
# 7.38905609893065
# 0.049787068367863944
# 54.598150033144236
# 0.006737946999085467
# 403.4287934927351
# 1096.6331584284585
# 2980.9579870417283
# 0.00012340980408667956
# 4.5399929762484854e-05

print(reduce(lambda x, y: abs(x) + abs(y), a))
# 55
