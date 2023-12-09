from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    numbers = []
    for line in data:
        numbers.append(list(map(int, line.split())))
    return numbers


def get_differences(line):
    differences = []
    for i in range(len(line) - 1):
        differences.append(line[i + 1] - line[i])
    return differences


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    numbers = parse_input(data)
    print(numbers)

    res = 0
    for line in numbers:
        pyramid = [line]
        next_line = line
        done = False
        while not done:
            next_line = get_differences(next_line)
            pyramid.append(next_line)
            if next_line.count(0) == len(next_line):
                done = True
            print(next_line)

        print(pyramid)

        for i, line in enumerate(pyramid[::-1]):
            if i == 0:
                continue
            print("reverse", line)
            this_elem = pyramid[::-1][i][-1]
            prev_elem = pyramid[::-1][i - 1][-1]
            next_item = this_elem + prev_elem
            pyramid[::-1][i].append(next_item)

        res += pyramid[0][-1]

    print(res)
