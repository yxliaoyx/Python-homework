a, b, c = 2, 4, 8


def func():
    global a, c
    a, b, c = 3, 6, 9

    def inner_func():
        nonlocal b
        global c
        a, b, c = 5, 10, 15
        print("inner_func:{},{},{}".format(a, b, c))

    inner_func()
    print("func:{},{},{}".format(a, b, c))


print("before func:{},{},{}".format(a, b, c))
func()
print("after func:{},{},{}".format(a, b, c))
# before func:2,4,8
# inner_func:5,10,15
# func:3,10,15
# after func:3,4,15
