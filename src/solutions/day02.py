from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    games = []
    for line in data:
        id = int(line.split(":")[0].split(" ")[1])
        games_str = list(line.split(": ")[1].split(";"))
        takes = []
        for game in games_str:
            takes.append({"red": 0, "green": 0, "blue": 0})
            colors = game.split(",")
            for color in colors:
                num, color_str = color.strip().split(" ")
                num = int(num)
                takes[-1][color_str] = num
        games.append((id, takes))
    return games


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    games = parse_input(data)

    sum_ids = 0
    for id, game in games:
        possible = True
        for take in game:
            if take["red"] > 12 or take["blue"] > 14 or take["green"] > 13:
                possible = False

        if possible:
            sum_ids += id

    print(sum_ids)

    sum_powers = 0
    for id, game in games:
        min_required = [0, 0, 0]
        for take in game:
            if take["red"] > min_required[0]:
                min_required[0] = take["red"]
            if take["blue"] > min_required[1]:
                min_required[1] = take["blue"]
            if take["green"] > min_required[2]:
                min_required[2] = take["green"]
        power = min_required[0] * min_required[1] * min_required[2]
        sum_powers += power

    print(sum_powers)
