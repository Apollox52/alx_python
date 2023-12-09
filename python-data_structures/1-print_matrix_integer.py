def print_matrix_integer(matrix=[]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list[list[int]]): The matrix to print.
    """
    if matrix is None or len(matrix) == 0:  # Check for empty or non-existent matrix
        print("--$")
        return

    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")

    print()