class myChain1:
    def __init__(self, *lst):
        self.p = lst

    def __iter__(self):
        for i in self.p:
            for j in i:
                yield j


for i in myChain1([1], [2, 2], [], [[3], 3, 3]):
    print(i)
# 1
# 2
# 2
# [3]
# 3
# 3

class myChain2:
    def __init__(self, *lst):
        self.p = lst

    def __iter__(self):
        self.iter_p = iter(self.p)
        a = next(self.iter_p)
        while len(a) == 0:
            a = next(self.iter_p)
        self.iter_pp = iter(a)
        return self

    def __next__(self):
        try:
            v = next(self.iter_pp)
            return v
        except StopIteration:
            a = next(self.iter_p)
            while len(a) == 0:
                a = next(self.iter_p)
            self.iter_pp = iter(a)
            v = next(self.iter_pp)
            return v


for i in myChain2([1], [2, 2], [], [[3], 3, 3]):
    print(i)
# 1
# 2
# 2
# [3]
# 3
# 3

class myChain3:
    def __init__(self, *args):
        self.lists = self.flatten(list(args))

    def __iter__(self):
        return self

    def __next__(self):
        if self.lists:
            l = self.lists
            self.lists = self.lists[1:]
            return l[0]
        else:
            raise StopIteration

    def flatten(self, s):
        if s:
            return self.flatten(s[0]) + (self.flatten(s[1:]) if len(s) > 1 else []) if type(s) is list else [s]
        else:
            return []


for i in myChain3([1], [2, 2], [], [[3], 3, 3]):
    print(i)
# 1
# 2
# 2
# 3
# 3
# 3
