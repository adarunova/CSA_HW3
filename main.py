import sys
import time

from container import Container
from random_shape_generator import random_generate_shape
from build_container import build_container


# main.py - содержит главную функцию, обеспечивающую простое тестирование.

def error_message():
    print("Incorrect command line! You must write: python main -f <inputFileName> <outputFileName1> <outputFileName2>")
    print("Or")
    print("Incorrect command line! You must write: python main -n \"number\" <outputFileName1> <outputFileName2>")


if __name__ == '__main__':

    start_time = time.time()

    print("Start")

    if len(sys.argv) != 5:
        error_message()
        exit(1)

    # Контейнер.
    container = Container()

    if sys.argv[1] == '-f':
        input_file_name = sys.argv[2]
        output_file_name1 = sys.argv[3]
        output_file_name2 = sys.argv[4]

        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки.
        input_stream = open(input_file_name)
        input_string = input_stream.read()
        input_stream.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        str_array = input_string.replace("\n", " ").split(" ")
        shape_count = build_container(container, str_array)
        if shape_count > Container.MAX_LENGTH or shape_count <= 0:
            print("Incorrect number of figures = {}. Set 0 < number <= {}".format(shape_count, container.MAX_LENGTH))
            exit(2)

    elif sys.argv[1] == '-n':
        size = int(sys.argv[2])
        output_file_name1 = sys.argv[3]
        output_file_name2 = sys.argv[4]

        if size > Container.MAX_LENGTH or size <= 0:
            print("Incorrect number of figures = {}. Set 0 < number <= {}".format(size, container.MAX_LENGTH))
            exit(2)
        while size != 0:
            container.store.append(random_generate_shape())
            size -= 1
    else:
        error_message()
        exit(1)

    print("The container stores", len(container.store), "shapes:")
    container.print()

    output_stream1 = open(output_file_name1, 'w')
    output_stream1.write("The container stores {} shapes:\n".format(len(container.store)))
    container.write(output_stream1)
    output_stream1.close()

    container.delete_elements()

    print("\nThe container after deleting elements contains {} shapes:".format(len(container.store)))
    container.print()

    output_stream2 = open(output_file_name2, 'w')
    output_stream2.write("The container after deleting elements contains {} shapes:\n".format(len(container.store)))
    container.write(output_stream2)
    output_stream2.close()

    print("\n%s seconds" % (time.time() - start_time))

    print("Finish")
