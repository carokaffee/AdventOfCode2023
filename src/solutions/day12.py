from src.tools.loader import load_data
import itertools

TESTING = True


def parse_input(data):
    springs = []
    conditions = []
    for line in data:
        springs.append(line.split()[0])
        conditions.append(list(map(int, line.split()[1].split(","))))
    return springs, conditions


def unfold_paper(springs, conditions):
    longer_springs = []
    longer_conditions = []
    for i in range(len(springs)):
        longer_springs.append((springs[i] + "?") * 4 + springs[i])
        longer_conditions.append(conditions[i] * 5)
    return longer_springs, longer_conditions


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    springs, conditions = parse_input(data)
    springs, conditions = unfold_paper(springs, conditions)

    res = 0
    for i in range(len(springs)):
        print(i)
        num_springs = len(springs[i])
        num_broken = sum(conditions[i])
        num_conditions = len(conditions[i])
        possible_springs = []
        for empty_spaces in itertools.combinations(
            list(
                range(num_springs - num_broken + num_conditions - (num_conditions - 1))
            ),
            num_conditions,
        ):
            current_spring = "." * empty_spaces[0]
            for j in range(1, len(empty_spaces)):
                current_spring += "#" * conditions[i][j - 1]
                current_spring += "." * (empty_spaces[j] - empty_spaces[j - 1])
            current_spring += "#" * conditions[i][-1]
            current_spring += "." * (num_springs - len(current_spring))
            valid = True
            for x in range(num_springs):
                if (springs[i][x] == "#" and current_spring[x] == ".") or (
                    springs[i][x] == "." and current_spring[x] == "#"
                ):
                    valid = False
            if valid:
                possible_springs.append(current_spring)
        res += len(possible_springs)

    print(res)
