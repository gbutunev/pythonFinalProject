from validation import is_valid


def find_longest_path(mat):
    path = 0  # longest path placeholder
    total_count = mat.shape[0] * mat.shape[1]

    for color in ["R", "G", "B"]:
        for row in range(0, mat.shape[0]):
            for col in range(0, mat.shape[1]):
                current_path = 0
                if mat[row, col] == color:
                    current_path += 1
                    current_row = row
                    current_col = col
                    passed_coords = {(row, col)}

                    while True:
                        # right
                        if is_valid(mat, current_row, current_col + 1, passed_coords, color):
                            current_col += 1
                        # down
                        elif is_valid(mat, current_row + 1, current_col, passed_coords, color):
                            current_row += 1
                        # left
                        elif is_valid(mat, current_row, current_col - 1, passed_coords, color):
                            current_col -= 1
                        # up
                        elif is_valid(mat, current_row - 1, current_col, passed_coords, color):
                            current_row -= 1
                        else:
                            break
                        passed_coords.add((current_row, current_col))
                        current_path += 1

                    if current_path > path:
                        path = current_path
                    if path == total_count:
                        return path
    return path
