import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return -1
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        if p == -1:
            return -1
        under_sqrt = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(under_sqrt) if under_sqrt >= 0 else -1

class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimeter(self):
        return 2 * (self.a + self.b) if self.a > 0 and self.b > 0 else -1

    def area(self):
        return self.a * self.b if self.a > 0 and self.b > 0 else -1

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d if all(x > 0 for x in [self.a, self.b, self.c, self.d]) else -1

    def area(self):
        s = (self.a + self.b + self.c + self.d) / 2
        under_sqrt = (s - self.a) * (s - self.b) * (s - self.a - self.d) * (s - self.a - self.c)
        if under_sqrt < 0 or self.a == self.b:
            return -1
        h = (2 / (self.a - self.b)) * math.sqrt(under_sqrt)
        return (self.a + self.b) / 2 * h

class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def perimeter(self):
        return 2 * (self.a + self.b) if all(x > 0 for x in [self.a, self.b, self.h]) else -1

    def area(self):
        return self.a * self.h if all(x > 0 for x in [self.a, self.b, self.h]) else -1

class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r if self.r > 0 else -1

    def area(self):
        return math.pi * self.r**2 if self.r > 0 else -1

def parse_figure(line):
    parts = line.split()
    figure_type = parts[0]
    try:
        params = list(map(float, parts[1:]))
    except ValueError:
        return None

    if figure_type == "Triangle" and len(params) == 3:
        return Triangle(*params)
    elif figure_type == "Rectangle" and len(params) == 2:
        return Rectangle(*params)
    elif figure_type == "Trapeze" and len(params) == 4:
        return Trapeze(*params)
    elif figure_type == "Parallelogram" and len(params) == 3:
        return Parallelogram(*params)
    elif figure_type == "Circle" and len(params) == 1:
        return Circle(*params)
    else:
        return None

figures = []
try:
    with open('input01.txt', 'r', encoding="utf-8") as file:
        for line in file:
            figure = parse_figure(line)
            if figure:
                figures.append(figure)

    if not figures:
        raise ValueError("Файл не містить коректних фігур.")

    valid_figures = [f for f in figures if f.area() != -1 and f.perimeter() != -1]

    if not valid_figures:
        raise ValueError("Жодна з фігур не має коректних значень площі та периметра.")

    max_area_figure = max(valid_figures, key=lambda f: f.area())
    max_perimeter_figure = max(valid_figures, key=lambda f: f.perimeter())

    output_text = (
        f"Фігура з найбільшою площею: {type(max_area_figure).__name__} з площею {max_area_figure.area():.2f}\n"
        f"Фігура з найбільшим периметром: {type(max_perimeter_figure).__name__} з периметром {max_perimeter_figure.perimeter():.2f}\n"
    )

    print(output_text)

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

except FileNotFoundError:
    print("Файл input01.txt не знайдено.")
except ValueError as e:
    print(f"Помилка: {e}")
