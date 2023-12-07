from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    hands = []

    for line in data:
        card_string = line.split()[0]
        bid = int(line.split()[1].strip())
        cards = {i: 0 for i in range(2, 15)}
        card_list = []
        for digit in card_string:
            if digit.isdigit():
                cards[int(digit)] += 1
                card_list.append(int(digit))
            elif digit == "T":
                cards[10] += 1
                card_list.append(10)
            elif digit == "J":
                cards[11] += 1
                card_list.append(11)
            elif digit == "Q":
                cards[12] += 1
                card_list.append(12)
            elif digit == "K":
                cards[13] += 1
                card_list.append(13)
            elif digit == "A":
                cards[14] += 1
                card_list.append(14)
            else:
                raise ValueError("invalid input string")
        hands.append((cards, bid, tuple(card_list)))
    return hands


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    hands = parse_input(data)

    categorised_hands = {
        "five": [],
        "four": [],
        "fullhouse": [],
        "three": [],
        "twopairs": [],
        "onepair": [],
        "high": [],
    }

    for hand in hands:
        cards, bid, card_tuple = hand
        vals = list(cards.values())
        if 5 in vals:
            categorised_hands["five"].append(hand)
        elif 4 in vals:
            categorised_hands["four"].append(hand)
        elif 3 in vals and 2 in vals:
            categorised_hands["fullhouse"].append(hand)
        elif 3 in vals:
            categorised_hands["three"].append(hand)
        elif vals.count(2) == 2:
            categorised_hands["twopairs"].append(hand)
        elif 2 in vals:
            categorised_hands["onepair"].append(hand)
        else:  # len(vals) == 5:
            categorised_hands["high"].append(hand)
        # else:
        #    print("WTF?", hand)

    sorted_cat_cards = {key: None for key in categorised_hands.keys()}

    for category, cat_hands in categorised_hands.items():
        cards_in_cat = []
        for hand, bid, card_tuple in cat_hands:
            cards_in_cat.append((card_tuple, bid))
        cards_in_cat = sorted(cards_in_cat, key=lambda x: x[0])

        sorted_cat_cards[category] = cards_in_cat

    res = 0
    counter = 1
    sorted_cat_cards_tuple = []
    for key in reversed(
        ["five", "four", "fullhouse", "three", "twopairs", "onepair", "high"]
    ):
        if sorted_cat_cards[key] != []:
            sorted_cat_cards_tuple += sorted_cat_cards[key]
    print(sorted_cat_cards_tuple)

    for item in sorted_cat_cards_tuple:
        hand, bid = item
        res += counter * bid
        counter += 1

    print(res)
