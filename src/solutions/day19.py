from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    workflows = dict()
    variables = []
    for line in data[0].split("\n"):
        name = line.split("{")[0]
        steps = line.split("{")[1][:-1].split(",")
        sorted_steps = []
        for step in steps:
            if ":" in step:
                cond, next = step.split(":")
            else:
                cond, next = "True", step
            sorted_steps.append((cond, next))
        workflows[name] = sorted_steps
    for line in data[1].split("\n"):
        variable = dict()
        for var in line[1:-1].split(","):
            name, val = var.split("=")
            variable[name] = int(val)
        variables.append(variable)
    return workflows, variables


def add_accepted_parts(workflows, variables):
    res = 0
    for variable in variables:
        x, m, a, s = variable["x"], variable["m"], variable["a"], variable["s"]
        current = "in"
        done = False
        while not done:
            next_workflow = workflows[current]
            found = False
            for next_step in next_workflow:
                if not found and eval(next_step[0]):
                    current = next_step[1]
                    found = True
            if current == "A":
                done = True
                res += x + m + a + s
            if current == "R":
                done = True
    return res


def number_of_possiblities(current, min_max_vals):
    if current == "R":
        return 0
    elif current == "A":
        return (
            (min_max_vals["x"][1] - min_max_vals["x"][0])
            * (min_max_vals["m"][1] - min_max_vals["m"][0])
            * (min_max_vals["a"][1] - min_max_vals["a"][0])
            * (min_max_vals["s"][1] - min_max_vals["s"][0])
        )

    possible_next_configs = []
    for condition, next_name in workflows[current]:
        if "<" in condition:
            var, num = condition.split("<")
            num = int(num)
            if min_max_vals[var][1] <= num:
                possible_next_configs.append(
                    (next_name, {key: val for key, val in min_max_vals.items()})
                )
            elif min_max_vals[var][0] < num:
                left_min_max_vals = {key: val for key, val in min_max_vals.items()}
                right_min_max_vals = {key: val for key, val in min_max_vals.items()}
                left_min_max_vals[var] = (min_max_vals[var][0], num)
                right_min_max_vals[var] = (num, min_max_vals[var][1])
                possible_next_configs.append((next_name, left_min_max_vals))
                min_max_vals = right_min_max_vals
            else:
                continue
        elif ">" in condition:
            var, num = condition.split(">")
            num = int(num)
            if min_max_vals[var][0] <= num:
                left_min_max_vals = {key: val for key, val in min_max_vals.items()}
                right_min_max_vals = {key: val for key, val in min_max_vals.items()}
                left_min_max_vals[var] = (min_max_vals[var][0], num + 1)
                right_min_max_vals[var] = (num + 1, min_max_vals[var][1])
                possible_next_configs.append((next_name, right_min_max_vals))
                min_max_vals = left_min_max_vals
            elif min_max_vals[var][0] > num:
                possible_next_configs.append(
                    (next_name, {key: val for key, val in min_max_vals.items()})
                )
            else:
                continue
        else:
            possible_next_configs.append(
                (next_name, {key: val for key, val in min_max_vals.items()})
            )
    sol = 0
    for current, min_max_vals in possible_next_configs:
        sol += number_of_possiblities(current, min_max_vals)
    return sol


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    workflows, variables = parse_input(data)

    # PART 1
    # test:    19114
    # answer: 325952
    print(add_accepted_parts(workflows, variables))

    # PART 2
    # test:   167409079868000
    # answer: 125744206494820
    min_max_vals = {key: (1, 4001) for key in ("x", "m", "a", "s")}
    print(number_of_possiblities("in", min_max_vals))
