def print_matrix_integer(matrix=[[]]):
  """
  Prints a matrix of integers.

  Args:
    matrix: A list of lists of integers.
  """
  for row in matrix:
    for element in row:
      # Use str.format() to print integers without casting
      print("{:d}".format(element), end=" ")
    print("")
