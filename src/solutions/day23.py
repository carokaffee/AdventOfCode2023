from src.tools.loader import load_data

TESTING = False

DIRECTIONS = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}


def print_path(grid, path):
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if (i, j) in path:
                print("O", end="")
            else:
                print(el, end="")
        print()


if __name__ == "__main__":
    grid = load_data(TESTING, "\n")

    si, sj = 0, 0
    for i, el in enumerate(grid[0]):
        if el == ".":
            sj = i

    current = (si, sj)
    visited = []
    down = 0

    currents = [current]
    visiteds = [visited]
    dones = []

    nodes = {current: []}

    while currents:
        current = currents[0]
        new_currents = currents[1:]
        visited = visiteds[0]
        new_visiteds = visiteds[1:]
        if current[0] == len(grid) - 1 and current[1] == len(grid[0]) - 2:
            dones.append(len(set(visited)))
            assert len(visited) == len(set(visited))
            currents = new_currents
            visiteds = new_visiteds
            continue
        next_x, next_y = [], []
        visited.append(current)
        if grid[current[0]][current[1]] in "><v^":
            down += 1
        for (x, y), sym in DIRECTIONS.items():
            if (
                grid[current[0] + x][current[1] + y] in [".", sym]
                and (current[0] + x, current[1] + y) not in visited
            ):
                next_x.append(current[0] + x)
                next_y.append(current[1] + y)

        for j in range(len(next_x)):
            new_currents.append((next_x[j], next_y[j]))
            new_visiteds.append([i for i in visited])
        currents = new_currents
        visiteds = new_visiteds

    for i in range(len(visiteds)):
        print(len(visiteds[i]))

    print(dones)
    print(max(dones))
