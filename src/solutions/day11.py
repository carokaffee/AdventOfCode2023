from src.tools.loader import load_data
import itertools


TESTING = False


def expand_universe(data):
    grid = []
    for line in data:
        grid.append(line)
        if line.find("#") < 0:
            grid.append(["." for _ in range(len(line))])

    new_grid = ["" for _ in range(len(grid))]
    for j in range(len(grid[0])):
        has_hash = False
        for i in range(len(grid)):
            if grid[i][j] == "#":
                has_hash = True
        for i in range(len(grid)):
            new_grid[i] += grid[i][j]
        if not has_hash:
            for i in range(len(grid)):
                new_grid[i] += "."
    return new_grid


def expand_universe_more(data):
    expanded_rows = []
    expanded_cols = []
    for i, line in enumerate(data):
        if line.find("#") < 0:
            expanded_rows.append(i)

    for j in range(len(data[0])):
        has_hash = False
        for i in range(len(data)):
            if data[i][j] == "#":
                has_hash = True
        if not has_hash:
            expanded_cols.append(j)
    return expanded_rows, expanded_cols


def get_coords(grid):
    coords = []
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "#":
                coords.append((i, j))
    return coords


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    print(data)
    print()
    new_grid = expand_universe(data)
    for line in new_grid:
        print(line)

    coords = get_coords(new_grid)
    print(coords)

    print(list(itertools.combinations([1, 2, 3, 4, 5], 2)))

    res = 0
    for pair_1, pair_2 in itertools.combinations(coords, 2):
        res += abs(pair_1[0] - pair_2[0]) + abs(pair_1[1] - pair_2[1])

    print(res)

    expanded_rows, expanded_cols = expand_universe_more(data)
    print(expanded_rows, expanded_cols)

    res_2 = 0

    coords = get_coords(data)

    for pair_1, pair_2 in itertools.combinations(coords, 2):
        if pair_1[0] > pair_2[0]:
            exp_length_row = len(
                list(
                    set(expanded_rows).intersection(
                        set(range(pair_2[0], pair_1[0] + 1))
                    )
                )
            )
        else:
            exp_length_row = len(
                list(
                    set(expanded_rows).intersection(
                        set(range(pair_1[0], pair_2[0] + 1))
                    )
                )
            )
        if pair_1[1] > pair_2[1]:
            exp_length_col = len(
                list(
                    set(expanded_cols).intersection(
                        set(range(pair_2[1], pair_1[1] + 1))
                    )
                )
            )
        else:
            exp_length_col = len(
                list(
                    set(expanded_cols).intersection(
                        set(range(pair_1[1], pair_2[1] + 1))
                    )
                )
            )
        res_2 += exp_length_row * (1000000 - 1)
        res_2 += exp_length_col * (1000000 - 1)
        res_2 += abs(pair_1[0] - pair_2[0]) + abs(pair_1[1] - pair_2[1])

    print(res_2)
