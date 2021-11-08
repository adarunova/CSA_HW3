from math import pi
from shape import *


# circle.py - содержит функции обработки круга.

class Circle(Shape):
    def __init__(self):
        super().__init__()
        # Координаты центра.
        self.x = 0
        self.y = 0
        # Радиус.
        self.radius = 0

    # Ввод параметров круга из файла.
    def read_shape_parameters(self, str_array, position):
        # Должно быт как минимум три непрочитанных значения в массиве
        if position >= len(str_array) - 2:
            return 0
        self.x = int(str_array[position])
        self.y = int(str_array[position + 1])
        self.radius = int(str_array[position + 2])
        position += 3

        if self.radius <= 0:
            print("Incorrect CIRCLE. Radius cannot be zero or less. The CIRCLE will be randomly generated.")
            self.generate_parameters()

        return position

    # Генерация параметров круга.
    def generate_parameters(self):
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.radius = random.randint(0, 100)
        pass

    # Вывод параметров круга в консоль.
    def print(self):
        print(
            "CIRCLE. Center coordinates: Center coordinates: ({}, {}), radius: {} Perimeter = {}. Color: {}".format(
                self.x, self.y, self.radius, self.get_perimeter(), self.color.name))
        pass

    # Вывод параметров круга в файл.
    def write(self, output_stream):
        output_stream.write(
            "CIRCLE. Center coordinates:  ({}, {}), radius: {} Perimeter = {}. Color: {}".format(
                self.x, self.y, self.radius, self.get_perimeter(), self.color.name))
        pass

    # Вычисление периметра круга.
    def get_perimeter(self):
        return 2 * pi * self.radius
        pass
