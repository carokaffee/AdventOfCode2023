from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    bricks = []
    for line in data:
        coord1, coord2 = line.split("~")
        coord1 = list(map(int, coord1.split(",")))
        coord2 = list(map(int, coord2.split(",")))
        bricks.append((coord1, coord2))
    return bricks


def get_full_bricks(bricks):
    full_bricks = []
    for start, end in bricks:
        full_bricks.append([])
        xs, ys, zs = start
        xe, ye, ze = end
        brick_range = max(xe - xs, ye - ys, ze - zs) + 1
        if xe != xs:
            for i in range(brick_range):
                full_bricks[-1].append((xs + i, ys, zs))
        elif ye != ys:
            for i in range(brick_range):
                full_bricks[-1].append((xs, ys + i, zs))
        elif ze != zs:
            for i in range(brick_range):
                full_bricks[-1].append((xs, ys, zs + i))
        else:
            full_bricks[-1].append((xs, ys, zs))
    return full_bricks


def let_them_fall(full_bricks):
    still_falling = True
    while still_falling:
        still_falling = False
        for i, cubes in enumerate(full_bricks):
            can_fall = True
            for j, other_cubes in enumerate(full_bricks):
                if i == j:
                    continue
                for xc, yc, zc in cubes:
                    for xo, yo, zo in other_cubes:
                        if (xo == xc and yc == yo and zo == zc - 1) or zc == 1:
                            can_fall = False
            if can_fall:
                still_falling = True
                for k, (x, y, z) in enumerate(full_bricks[i]):
                    full_bricks[i][k] = (x, y, z - 1)
    return full_bricks


def get_supports(full_bricks):
    supported_from = {brick: [] for brick in range(len(bricks))}
    supports = {brick: [] for brick in range(len(bricks))}
    for i, cube in enumerate(full_bricks):
        for j, other_cube in enumerate(full_bricks):
            if i == j:
                continue
            found = False
            for xc, yc, zc in cube:
                for xo, yo, zo in other_cube:
                    if not found and xo == xc and yc == yo and zo == zc + 1:
                        found = True
                        supported_from[j].append(i)
                        supports[i].append(j)
    for key in supported_from.keys():
        for _, _, z in full_bricks[key]:
            if z == 1:
                supported_from[key].append(-1)
    return supports, supported_from


def count_removable_bricks(supports, supported_from):
    counter = 0
    for support in supports.values():
        can_be_removed = True
        for j in support:
            if len(supported_from[j]) <= 1:
                can_be_removed = False
        if can_be_removed:
            counter += 1
    return counter


def count_chain_reactions(full_bricks, supported_from):
    res = 0
    for i in range(len(full_bricks)):
        new_supported_from = {key: val for key, val in supported_from.items()}
        removed = {i}
        done = False
        while not done:
            done = True
            for key, val in new_supported_from.items():
                if len(set(val).intersection(set(removed))) > 0:
                    done = False
                    new_supported_from[key] = [el for el in val if el not in removed]
            for key, val in new_supported_from.items():
                if val == [] and key not in removed:
                    removed.add(key)
        res += len(removed) - 1
    return res


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    bricks = parse_input(data)
    full_bricks = get_full_bricks(bricks)
    full_bricks = let_them_fall(full_bricks)
    supports, supported_from = get_supports(full_bricks)

    # PART 1
    # test:     5
    # answer: 375
    print(count_removable_bricks(supports, supported_from))

    # PART 2
    # test:       7
    # answer: 72352
    print(count_chain_reactions(full_bricks, supported_from))
