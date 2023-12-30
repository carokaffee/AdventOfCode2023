from src.tools.loader import load_data

TESTING = False


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
        else:
            broadcaster = [name.strip() for name in dest.split(",")]
    return broadcaster, flipflops, conjunctions


def initialise_values():
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

    input_conj_for_rx = None
    for conjunction, dests in conjunctions.items():
        if "rx" in dests:
            input_conj_for_rx = conjunction
    relevant_conjunctions = []

    if input_conj_for_rx is None:
        return flipflop_states, conjunction_states, []

    for conjunction in conjunction_states[input_conj_for_rx].keys():
        relevant_conjunctions.append(conjunction)
    return flipflop_states, conjunction_states, relevant_conjunctions


def run_system(conjunction_states, flipflop_states, aim, bound):
    low_signal_counter = 0
    high_signal_counter = 0
    button_press_counter = 0
    button_presses = [0, 0]
    counter = 0
    while counter < bound:
        counter += 1
        signal_queue = [("button", "broadcaster", "low")]
        low_signal_counter += 1
        button_press_counter += 1
        while signal_queue:
            new_signal_queue = signal_queue[1:]
            source, next_name, signal_type = signal_queue[0]
            if next_name == aim:
                if signal_type == "low":
                    button_presses.append(button_press_counter)
            elif next_name == "broadcaster":
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
                    else:
                        for dest in flipflops[next_name]:
                            low_signal_counter += 1
                            new_signal_queue.append((next_name, dest, "low"))
                    flipflop_states[next_name] = 1 - flipflop_states[next_name]
            elif next_name in conjunctions.keys():
                conjunction_states[next_name][source] = signal_type
                all_high = True
                for _, sign_type in conjunction_states[next_name].items():
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
                pass
            signal_queue = new_signal_queue
    return (
        low_signal_counter * high_signal_counter,
        button_presses[-1] - button_presses[-2],
    )


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    broadcaster, flipflops, conjunctions = parse_input(data)
    flipflop_states, conjunction_states, relevant_conjunctions = initialise_values()

    # PART 1
    # test:    11687500
    # answer: 949764474
    print(run_system(conjunction_states, flipflop_states, None, 1000)[0])

    # PART 2
    # test:   ---------------
    # answer: 243221023462303
    res = 1
    for conjunction in relevant_conjunctions:
        res *= run_system(conjunction_states, flipflop_states, conjunction, 10000)[1]
    print(res)
