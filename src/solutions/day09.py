from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    numbers = []
    for line in data:
        numbers.append(list(map(int, line.split())))
    return numbers


def get_differences(row):
    differences = []
    for i in range(len(row) - 1):
        differences.append(row[i + 1] - row[i])
    return differences


def extrapolate_pyramid(rows, backwards=False):
    sum = 0
    for row in rows:
        if backwards:
            row = list(reversed(row))
        pyramid = [row]
        done = False
        while not done:
            row = get_differences(row)
            pyramid.append(row)
            if row.count(0) == len(row):
                done = True

        for i in range(1, len(pyramid)):
            new_number = (
                list(reversed(pyramid))[i][-1] + list(reversed(pyramid))[i - 1][-1]
            )
            pyramid[len(pyramid) - i - 1].append(new_number)

        sum += pyramid[0][-1]
    return sum


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    rows = parse_input(data)

    # PART 1
    # test:          114
    # answer: 1972648895
    print(extrapolate_pyramid(rows))

    # PART 2
    # test:     2
    # answer: 919
    print(extrapolate_pyramid(rows, backwards=True))
