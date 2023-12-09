def print_matrix_integer(matrix=[]):
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")
    if not matrix or not matrix[0]:
        print("--$")