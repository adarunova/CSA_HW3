from math import sqrt
from shape import *


# triangle.py - содержит функции обработки треугольника.

class Triangle(Shape):

    def __init__(self):
        super().__init__()
        # Координаты вершин.
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0

    # Ввод параметров треугольника из файла.
    def read_shape_parameters(self, str_array, position):
        # Должно быть как минимум четыре непрочитанных значения в массиве
        if position >= len(str_array) - 3:
            return 0
        self.x1 = int(str_array[position])
        self.y1 = int(str_array[position + 1])
        self.x2 = int(str_array[position + 2])
        self.y2 = int(str_array[position + 3])
        self.x3 = int(str_array[position + 4])
        self.y3 = int(str_array[position + 5])
        position += 6

        # Проверка на то, что координаты находятся на одной линии.
        if (self.x3 - self.x2) * (self.y2 - self.y1) == (self.y3 - self.y2) * (self.x2 - self.x1):
            print("Incorrect TRIANGLE. All coordinates are on one line. The TRIANGLE will be randomly generated.")
            self.generate_parameters()

        return position

    # Генерация параметров треугольника.
    def generate_parameters(self):
        self.x1 = random.randint(-100, 100)
        self.y1 = random.randint(-100, 100)
        self.x2 = random.randint(-100, 100)
        self.x3 = random.randint(-100, 100)

        # Генерируем y2 так, чтобы точки (x1, y1) и(x2, y2) не совпадали.
        while self.x1 == self.x2 and self.y1 == self.y2:
            self.y2 = random.randint(-100, 100)

        # Генерируем y3 так, чтобы точки (x1, y1), (x2, y2) и (x3, y3) не лежали на одной прямой.
        while (self.x3 - self.x2) * (self.y2 - self.y1) == (self.y3 - self.y2) * (self.x2 - self.x1):
            self.y2 = random.randint(-100, 100)
        pass

    # Вывод параметров треугольника в консоль.
    def print(self):
        print("TRIANGLE. Coordinates of vertices: ({}, {}), ({}, {}), ({}, {}). Perimeter = {}. Color: {}".format(
            self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.get_perimeter(), self.color.name))
        pass

    # Вывод параметров треугольника в файл.
    def write(self, output_stream):
        output_stream.write(
            "TRIANGLE. Coordinates of vertices: ({}, {}), ({}, {}), ({}, {}). Perimeter = {}. Color: {}".format(
                self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.get_perimeter(), self.color.name))
        pass

    # Вычисление периметра треугольника.
    def get_perimeter(self):
        return sqrt(pow(self.x1 - self.x2, 2) + pow(self.y1 - self.y2, 2)) + \
               sqrt(pow(self.x2 - self.x3, 2) + pow(self.y2 - self.y3, 2)) + \
               sqrt(pow(self.x1 - self.x3, 2) + pow(self.y1 - self.y3, 2))
        pass
