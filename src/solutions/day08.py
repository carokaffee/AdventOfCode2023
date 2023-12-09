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


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    instruction, directions = parse_input(data)

    counter = 0
    steps = 0
    locations_with_A = [key for key in directions.keys() if key[-1] == "A"]
    print("locs with A", locations_with_A)
    start_locations = [i for i in locations_with_A]
    visited_locations = [[] for loc in locations_with_A]
    valid_locations = [[] for loc in locations_with_A]
    periods_of_locations = [None for _ in range(len(locations_with_A))]

    while None in periods_of_locations:
        index = counter % len(instruction)
        current_ins = instruction[index]
        new_locations = []
        for i, location in enumerate(locations_with_A):
            if current_ins == "R":
                location = directions[location][1]
            elif current_ins == "L":
                location = directions[location][0]

            new_locations.append(location)

            if (location, current_ins) in visited_locations[i]:
                if periods_of_locations[i] is None:
                    periods_of_locations[i] = len(visited_locations[i])
                    print("visited for ", i, ":", visited_locations[i])
            if (
                periods_of_locations[i] is None
                and (location, current_ins) not in visited_locations[i]
            ):
                if location[-1] == "Z":
                    print("$$$$$ JUHU")
                visited_locations[i].append((location, current_ins))
                valid_locations[i].append(location[-1] == "Z")

        steps += 1
        locations_with_A = new_locations
        counter += 1

    print(steps)
    print(periods_of_locations)
    print(visited_locations)
    for loc in valid_locations:
        for elem in loc:
            if elem == True:
                print("########juhu")

    print(math.lcm(*periods_of_locations))

    # wrong 152381520 [54, 79, 48, 47, 60, 76]
    # wrong 102256020 [54, 79, 51, 47, 60, 81]
