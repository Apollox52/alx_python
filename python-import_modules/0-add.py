from add_0 import add as add_function

def main():
    a = 1
    b = 2

    c = add_function(a, b)
    print("{} + {} = {}".format(a, b, c))

if __name__ == "__main__":
    main()