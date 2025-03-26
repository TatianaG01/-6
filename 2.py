import math


class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimetr() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2


class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3

    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3

    def volume(self):
        return (1 / 3) * super().square() * self.h


# Читання файлу та знаходження фігури з найбільшою мірою

def read_figures_from_file(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name, params = parts[0], list(map(float, parts[1:]))

            if name == "Triangle":
                figures.append(Triangle(*params))
            elif name == "Rectangle":
                figures.append(Rectangle(*params))
            elif name == "Circle":
                figures.append(Circle(*params))
            elif name == "Ball":
                figures.append(Ball(*params))
            elif name == "TriangularPyramid":
                figures.append(TriangularPyramid(*params))
    return figures


def find_largest_figure(figures):
    return max(figures, key=lambda f: f.volume())


# Приклад використання
figures = read_figures_from_file("input01.txt")
largest_figure = find_largest_figure(figures)
print(f"Найбільша фігура: {type(largest_figure).__name__}, міра: {largest_figure.volume()}")
