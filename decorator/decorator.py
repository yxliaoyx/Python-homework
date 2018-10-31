import time


def print_time(f):
    def new_f(*args, **kwargs):
        a = time.time()
        ans = f(*args, **kwargs)
        b = time.time()
        print('處理程序耗時: {} 秒'.format(b - a))
        return ans

    return new_f


@print_time
def f1(n=1000000):
    s = 0
    for i in range(n):
        s += i
    return s


@print_time
def f2(n=1000000):
    s = 0
    lst = list(range(n))
    for i in lst:
        s += i
    return s


print(f1())
print(f2())
