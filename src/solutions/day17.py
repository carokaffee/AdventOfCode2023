from src.tools.loader import load_data

TESTING = False

DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def parse_input(data):
    return [list(map(int, line)) for line in data]


def initialise_graph(grid):
    i_dim = len(grid)
    j_dim = len(grid[0])
    nodes = {
        (i, j, dir): 2**100
        for i in range(i_dim)
        for j in range(j_dim)
        for dir in DIRECTIONS
    }
    nodes[(0, 0, (1, 0))] = 0
    nodes[(0, 0, (0, 1))] = 0
    end_coords = [(i_dim - 1, j_dim - 1, dir) for dir in [(0, 1), (1, 0)]]
    return nodes, end_coords


def set_neighbours(grid, nodes, coords, queue, visited, step_sizes):
    for dir in DIRECTIONS:
        if (dir == coords[2]) or (dir == (-coords[2][0], -coords[2][1])):
            continue
        for step in step_sizes:
            next_coord = (
                coords[0] + dir[0] * step,
                coords[1] + dir[1] * step,
                dir,
            )
            if next_coord in nodes and next_coord not in visited:
                queue.add(next_coord)
                cost = nodes[coords] + sum(
                    [
                        grid[coords[0] + dir[0] * i][coords[1] + dir[1] * i]
                        for i in range(1, step + 1)
                    ]
                )
                if nodes[next_coord] > cost:
                    nodes[next_coord] = cost
    return queue


def do_dijkstra(nodes, end_coords, step_sizes):
    queue = set([(0, 0, (1, 0)), (0, 0, (0, 1))])
    visited = set()
    while len(set(end_coords).intersection(visited)) < 1:
        current_coordinate = min(queue, key=lambda x: nodes[x])
        queue.remove(current_coordinate)
        visited.add(current_coordinate)
        queue = set_neighbours(
            grid, nodes, current_coordinate, queue, visited, step_sizes
        )
    return min([nodes[end_coord] for end_coord in end_coords])


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)

    # PART 1
    # test:   102
    # answer: 953
    nodes, end_coords = initialise_graph(grid)
    print(do_dijkstra(nodes, end_coords, range(1, 4)))

    # PART 2
    # test:     94
    # answer: 1180
    nodes, end_coords = initialise_graph(grid)
    print(do_dijkstra(nodes, end_coords, range(4, 11)))
