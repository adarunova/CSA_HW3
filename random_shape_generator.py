# Генерация случайной фигуры.
import random

from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from colors import Color


# random_generate_shape.py - содержит функцию генерации случайной фигуры.

# Генерирует случайную фигуру.
def random_generate_shape():
    key = random.randint(1, 3)
    # Значение ключа для круга.
    if key == 1:
        shape = Circle()
    # Значение ключа для прямоугольника.
    elif key == 2:
        shape = Rectangle()
    # Значение ключа для треугольника.
    else:
        shape = Triangle()

    shape.color = Color(random.randint(0, 6))
    shape.generate_parameters()
    return shape
