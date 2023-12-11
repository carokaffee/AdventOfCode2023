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


def apply_maps(seeds, conversions):
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
    return transformed


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


def apply_maps_to_more_seeds(seeds, conversions):
    seed_ranges = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    for _ in seed_ranges:
        current_ranges = [i for i in seed_ranges]
        for conversion in conversions:
            new_ranges = []
            for source, dest in conversion.items():
                new_unmapped_ranges = []
                for current_range in current_ranges:
                    remaining_ranges, mapped_range = convert_intervals(
                        *current_range, *source, dest[0]
                    )
                    if mapped_range is not None:
                        new_ranges.append(mapped_range)
                    new_unmapped_ranges += remaining_ranges
                current_ranges = new_unmapped_ranges
            current_ranges += new_ranges
    return current_ranges


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    seeds, conversions = parse_input(data)

    # PART 1
    # test:          35
    # answer: 309796150
    print(min(apply_maps(seeds, conversions)))

    # PART 1
    # test:         46
    # answer: 50716416
    ranges = apply_maps_to_more_seeds(seeds, conversions)
    print(min([range[0] for range in ranges]))
