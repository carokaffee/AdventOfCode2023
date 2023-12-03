from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    numbers = []
    for i, line in enumerate(data):
        in_number = False
        for j, el in enumerate(line):
            if not in_number:
                if el.isdigit():
                    in_number = True
                    numbers.append([el, [(i, j)]])
            else:
                if el.isdigit():
                    numbers[-1][0] += el
                    numbers[-1][1].append((i, j))
                else:
                    in_number = False
                    numbers[-1][0] = int(numbers[-1][0])
    return numbers


def get_valid_coords(data):
    valid_coords = []
    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if not el.isdigit() and el != ".":
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        valid_coords.append((i + x, j + y))
    return valid_coords


def get_sum_of_valid_numbers(numbers, valid_coords):
    sum_of_valids = 0
    for number, coords in numbers:
        number_valid = False
        for coord in coords:
            if coord in valid_coords:
                number_valid = True
        if number_valid:
            sum_of_valids += int(number)
    return sum_of_valids


def get_gear_coords(data):
    gear_coords = dict()
    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if el == "*":
                gear_coords[(i, j)] = [0, []]
    return gear_coords


def get_sum_of_gear_ratios(numbers, gear_coords):
    for number, coords in numbers:
        used_gear_coords = []
        adjacent_cells = []
        for i, j in coords:
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if (i + x, j + y) not in coords:
                        adjacent_cells.append((i + x, j + y))
        for coord in adjacent_cells:
            if coord in gear_coords.keys() and coord not in used_gear_coords:
                used_gear_coords.append(coord)
                gear_coords[coord][0] += 1
                gear_coords[coord][1].append(number)

    sum_of_gear_ratios = 0
    for value in gear_coords.values():
        if len(value[1]) == 2:
            sum_of_gear_ratios += int(value[1][0]) * int(value[1][1])

    return sum_of_gear_ratios


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    numbers = parse_input(data)

    valid_coords = get_valid_coords(data)
    gear_coords = get_gear_coords(data)

    # PART 1
    # test:     4361
    # answer: 537832
    print(get_sum_of_valid_numbers(numbers, valid_coords))

    # PART 2
    # test:     467835
    # answer: 81939900
    print(get_sum_of_gear_ratios(numbers, gear_coords))
