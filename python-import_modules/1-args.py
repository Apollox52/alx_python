import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} {'argument' if argc == 1 else 'arguments'}:")
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")



