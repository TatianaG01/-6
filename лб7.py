import math

# Базовий клас
class Figure:
    def dimention(self):
        pass

    def perimetr(self):
        pass

    def square(self):
        pass

    def squareSurface(self):
        pass

    def squareBase(self):
        pass

    def height(self):
        pass

    def volume(self):
        pass

# 2D фігури

import math


class Figure:
    def dimention(self):
        pass

    def perimetr(self):
        pass

    def square(self):
        pass

    def volume(self):
        return 0  # Для плоских фігур (площа)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        s = (self.a + self.b + self.c) / 2
        return s * (s - self.a) * (s - self.b) * (s - self.c)

    def volume(self):
        return self.square()  # Площа для трикутника


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()  # Площа для прямокутника


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a  # Перша основа
        self.b = b  # Друга основа
        self.c = c  # Перша бічна сторона
        self.d = d  # Друга бічна сторона

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return ((self.a + self.b) / 2)

    def volume(self):
        return self.square()  # Площа для трапеції


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()  # Площа для паралелограма


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * (self.radius ** 2)

    def volume(self):
        return self.square()  # Площа для кола


# 3D фігури

class Ball(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def dimention(self):
        return 3

    def square(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)  # Об'єм кулі


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3

    def volume(self):
        return (1 / 3) * self.square() * self.h  # Об'єм трикутної піраміди


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def volume(self):
        return (1 / 3) * self.square() * self.h  # Об'єм чотирикутної піраміди


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def square(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def volume(self):
        return self.a * self.b * self.c  # Об'єм прямокутного паралелепіпеда


class Cone(Circle):
    def __init__(self, radius, h):
        super().__init__(radius)
        self.h = h

    def dimention(self):
        return 3

    def square(self):
        return math.pi * self.radius * (self.radius + math.sqrt(self.h ** 2 + self.radius ** 2))

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.h  # Об'єм конуса


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return 3

    def volume(self):
        return super().square() * self.h  # Об'єм трикутної призми


# Функція для створення фігури на основі вхідних даних
def create_figure_from_data(data):
    parts = data.split()
    figure_type = parts[0]

    try:
        if figure_type == "Triangle":
            a, b, c = map(float, parts[1:])
            return Triangle(a, b, c)
        elif figure_type == "Rectangle":
            a, b = map(float, parts[1:])
            return Rectangle(a, b)
        elif figure_type == "Trapeze":
            if len(parts) != 5:
                raise ValueError(f"Трапеція повинна мати 4 параметрів: основи, бокові сторони та висота. Замість цього надано {len(parts)-1}.")
            a, b, c, d = map(float, parts[1:])
            return Trapeze(a, b, c, d)
        elif figure_type == "Parallelogram":
            a, b, h = map(float, parts[1:])
            return Parallelogram(a, b, h)
        elif figure_type == "Circle":
            radius = float(parts[1])
            return Circle(radius)
        elif figure_type == "Ball":
            radius = float(parts[1])
            return Ball(radius)
        elif figure_type == "TriangularPyramid":
            a, h = map(float, parts[1:])
            return TriangularPyramid(a, h)
        elif figure_type == "QuadrangularPyramid":
            a, b, h = map(float, parts[1:])
            return QuadrangularPyramid(a, b, h)
        elif figure_type == "RectangularParallelepiped":
            a, b, c = map(float, parts[1:])
            return RectangularParallelepiped(a, b, c)
        elif figure_type == "Cone":
            radius, h = map(float, parts[1:])
            return Cone(radius, h)
        elif figure_type == "TriangularPrism":
            a, b, c, h = map(float, parts[1:])
            return TriangularPrism(a, b, c, h)
        else:
            raise ValueError(f"Невідома фігура: {figure_type}")
    except ValueError as e:
        print(f"Помилка при створенні фігури: {e}")
        return None


# Читання фігур з файлу
def read_figures_from_file(file_name):
    figures = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                figures.append(create_figure_from_data(line))
    return figures

# Знаходимо найбільшу фігуру
def find_largest_figure(figures):
    largest = None
    largest_measure = -float('inf')

    for figure in figures:
        if figure is None:
            continue  # Пропускаємо некоректні фігури

        if hasattr(figure, "volume"):
            measure = figure.volume()
        elif hasattr(figure, "square"):
            measure = figure.square()
        else:
            continue  # Якщо немає ні площі, ні об'єму, пропускаємо

        if measure > largest_measure:
            largest_measure = measure
            largest = figure

    return largest

# Читання фігур з файлу
figures = read_figures_from_file('input01.txt')

# Знаходимо найбільшу фігуру
largest_figure = find_largest_figure(figures)

# Виводимо результат
print(f"The largest figure is {largest_figure.__class__.__name__} with measure: {largest_figure.volume()}")
