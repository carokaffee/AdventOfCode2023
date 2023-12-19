from src.tools.loader import load_data

TESTING = True


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


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    workflows, variables = parse_input(data)
    print(workflows, variables)

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

    print(res)
