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
    """
    instruction, directions = parse_input(data)

    counter = 0
    steps = 0
    locations_with_A = [key for key in directions.keys() if key[-1] == "A"]
    print("locs with A", locations_with_A)
    start_locations = [i for i in locations_with_A]
    visited_locations = [[] for loc in locations_with_A]
    valid_locations = [[] for loc in locations_with_A]
    periods_of_locations = [None for _ in range(len(locations_with_A))]

    visits_new = []
    period_lengths = []
    start_tail = []
    valid_indices = [[] for _ in locations_with_A]

    for j, my_loc in enumerate(start_locations):
        print(my_loc)
        visited = []
        counter_2 = 0
        found_visited = False

        while not found_visited:
            index = counter_2 % len(instruction)
            current_ins = instruction[index]
            next_loc = directions[my_loc][0 if current_ins == "L" else 1]
            if (my_loc, index) not in visited:
                visited.append((my_loc, index))
            else:
                found_visited = True
                print((my_loc, index), counter_2)
                print("visited", visited)
                print(
                    "Location index",
                    visited.index((my_loc, index)),
                )
                period_lengths.append(len(visited) - visited.index((my_loc, index)))
                start_tail.append(visited.index((my_loc, index)))
                # valid_indices.append(
                #    [
                #        (start_tail[-1] - 1) + i * period_lengths[-1]
                #        for i in range(1, 10**10)
                #    ]
                # )

            if current_ins == "R":
                my_loc = directions[my_loc][1]
            elif current_ins == "L":
                my_loc = directions[my_loc][0]
            counter_2 += 1

        print(len(visited) - 1)
        visits_new.append(len(visited) - 1)
        # print(visited)False
        for visit in visited:
            if visit[0][-1] == "Z":
                print("VISITED!", visit)

    print("period_lengths", period_lengths)
    print("start_tail", start_tail)
    print("SOLUTION:", math.lcm(*visits_new))

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
                    # print("visited for ", i, ":", visited_locations[i])
            if (
                periods_of_locations[i] is None
                and (location, current_ins) not in visited_locations[i]
            ):
                visited_locations[i].append((location, current_ins))
                valid_locations[i].append(location[-1] == "Z")

        steps += 1
        locations_with_A = new_locations
        counter += 1

    # print(steps)
    # print(periods_of_locations)
    # print(visited_locations)
    for loc in valid_locations:
        for elem in loc:
            if elem == True:
                print("########juhu")

    # print(math.lcm(*periods_of_locations))

    # wrong 152381520 [54, 79, 48, 47, 60, 76]
    # wrong 102256020 [54, 79, 51, 47, 60, 81]

    print(len(instruction))
    """

    instruction, directions = parse_input(data)
    print(instruction, directions)

    locations_with_A = [key for key in directions.keys() if key[-1] == "A"]
    steps_to_first_Z = []

    for location in locations_with_A:
        counter = 0
        steps = 0
        found = False
        while not found:
            steps += 1
            next_location = (
                directions[location][0]
                if instruction[counter] == "L"
                else directions[location][1]
            )
            if next_location[-1] == "Z":
                found = True
                steps_to_first_Z.append(steps)
            location = next_location
            counter = (counter + 1) % len(instruction)

    print(steps_to_first_Z)
    print(math.lcm(*steps_to_first_Z))
