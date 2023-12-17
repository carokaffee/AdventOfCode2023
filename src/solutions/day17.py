from src.tools.loader import load_data
from tqdm import tqdm

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
            # print("small coord", coord, nodes[coord])
            next_coordinate = coord
            min_dist = nodes[coord]
    return next_coordinate


def set_neighbours(coordinates, unvisited):
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
            # print("got here 1", next_coord, nodes[next_coord])
            if (
                nodes[next_coord]
                > nodes[coordinates] + grid[next_coord[0]][next_coord[1]]
            ):
                # print("got here ########################")
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
        (i, j, dir, num): 2**100
        for i in range(grid_i_dim)
        for j in range(grid_j_dim)
        for dir in DIRECTIONS
        for num in [0, 1, 2, 3]
    }

    nodes[(0, 0, (1, 0), 0)] = 0
    nodes[(0, 0, (0, 1), 0)] = 0

    unvisited = set(nodes.keys())
    print(grid_i_dim, grid_j_dim, len(unvisited))

    visited = set()
    end_coordinates = [
        (grid_i_dim - 1, grid_j_dim - 1, dir, num)
        for dir in [(0, 1), (1, 0)]
        for num in [0, 1, 2, 3]
    ]
    counter = 0
    while set(end_coordinates) not in visited:
        counter += 1
        counter = counter % 10
        if counter == 0:
            print(len(visited), len(unvisited), grid_i_dim * grid_j_dim)

        # print("next")
        # for key, val in nodes.items():
        # if val < 2**100:
        # print("possibilities:", key, val)
        # print("unvisited", unvisited)
        current_coordinate = get_next_coordinate(unvisited)
        if current_coordinate is None:
            break
        # print("current coordinate", current_coordinate, nodes[current_coordinate])
        unvisited.remove(current_coordinate)
        visited.add(current_coordinate)
        set_neighbours(current_coordinate, unvisited)

    for end_coordinate in end_coordinates:
        print("done", end_coordinate, nodes[end_coordinate])

    # print(nodes)
