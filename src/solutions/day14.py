from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    grid = []
    for line in data:
        grid.append([])
        for el in line:
            grid[-1].append(el)
    return grid


def tilt_up(grid):
    new_grid = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "#":
                new_grid[i][j] = "#"
            elif el == "O":
                counter = 0
                found_end = False
                end = -1
                for n in range(i - 1, -1, -1):
                    if grid[n][j] == "#":
                        found_end = True
                        if end == -1:
                            end = n
                    if not found_end:
                        if grid[n][j] == "O":
                            counter += 1
                        else:
                            assert grid[n][j] == "."
                if end != -1:
                    new_grid[end + counter + 1][j] = "O"
                else:
                    new_grid[counter][j] = "O"
    return new_grid


def turn_grid(grid):
    new_grid = []
    for j in range(len(grid[0])):
        new_grid.append([])
        for i in range(len(grid)):
            new_grid[-1].append(grid[len(grid) - i - 1][j])
    return new_grid


def full_cycle(grid):
    for _ in range(4):
        grid = tilt_up(grid)
        grid = turn_grid(grid)
    return grid


def get_score(grid):
    res = 0
    for i, line in enumerate(grid):
        res += line.count("O") * (len(line) - i)
    return res


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)
    new_grid = tilt_up(grid)

    # PART 1
    # test:      136
    # answer: 110779
    print(get_score(new_grid))

    # PART 2
    # test:      64
    # answer: 86069
    # I just found the cycle manually which was after 77 steps and did some maths
    for i in range(1000):
        grid = full_cycle(grid)
        print(i, get_score(grid))
