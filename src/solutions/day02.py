from src.tools.loader import load_data
import math

TESTING = False

COLOURS = ("red", "green", "blue")


def parse_input(data):
    games = []
    for line in data:
        id = int(line.split(":")[0].split(" ")[1])
        reveal_strings = list(line.split(": ")[1].split(";"))
        reveals = []
        for reveal in reveal_strings:
            reveals.append({colour: 0 for colour in COLOURS})
            cubes = reveal.split(",")
            for cube in cubes:
                num, colour = cube.strip().split(" ")
                reveals[-1][colour] = int(num)
        games.append((id, reveals))
    return games


def is_possible(game):
    possible = True
    for reveal in game:
        if reveal["red"] > 12 or reveal["green"] > 13 or reveal["blue"] > 14:
            possible = False
    return possible


def sum_of_possible_game_ids(games):
    sum_ids = 0
    for id, game in games:
        if is_possible(game):
            sum_ids += id
    return sum_ids


def sum_of_powers(games):
    sum_powers = 0
    for _, game in games:
        min_required = {colour: 0 for colour in COLOURS}
        for reveal in game:
            for colour in COLOURS:
                min_required[colour] = max(min_required[colour], reveal[colour])

        sum_powers += math.prod([min_required[colour] for colour in COLOURS])
    return sum_powers


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    games = parse_input(data)

    # PART 1
    # test:      8
    # answer: 2512
    print(sum_of_possible_game_ids(games))

    # PART 2
    # test:    2286
    # answer: 67335
    print(sum_of_powers(games))
