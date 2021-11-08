import random


# shape.py - содержит процедуры связанные с обработкой обобщенной фигуры и создания произвольной фигуры.
from colors import Color


class Shape:

    def __init__(self):
        self.color = Color.NONE

    # Ввод обобщенной фигуры.
    def read_shape_parameters(self, str_array, position):
        pass

    # Генерация параметров фигуры фигуры.
    def generate_parameters(self):
        pass

    # Вывод обобщенной фигуры в консоль.
    def print(self):
        pass

    # Вывод обобщенной фигуры в файл.
    def write(self, output_stream):
        pass

    # Вычисление периметра обобщенной фигуры.
    def get_perimeter(self):
        pass
