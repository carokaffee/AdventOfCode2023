from src.tools.loader import load_data

TESTING = False

DIRECTIONS = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
MAPPING = {0: "R", 1: "D", 2: "L", 3: "U"}
MAPPING_2 = {val: key for key, val in MAPPING.items()}


def parse_input(data):
    instructions = []
    instructions_2 = []
    for line in data:
        dir = line.split()[0]
        num = int(line.split()[1])
        instructions.append((dir, num))
        dir_2 = MAPPING[int(line.split()[2][-2])]
        num_2 = int(line.split()[2][2:-2], 16)
        instructions_2.append((dir_2, num_2))
    return instructions, instructions_2


def get_corners(instructions):
    current = (0, 0)
    corners = []
    for i in range(len(instructions)):
        dir, num = instructions[i]
        prev_dir = instructions[i - 1][0]
        convex = (MAPPING_2[prev_dir] % 4) == ((MAPPING_2[dir] - 1) % 4)
        current = (
            current[0] + DIRECTIONS[dir][0] * num,
            current[1] + DIRECTIONS[dir][1] * num,
        )
        corners.append((*current, convex))
    return corners


def apply_shoelace(instructions, corners):
    res = 0
    for i in range(len(corners)):
        x, y, _ = corners[i - 1]
        x2, y2, convex = corners[i]
        res += 0.5 * (y + y2) * (x2 - x)
        if convex:
            res += 0.75
        else:
            res += 0.25
        res += 0.5 * (instructions[i][1] - 1)
    return int(res)


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    instructions, instructions_2 = parse_input(data)
    corners = get_corners(instructions)
    corners_2 = get_corners(instructions_2)

    # PART 1
    # test:      62
    # answer: 47139
    print(apply_shoelace(instructions, corners))

    # PART 2
    # test:      952408144115
    # answer: 173152345887206
    print(apply_shoelace(instructions_2, corners_2))
