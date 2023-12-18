from src.tools.loader import load_data

TESTING = True

DIRECTIONS = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
MAPPING = {0: "R", 1: "D", 2: "L", 3: "U"}
MAPPING_2 = {"R": 0, "D": 1, "L": 2, "U": 3}


def parse_input(data):
    instructions = []
    instructions_2 = []
    for line in data:
        dir = line.split()[0]
        num = int(line.split()[1])
        instructions.append((dir, num))
        num_2 = int(line.split()[2][2:-2], 16)
        dir_2 = MAPPING[int(line.split()[2][-2])]
        instructions_2.append((dir_2, num_2))
    return instructions, instructions_2


def print_grid(outline, max_i, max_j, min_i, min_j):
    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            if (i, j) == (0, 0):
                print("S", end="")
            elif (i, j) in outline:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    instructions, instructions_2 = parse_input(data)

    current = (0, 0)
    outline = [(0, 0)]

    for dir, num in instructions:
        for i in range(num):
            current = (current[0] + DIRECTIONS[dir][0], current[1] + DIRECTIONS[dir][1])
            outline.append(current)

    max_i = -1
    max_j = -1
    min_i = 1
    min_j = 1

    for i, j in outline:
        max_i = max(max_i, i + 1)
        max_j = max(max_j, j + 1)
        min_i = min(min_i, i)
        min_j = min(min_j, j)

    grid = []

    for i in range(min_i, max_i):
        grid.append([])
        for j in range(min_j, max_j):
            if (i, j) == (0, 0):
                grid[-1].append("S")
            elif (i, j) in outline:
                grid[-1].append("#")
            else:
                grid[-1].append(".")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_i = i
                start_j = j

    active = {(start_i + 1, start_j + 1)}

    while active:
        new_active = set()
        for i, j in active:
            grid[i][j] = "#"
            for dir in DIRECTIONS:
                new = (i + DIRECTIONS[dir][0], j + DIRECTIONS[dir][1])
                if grid[new[0]][new[1]] == ".":
                    new_active.add((i + DIRECTIONS[dir][0], j + DIRECTIONS[dir][1]))
        active = new_active

    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                res += 1

    print(res)

    print(instructions_2)

    current = (0, 0)
    outline = [(0, 0)]

    for dir, num in instructions_2:
        current = (
            current[0] + DIRECTIONS[dir][0] * num,
            current[1] + DIRECTIONS[dir][1] * num,
        )
        outline.append(current)
