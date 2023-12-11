from src.tools.loader import load_data

TESTING = False

NEIGHBOURS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    ".": [],
}

CONNECTORS = {
    "left": "-LF",
    "right": "-J7",
    "up": "|7F",
    "down": "|LJ",
}


def parse_input(data):
    return [[el for el in line] for line in data]


def fill_in_missing_pipe(grid, x, y):
    connected_pipes = []
    if grid[x - 1][y] in CONNECTORS["up"]:
        connected_pipes.append((-1, 0))
    if grid[x + 1][y] in CONNECTORS["down"]:
        connected_pipes.append((1, 0))
    if grid[x][y - 1] in CONNECTORS["left"]:
        connected_pipes.append((0, -1))
    if grid[x][y + 1] in CONNECTORS["right"]:
        connected_pipes.append((0, 1))
    for key, val in NEIGHBOURS.items():
        if len(set(connected_pipes).intersection(set(val))) == 2:
            grid[x][y] = key
    return grid


def replace_S(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                x, y = i, j

    grid = fill_in_missing_pipe(grid, x, y)

    return grid, (x, y)


def find_loop(grid, coords):
    not_found = True
    queue = [coords]
    loop = [coords]
    steps = 0
    while not_found:
        steps += 1
        new_queue = []
        for x, y in queue:
            for x_neigh, y_neigh in NEIGHBOURS[grid[x][y]]:
                if (x + x_neigh, y + y_neigh) not in new_queue:
                    if (x + x_neigh, y + y_neigh) not in loop:
                        new_queue.append((x + x_neigh, y + y_neigh))
                        loop.append((x + x_neigh, y + y_neigh))
                else:
                    not_found = False
        queue = new_queue
    return loop, steps


def expand_grid(grid, loop):
    new_grid = []
    for x in range(len(grid)):
        new_grid.append(["."])
        for y in range(len(grid[0])):
            if (x, y) in loop:
                new_grid[-1].append(grid[x][y])
            else:
                new_grid[-1].append(".")
            new_grid[-1].append("o")
        new_grid[-1].append(".")
        new_grid.append(["."] + ["o" for _ in range(2 * len(grid[0]))] + ["."])
    new_grid.append(["." for _ in range(2 * len(grid[0]) + 2)])

    for x in range(len(new_grid)):
        for y in range(len(new_grid[0])):
            if new_grid[x][y] == "o":
                new_grid = fill_in_missing_pipe(new_grid, x, y)
    return new_grid


def count_inner_tiles(grid, loop):
    new_grid = expand_grid(grid, loop)
    queue = [(1, 1)]
    while queue:
        new_queue = []
        for i, j in queue:
            if new_grid[i][j] in ".o":
                for x in [-1, 1]:
                    for y in [-1, 1]:
                        if new_grid[i + x][j] in ".o":
                            new_queue.append((i + x, j))
                        if new_grid[i][j + y] in ".o":
                            new_queue.append((i, j + y))
                new_grid[i][j] = "x"
        queue = new_queue

    num_inner_tiles = 0
    for line in new_grid:
        num_inner_tiles += line.count(".")

    return num_inner_tiles


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)
    grid, coords = replace_S(grid)
    loop, farthest_point = find_loop(grid, coords)
    num_inner_tiles = count_inner_tiles(grid, loop)

    # PART 1
    # test:     80
    # answer: 6738
    print(farthest_point)

    # PART 2
    # test:    10
    # answer: 579
    print(num_inner_tiles)
