def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num), end="")
        print()
  
    print()

if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2], [4, 5]]
    matrix3 = [[1, 2], [4, 5], [7, 8]]
    matrix4 = [[1]]
    matrix5 = [[1], [2], [3], [4]]

    print_matrix_integer(matrix1)
    print("--")
    print_matrix_integer(matrix2)
    print("--")
    print_matrix_integer(matrix3)
    print("--")
    print_matrix_integer(matrix4)
    print("--")
    print_matrix_integer(matrix5)
