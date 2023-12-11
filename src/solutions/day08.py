from src.tools.loader import load_data
import math

TESTING = False


def parse_input(data):
    instruction = data[0].strip()
    directions = dict()
    for line in data[1].split("\n"):
        start = line.split("=")[0].strip()
        end = tuple(line.split("=")[1].strip()[1:-1].split(", "))
        directions[start] = end
    return instruction, directions


def steps_to_ZZZ(instruction, directions):
    steps = 0
    found = False
    location = "AAA"
    while not found:
        location = directions[location][
            0 if instruction[steps % len(instruction)] == "L" else 1
        ]
        steps += 1
        if location == "ZZZ":
            found = True
    return steps


def steps_to_synchronised_Z(instruction, directions):
    locations_with_A = [key for key in directions.keys() if key[-1] == "A"]
    steps_to_Z = []

    for location in locations_with_A:
        steps = 0
        found = False
        while not found:
            location = directions[location][
                0 if instruction[steps % len(instruction)] == "L" else 1
            ]
            steps += 1
            if location[-1] == "Z":
                found = True
                steps_to_Z.append(steps)
    return math.lcm(*steps_to_Z)


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    instruction, directions = parse_input(data)

    # PART 1
    # test:   -----
    # answer: 22411
    print(steps_to_ZZZ(instruction, directions))

    # PART 2
    # test:                6
    # answer: 11188774513823
    print(steps_to_synchronised_Z(instruction, directions))
