from sys import argv

def print_arguments():
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments.\n.")
    else:
        print(f"{num_args} argument{'s' if num_args != 1 else ''}:")

        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}\n" if i < num_args else f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()



