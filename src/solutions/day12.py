from src.tools.loader import load_data
from tqdm import tqdm

TESTING = False


def parse_input(data):
    springs = [line.split()[0] for line in data]
    conditions = [list(map(int, line.split()[1].split(","))) for line in data]
    return springs, conditions


def unfold_paper(springs, conditions):
    longer_springs = [(springs[i] + "?") * 4 + springs[i] for i in range(len(springs))]
    longer_conditions = [conditions[i] * 5 for i in range(len(springs))]
    return longer_springs, longer_conditions


def find_all_combinations(spring, condition):
    # if spring is too short for all conditions, there is no possible configuration
    if sum(condition) + len(condition) - 1 > len(spring):
        return 0

    # if no conditions are left, there is either one configuration or we are missing conditions
    if condition == []:
        if spring.count("#") > 0:
            return 0
        else:
            return 1

    # pick middle condition and divide problem in smaller parts
    current_condition = condition[len(condition) // 2]
    prev_condition = condition[: len(condition) // 2]
    next_condition = condition[len(condition) // 2 + 1 :]
    res = 0
    prev_spring, next_spring = None, None

    # find all placements for current condition and solve smaller problems to the left and right
    for i in range(len(spring)):
        if i + current_condition - 1 < len(spring):
            fit = True
            # condition cannot be placed on a dot
            for j in range(i, i + current_condition):
                if spring[j] == ".":
                    fit = False
            if fit:
                if i + current_condition == len(spring):
                    next_spring = ""
                else:
                    # after condition is placed, next item cannot be #
                    if spring[i + current_condition] == "#":
                        continue
                    next_spring = spring[i + current_condition :]
                    next_spring = "." + next_spring[1:]
                if i == 0:
                    prev_spring = ""
                else:
                    # after condition is placed, previous item cannot be #
                    if spring[i - 1] == "#":
                        continue
                    prev_spring = spring[:i]
                    prev_spring = prev_spring[: i - 1] + "."
            # position does not fit with condition
            else:
                continue
        # condition is too long for spring and position
        else:
            continue

        if prev_spring is None:
            return 0

        # solve smaller problems recursively and multiply independent left and right number of possibilities
        res += find_all_combinations(
            prev_spring, prev_condition
        ) * find_all_combinations(next_spring, next_condition)
    return res


def get_result(springs, conditions):
    res = 0
    # takes about an hour to compute part 2 but oh well... it works
    for i in tqdm(range(len(springs))):
        res += find_all_combinations(springs[i], conditions[i])
    return res


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    springs, conditions = parse_input(data)

    # PART 1
    # test:     21
    # answer: 7716
    print(get_result(springs, conditions))

    # PART 2
    # test:           525152
    # answer: 18716325559999
    print(get_result(*unfold_paper(springs, conditions)))
