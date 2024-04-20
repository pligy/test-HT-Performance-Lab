import sys


def get_nums(file):
    nums = []
    with open(file, 'r') as file:
        for line in file:
            nums.append(int(line.strip()))

    return nums

def get_min_moves(nums):
    avg_num = sum(nums) // len(nums)
    moves = [abs(num - avg_num) for num in nums]
    return sum(moves)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise IOError("write in the format - python" + \
                "\\path_to_file\\task4.py \\path_to_file\\numbers.txt")

        file = sys.argv[1]
        nums = get_nums(file)

        print(get_min_moves(nums))
    except IOError as ie:
        print("Error:", ie)