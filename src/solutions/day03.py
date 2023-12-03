from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    numbers = []
    for i, line in enumerate(data):
        in_number = False
        for j, el in enumerate(line):
            if not in_number:
                if el in "0123456789":
                    in_number = True
                    numbers.append([el, [(i, j)]])
            elif in_number:
                if el in "0123456789":
                    numbers[-1][0] += el
                    numbers[-1][1].append((i, j))
                else:
                    in_number = False
    return numbers


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    print(data)

    numbers = parse_input(data)
    print(numbers)

    valid_coords = []

    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if el not in "0123456789.":
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        valid_coords.append((i + x, j + y))
    print(valid_coords)

    sum_of_valids = 0

    for number, coords in numbers:
        number_valid = False
        for coord in coords:
            if coord in valid_coords:
                number_valid = True
        if number_valid:
            sum_of_valids += int(number)

    print(sum_of_valids)
