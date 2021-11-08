# container.py - содержит тип данных, представляющий простейший контейнер.

class Container:
    # Максимальная длина массива.
    MAX_LENGTH = 10000

    def __init__(self):
        # Массив фигур.
        self.store = []
        pass

    # Выводит фигуры в консоль.
    def print(self):
        for i in range(len(self.store)):
            print("{}. ".format(i), end='')
            self.store[i].print()
        pass

    # Вывод содержимого контейнера в указанный поток.
    def write(self, output_stream):
        for i in range(len(self.store)):
            output_stream.write("{}. ".format(i))
            self.store[i].write(output_stream)
            output_stream.write("\n")
        pass

    # Отчистка контейнера от фигур с периметром, меньшим среднего значаения.
    def delete_elements(self):
        perimeters = []
        average_perimeter = 0.0
        for shape in self.store:
            perimeter = shape.get_perimeter()
            perimeters.append(perimeter)
            average_perimeter += perimeter

        average_perimeter /= len(self.store)
        new_store = []
        for i in range(len(perimeters)):
            if perimeters[i] >= average_perimeter:
                new_store.append(self.store[i])
        self.store = new_store
        pass
