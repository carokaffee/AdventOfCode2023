from src.tools.loader import load_data

TESTING = True


def parse_input(data):
    seeds = list(map(int, data[0].split(": ")[1].split()))
    conversions = []
    for block in data[1:]:
        conversions.append(dict())
        for line in block.split("\n")[1:]:
            dest, source, length = list(map(int, line.split()))
            conversions[-1][(source, source + length)] = (dest, dest + length)
    return seeds, conversions


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    seeds, conversions = parse_input(data)

    transformed = []
    for seed in seeds:
        current_seed = seed
        for conversion in conversions:
            found = False
            for source_begin, source_end in conversion.keys():
                if (
                    current_seed >= source_begin
                    and current_seed <= source_end
                    and found == False
                ):
                    found = True
                    current_seed = (
                        conversion[(source_begin, source_end)][0]
                        + current_seed
                        - source_begin
                    )
        transformed.append(current_seed)

    print(transformed)
    print(min(transformed))
