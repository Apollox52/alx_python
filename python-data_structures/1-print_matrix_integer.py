def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
           
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num))
    
    print()

if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2], [4, 5]]
    matrix3 = [[1, 2], [4, 5], [7, 8]]
    matrix4 = [[1]]
    matrix5 = [[1], [2], [3], [4]]

    print("Correct output - case: matrix =", matrix1)
    print_matrix_integer(matrix1)

    print("Correct output - case: matrix =", matrix2)
    print_matrix_integer(matrix2)

    print("Correct output - case: matrix =", matrix3)
    print_matrix_integer(matrix3)

    print("Correct output - case: matrix =", matrix4)
    print_matrix_integer(matrix4)

    print("Correct output - case: matrix =", matrix5)
    print_matrix_integer(matrix5)