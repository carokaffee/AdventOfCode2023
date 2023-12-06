from src.tools.loader import load_data

TESTING = False


def parse_races(data):
    times = list(map(int, data[0].split()[1:]))
    distances = list(map(int, data[1].split()[1:]))
    return tuple(zip(times, distances))


def parse_single_race(data):
    time = int("".join(data[0].split()[1:]))
    distance = int("".join(data[1].split()[1:]))
    return (time, distance)


def get_num_of_record_beaten(time, record):
    counter = 0
    for second in range(time):
        if (time - second) * second > record:
            counter += 1
    return counter


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    races = parse_races(data)
    single_race = parse_single_race(data)
    result = 1

    for time, record in races:
        result *= get_num_of_record_beaten(time, record)

    # PART 1
    # test:      288
    # answer: 114400
    print(result)

    # PART 1
    # test:      71503
    # answer: 21039729
    print(get_num_of_record_beaten(*single_race))
