import random

from colors import Color
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle


# build_container.py - содержит функцию ввода данных.

# Ввод содержимого контейнера.
def build_container(container, str_array):
    array_length = len(str_array)
    # Если параметров меньше пяти, то фигур нет.
    if array_length < 5:
        return 0
    # Текущая позиция при чтении параметров фигур.
    position = 0
    shape_number = 0
    while position < array_length:
        # Получение ключа - номера фиуры.
        key = int(str_array[position])
        # Значение ключа для круга.
        if key == 1:
            shape = Circle()
        # Значение ключа для прямоугольника.
        elif key == 2:
            shape = Rectangle()
        # Значение ключа для треугольника.
        elif key == 3:
            shape = Triangle()
        else:
            # Некорректный ключ признака. Возврат количества прочитанных фигур
            return shape_number

        position += 1
        if position == array_length:
            return shape_number

        # Чтение цвета фигуры.
        color = int(str_array[position])
        if color > 6 or color < 0:
            print("Incorrect color! The COLOR will be randomly generated.")
            color = random.randint(0, 6)
        shape.color = Color(color)
        position += 1

        # Чтение параметров фигуры с возвратом позиции после неё.
        position = shape.read_shape_parameters(str_array, position)
        if position == 0:
            return shape_number
        shape_number += 1
        container.store.append(shape)
    return shape_number
