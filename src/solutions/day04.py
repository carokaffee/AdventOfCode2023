from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    cards = []
    for line in data:
        win_nums, my_nums = line.split(":")[1].split("|")
        win_nums = list(map(int, win_nums.split()))
        my_nums = list(map(int, my_nums.split()))
        cards.append((win_nums, my_nums))
    return cards


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    cards = parse_input(data)

    points = 0
    num_scratchcards = {i: 1 for i in range(len(data))}

    for card_id, (win_nums, my_nums) in enumerate(cards):
        counter = len(set(win_nums).intersection(set(my_nums)))
        points += 2 ** (counter - 1) if counter else 0
        for i in range(1, counter + 1):
            num_scratchcards[card_id + i] += num_scratchcards[card_id]

    sum_scratchcards = sum(num_scratchcards.values())

    # PART 1
    # test:      13
    # answer: 23847
    print(points)

    # PART 2
    # test:        30
    # answer: 8570000
    print(sum_scratchcards)
