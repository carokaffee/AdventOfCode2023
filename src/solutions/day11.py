from src.tools.loader import load_data
import itertools

TESTING = True


def expand_universe(data):
    exp_rows = [i for i in range(len(data)) if data[i].find("#") < 0]
    exp_cols = []
    for j in range(len(data[0])):
        has_hash = False
        for i in range(len(data)):
            if data[i][j] == "#":
                has_hash = True
        if not has_hash:
            exp_cols.append(j)
    return exp_rows, exp_cols


def get_coords(grid):
    coords = []
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "#":
                coords.append((i, j))
    return coords


def get_distance(pair_1, pair_2):
    x1, y1 = pair_1
    x2, y2 = pair_2
    start_x, end_x = min(x1, x2), max(x1, x2)
    start_y, end_y = min(y1, y2), max(y1, y2)
    x_dist = len(set(exp_rows).intersection(set(range(start_x, end_x))))
    y_dist = len(set(exp_cols).intersection(set(range(start_y, end_y))))
    return x_dist + y_dist


def get_result(coords, exp_factor):
    sum = 0
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        distance = get_distance((x1, y1), (x2, y2))
        sum += distance * (exp_factor - 1)
        sum += abs(x2 - x1) + abs(y2 - y1)
    return sum


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    exp_rows, exp_cols = expand_universe(data)
    coords = get_coords(data)

    # PART 1
    # test:       374
    # answer: 9805264
    print(get_result(coords, 2))

    # PART 2
    # test:      82000210
    # answer:779032247216
    print(get_result(coords, 1000000))
