from numpy import matrix


def read_matrix_from_console():
    rows, cols = [int(num) for num in input().split(" ")]
    m = [[x for x in input().split(" ")[:cols]] for _ in range(rows)]
    return matrix(m)


def read_matrix_from_file(test_case):
    file_path = "tests/" + test_case
    with open(file_path, 'r') as file:
        rows, cols = [int(num) for num in file.readline().split(' ')]
        m = [[x.rstrip() for x in line.split(" ")[:cols]] for line in file]
        file.close()
        return matrix(m)
