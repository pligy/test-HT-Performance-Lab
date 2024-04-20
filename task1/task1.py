import sys


def get_path(n, m):
    path = []
    current_value = 1

    while current_value != 1 or len(path) == 0:
        path.append(current_value)

        current_value = (current_value + m - 1) % n
        if (current_value == 0):
            current_value = n

    return path


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("write in the format - python \\path_to_file\\task1.py n m")

        n = int(sys.argv[1])
        m = int(sys.argv[2])

        if n <= 0 or m <= 0:
            raise ValueError("n and m must be positive integers")

        print(*get_path(n, m), sep="")
    except ValueError as ve:
        print("Error:", ve)


