from sys import argv

def main():
    num_args = len(argv) - 1
    args_text = "argument" if num_args == 1 else "arguments"

    print(f"{num_args} {args_text}:")

    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")

    print("." if num_args == 0 else "")

if __name__ == "__main__":
    main()