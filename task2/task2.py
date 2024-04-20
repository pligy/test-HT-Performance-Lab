import sys


def read_circle_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        x, y = map(float, data[0].split())
        radius = float(data[1])

    return x, y, radius

def read_dots_file(file_path):
    with open(file_path, 'r') as file:
        dots = []
        for line in file:
            x, y = map(float, line.split())
            dots.append((x, y))

    return dots

def dot_position(x_c, y_c, radius, x_d, y_d):
    distance_squared = (x_d - x_c) ** 2 + (y_d - y_c) ** 2
    if distance_squared == radius ** 2:
        return 0
    elif distance_squared < radius ** 2:
        return 1
    else:
        return 2


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise IOError("write in the format - python" +
                  "\\path_to_file\\task2.py \\path_to_file\\circle.txt \\path_to_file\\dots.txt")

        circle_file = sys.argv[1]
        dots_file = sys.argv[2]

        x_c, y_c, radius = read_circle_file(circle_file)
        dots = read_dots_file(dots_file)

        for dot in dots:
            position = dot_position(x_c, y_c, radius, dot[0], dot[1])
            print(position)
    except IOError as ie:
        print("Error:", ie)