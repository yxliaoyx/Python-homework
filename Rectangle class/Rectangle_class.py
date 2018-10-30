class Rectangle:
    def __init__(self, x0, y0, width, height):
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __or__(self, other):
        x0 = self.x0 if self.x0 < other.x0 else other.x0
        y0 = self.y0 if self.y0 < other.y0 else other.y0
        width = (self.x0 + self.width if self.x0 + self.width > other.x0 + other.width else other.x0 + other.width) - x0
        height = (self.y0 + self.height if self.y0 + self.height > other.y0 + other.height else other.y0 + other.height) - y0
        return Rectangle(x0, y0, width, height)

    def __and__(self, other):
        x0 = self.x0 if self.x0 > other.x0 else other.x0
        y0 = self.y0 if self.y0 > other.y0 else other.y0
        width = (self.x0 + self.width if self.x0 + self.width < other.x0 + other.width else other.x0 + other.width) - x0
        height = (self.y0 + self.height if self.y0 + self.height < other.y0 + other.height else other.y0 + other.height) - y0
        return Rectangle(x0, y0, width, height)

    def __str__(self):
        return 'Rectangle: ({},{})-({},{})'.format(self.x0, self.y0, self.x0 + self.width, self.y0 + self.height)

    def __repr__(self):
        return 'Rectangle({},{},{},{})'.format(self.x0, self.y0, self.width, self.height)

    def __eq__(self, other):
        return self.x0 == other.x0 and self.y0 == other.y0 and self.width == other.width and self.height == other.height


rect1 = Rectangle(0, 0, 2, 2)
print(rect1.area)

rect2 = Rectangle(1, 1, 2, 2)
print(rect2.area)

# 涵蓋包含rect1與rect2區域的最小矩形
rect3 = rect1 | rect2
print(rect3.area)

# 剛好涵蓋rect1與rect2重疊區的矩形
rect4 = rect1 & rect2
print(rect4.area)

print(rect1)

print(rect1 == eval(repr(rect1)))
