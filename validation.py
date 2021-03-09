def is_in_matrix(mat, row, col):
    return 0 <= row < mat.shape[0] and 0 <= col < mat.shape[1]


def is_not_old(passed_coords, row, col):
    if (row, col) in passed_coords:
        return False
    return True


def is_valid(mat, row, col, passed_coords, color):
    if is_in_matrix(mat, row, col) and is_not_old(passed_coords, row, col) and mat[row, col] == color:
        return True
    return False
