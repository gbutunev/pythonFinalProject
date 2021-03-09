import sys

from algorithm import find_longest_path
from readers import read_matrix_from_console, read_matrix_from_file

if __name__ == '__main__':

    test_num = len(sys.argv)
    if test_num == 1:
        print("Enter matrix info:")
        current_matrix = read_matrix_from_console()
        print(find_longest_path(current_matrix))
    else:
        print("Executing predefined tests:")
        for i in range(1, test_num):
            print(sys.argv[i])
            current_matrix = read_matrix_from_file(sys.argv[i])
            print(find_longest_path(current_matrix))
