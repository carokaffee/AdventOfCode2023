from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    seeds = list(map(int, data[0].split(": ")[1].split()))
    conversions = []
    for block in data[1:]:
        conversions.append(dict())
        for line in block.split("\n")[1:]:
            dest, source, length = list(map(int, line.split()))
            conversions[-1][(source, source + length)] = (dest, dest + length)
    return seeds, conversions


def convert_intervals(seed_start, seed_end, conv_start, conv_end, dest_start):
    if seed_end <= conv_start or conv_end <= seed_start:
        return [(seed_start, seed_end)], None
    elif seed_start >= conv_start and seed_end <= conv_end:
        return [], (
            dest_start + seed_start - conv_start,
            dest_start + seed_end - conv_start,
        )
    elif seed_start >= conv_start:
        return [(conv_end, seed_end)], (
            dest_start + seed_start - conv_start,
            dest_start + conv_end - conv_start,
        )
    elif seed_end <= conv_end:
        return [(seed_start, conv_start)], (
            dest_start,
            dest_start + seed_end - conv_start,
        )
    else:
        return [(seed_start, conv_start), (conv_end, seed_end)], (
            dest_start,
            dest_start + conv_end - conv_start,
        )


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    seeds, conversions = parse_input(data)
    print(conversions)

    seed_ranges = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    print(seed_ranges)

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

    transformed_ranges = []
    for seed_range in seed_ranges:
        seed_begin, seed_end = seed_range
        current_ranges = [i for i in seed_ranges]
        for conversion in conversions:
            new_ranges = []
            for source_range, dest_range in conversion.items():
                new_unmapped_ranges = []
                for current_range in current_ranges:
                    remaining_ranges, mapped_range = convert_intervals(
                        *current_range, *source_range, dest_range[0]
                    )
                    if mapped_range is not None:
                        new_ranges.append(mapped_range)
                    new_unmapped_ranges += remaining_ranges
                current_ranges = new_unmapped_ranges
            current_ranges += new_ranges

    print(transformed)
    print(min(transformed))

    print(min([current_range[0] for current_range in current_ranges]))
