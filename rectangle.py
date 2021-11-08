from shape import *


# rectangle.py - содержит описание прямоугольника.

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        # Координаты левой верхней вершины.
        self.x1 = 0
        self.y1 = 0
        # Координаты правой нижней вершины.
        self.x2 = 0
        self.y2 = 0

    # Ввод параметров прямоугольника из файла.
    def read_shape_parameters(self, str_array, position):
        # Должно быт как минимум четыре непрочитанных значения в массиве
        if position >= len(str_array) - 3:
            return 0
        self.x1 = int(str_array[position])
        self.y1 = int(str_array[position + 1])
        self.x2 = int(str_array[position + 2])
        self.y2 = int(str_array[position + 3])
        position += 4

        if (self.x2 - self.x1) * (self.y1 - self.y2) == 0:
            print("Incorrect RECTANGLE. All coordinates are on one line. The RECTANGLE will be randomly generated.")
            self.generate_parameters()
        elif (self.x2 <= self.x1) or (self.y1 <= self.y2):
            print("Incorrect RECTANGLE. Wrong corner coordinates! The RECTANGLE will be randomly generated.")
            self.generate_parameters()

        return position

    # Генерация параметров треугольника.
    def generate_parameters(self):
        import random
        self.x1 = random.randint(-100, 100)
        self.y1 = random.randint(-100, 100)
        self.x2 = random.randint(self.x1, self.x1 + 100)
        self.y2 = random.randint(self.y1, self.y1 + 100)
        pass

    # Вывод параметров прямоугольника в консоль.
    def print(self):
        print("RECTANGLE. Coordinates of angles:  ({}, {}), ({}, {}). Perimeter = {}. Color: {}".format(
            self.x1, self.y1, self.x2, self.y2, self.get_perimeter(), self.color.name))
        pass

    # Вывод параметров прямоугольника в файл.
    def write(self, output_stream):
        output_stream.write(
            "RECTANGLE. Coordinates of angles:  ({}, {}), ({}, {}). Perimeter = {}. Color: {}".format(
                self.x1, self.y1, self.x2, self.y2, self.get_perimeter(), self.color.name))
        pass

    # Вычисление периметра прямоугольника.
    def get_perimeter(self):
        return 2.0 * (abs(self.x1 - self.x2) + abs(self.y1 - self.y2))
        pass
