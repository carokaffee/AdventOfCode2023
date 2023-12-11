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
        new_pyramid = [[0]]

        for i, line in enumerate(pyramid[::-1]):
            if i == 0:
                continue
            this_elem = pyramid[::-1][i][0]
            prev_elem = new_pyramid[i - 1][0]
            next_item = this_elem - prev_elem
            new_pyramid.append([next_item] + pyramid[::-1][i])

        res += new_pyramid[-1][0]

    print(res)
