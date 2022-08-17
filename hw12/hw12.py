# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було
# записати тільки обʼєкти класу Point. Використовуйте property
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет атрибут, що містить площу трикутника (за допомогою property).
# Для обчислень можна використати формулу Герона

class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def __str__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"


point1 = Point(0, 3)
point2 = Point(4, 0)
point3 = Point(0, 0)


class Line:

    _begin = None
    _end = None

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, begin_point):
        if not isinstance(begin_point, Point):
            raise TypeError
        self._begin = begin_point

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end_point):
        if not isinstance(end_point, Point):
            raise TypeError
        self._end = end_point

    @property
    def length(self):
        print('in length_getter')
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


line1 = Line(point2, point1)

print(line1.length)


class Triangle:

    _a = None
    _b = None
    _c = None

    def __init__(self, a_point: Point, b_point: Point, c_point: Point):
        self.a = a_point
        self.b = b_point
        self.c = c_point

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a_point):
        if not isinstance(a_point, Point):
            raise TypeError
        self._a = a_point

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b_point):
        if not isinstance(b_point, Point):
            raise TypeError
        self._b = b_point

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c_point):
        if not isinstance(c_point, Point):
            raise TypeError
        self._c = c_point

    @property
    def square(self):
        print('in square')
        ab = Line(self.a, self.b).length
        bc = Line(self.b, self.c).length
        ca = Line(self.c, self.a).length
        s = (ab + bc + ca)/2
        return (s * (s - ab) * (s - bc) * (s - ca)) ** 0.5

    def __eq__(self, other):
        return self.square == other.square

    def __gt__(self, other):
        return self.square > other.square

    def __ge__(self, other):
        return self.square >= other.square

    def __str__(self):
        return f"({self.a} {self.b} {self.c})"


triangle = Triangle(point1, point2, point3)
print(triangle)
