from src.tools.loader import load_data

TESTING = False

DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def parse_input(data):
    return [list(map(int, line)) for line in data]


def print_grid(grid):
    for line in grid:
        for el in line:
            print(el, end="")
        print()


def get_next_coordinate(unvisited):
    next_coordinate = None
    min_dist = 2**100
    for coord in unvisited:
        if nodes[coord] < min_dist:
            next_coordinate = coord
            min_dist = nodes[coord]
    return next_coordinate


def set_neighbours(coordinates, unvisited):
    for dir in DIRECTIONS:
        if (dir == coordinates[2]) or (dir == (-coordinates[2][0], -coordinates[2][1])):
            continue
        for step in [4, 5, 6, 7, 8, 9, 10]:
            next_coord = (
                coordinates[0] + dir[0] * step,
                coordinates[1] + dir[1] * step,
                dir,
            )
            if next_coord in unvisited:
                cost = nodes[coordinates] + sum(
                    [
                        grid[coordinates[0] + dir[0] * i][coordinates[1] + dir[1] * i]
                        for i in range(1, step + 1)
                    ]
                )
                if nodes[next_coord] > cost:
                    nodes[next_coord] = cost


def set_neighbours2(coordinates, unvisited):
    for dir in DIRECTIONS:
        if coordinates[2] == dir:
            if coordinates[3] == 3:
                continue
            else:
                next_coord = (
                    coordinates[0] + dir[0],
                    coordinates[1] + dir[1],
                    dir,
                    coordinates[3] + 1,
                )
        else:
            next_coord = (coordinates[0] + dir[0], coordinates[1] + dir[1], dir, 1)
        if next_coord in unvisited:
            if (
                nodes[next_coord]
                > nodes[coordinates] + grid[next_coord[0]][next_coord[1]]
            ):
                nodes[next_coord] = (
                    nodes[coordinates] + grid[next_coord[0]][next_coord[1]]
                )


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)
    print_grid(grid)

    grid_i_dim = len(grid)
    grid_j_dim = len(grid[0])

    nodes = {
        (i, j, dir): 2**100
        for i in range(grid_i_dim)
        for j in range(grid_j_dim)
        for dir in DIRECTIONS
    }

    nodes[(0, 0, (1, 0))] = 0
    nodes[(0, 0, (0, 1))] = 0

    unvisited = set(nodes.keys())
    print(grid_i_dim, grid_j_dim, len(unvisited))

    visited = set()
    end_coordinates = [
        (grid_i_dim - 1, grid_j_dim - 1, dir) for dir in [(0, 1), (1, 0)]
    ]
    while len(set(end_coordinates).intersection(visited)) < 1:
        current_coordinate = get_next_coordinate(unvisited)
        unvisited.remove(current_coordinate)
        visited.add(current_coordinate)
        set_neighbours(current_coordinate, unvisited)

    for end_coordinate in end_coordinates:
        print("done", end_coordinate, nodes[end_coordinate])
