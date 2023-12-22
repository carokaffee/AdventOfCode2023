from src.tools.loader import load_data

TESTING = True


def parse_input(data):
    broadcaster = None
    flipflops = dict()
    conjunctions = dict()
    for line in data:
        module, dest = line.split(" -> ")
        if module[0] == "%":
            flipflops[module[1:]] = [name.strip() for name in dest.split(",")]
        elif module[0] == "&":
            conjunctions[module[1:]] = [name.strip() for name in dest.split(",")]
        elif module == "broadcaster":
            broadcaster = [name.strip() for name in dest.split(",")]
        else:
            raise ValueError("what?")
    return broadcaster, flipflops, conjunctions


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    broadcaster, flipflops, conjunctions = parse_input(data)
    print(broadcaster)
    print(flipflops)
    print(conjunctions)
    flipflop_states = {name: 0 for name in flipflops.keys()}
    conjunction_states = {name: dict() for name in conjunctions.keys()}

    for conjunction in conjunctions.keys():
        if conjunction in broadcaster:
            conjunction_states[conjunction]["broadcaster"] = "low"
        for flipflop in flipflops.keys():
            if conjunction in flipflops[flipflop]:
                conjunction_states[conjunction][flipflop] = "low"
        for other_conj in conjunctions.keys():
            if conjunction in conjunctions[other_conj]:
                conjunction_states[conjunction][other_conj] = "low"

    low_signal_counter = 0
    high_signal_counter = 0
    button_press_counter = 0
    found = False

    print(flipflop_states)
    print(conjunction_states)

    while not found:
        signal_queue = [("button", "broadcaster", "low")]
        low_signal_counter += 1
        button_press_counter += 1
        while signal_queue:
            new_signal_queue = signal_queue[1:]
            source, next_name, signal_type = signal_queue[0]
            if next_name == "broadcaster":
                for dest in broadcaster:
                    if signal_type == "low":
                        low_signal_counter += 1
                    else:
                        high_signal_counter += 1
                    new_signal_queue.append((next_name, dest, signal_type))
            elif next_name in flipflops.keys():
                if signal_type == "low":
                    if flipflop_states[next_name] == 0:
                        for dest in flipflops[next_name]:
                            high_signal_counter += 1
                            new_signal_queue.append((next_name, dest, "high"))
                    elif flipflop_states[next_name] == 1:
                        for dest in flipflops[next_name]:
                            low_signal_counter += 1
                            new_signal_queue.append((next_name, dest, "low"))
                    else:
                        raise ValueError("whattt?")
                    flipflop_states[next_name] = 1 - flipflop_states[next_name]
            elif next_name in conjunctions.keys():
                conjunction_states[next_name][source] = signal_type
                all_high = True
                for src, sign_type in conjunction_states[next_name].items():
                    if sign_type == "low":
                        all_high = False
                if all_high:
                    for dest in conjunctions[next_name]:
                        low_signal_counter += 1
                        new_signal_queue.append((next_name, dest, "low"))
                else:
                    for dest in conjunctions[next_name]:
                        high_signal_counter += 1
                        new_signal_queue.append((next_name, dest, "high"))
            else:
                # print(next_name)
                if next_name == "rx":
                    if signal_type == "low":
                        print("button presses", button_press_counter)
                        found = True
            signal_queue = new_signal_queue

    print(low_signal_counter)
    print(high_signal_counter)
    print(low_signal_counter * high_signal_counter)
    print("button", button_press_counter)
