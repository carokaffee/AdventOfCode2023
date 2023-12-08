from src.tools.loader import load_data

TESTING = True


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
    print(instruction)
    print(directions)

    counter = 0
    steps = 0
    not_found = True
    locations_with_A = [key for key in directions.keys() if key[-1] == "A"]
    location = locations_with_A[0]
    print("loc", locations_with_A)
    while not_found:
        index = counter % len(instruction)
        current_ins = instruction[index]
        if current_ins == "R":
            location = directions[location][1]
            steps += 1
        elif current_ins == "L":
            location = directions[location][0]
            steps += 1
        if location[-1] == "Z":
            not_found = False
        counter += 1

    print(steps)
