def no_c(my_string):
    result = [char for char in my_string if char not in {'c', 'C'}]
    
    return ''.join(result)

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
    