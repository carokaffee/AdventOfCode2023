from src.tools.loader import load_data

# import itertools
from collections import Counter

TESTING = False

CONVERSION = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
CATEGORIES = ("five", "four", "fullhouse", "three", "twopairs", "onepair", "high")


def parse_input(data):
    hands = []
    for line in data:
        cards = line.split()[0].strip()
        bid = int(line.split()[1].strip())
        cards = [int(i) if i.isdigit() else CONVERSION[i] for i in cards]
        hands.append((cards, bid))
    return hands


def sort_by_category(hands):
    categorised_hands = {category: [] for category in CATEGORIES}
    for hand in hands:
        cards, bid = hand
        counts = dict(Counter(cards))
        vals = list(counts.values())
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
        else:
            categorised_hands["high"].append(hand)
    return categorised_hands


def sort_by_highest_card(hands):
    return sorted(hands, key=lambda x: x[0])


def get_score(hands):
    res = 0
    for i, hand in enumerate(hands):
        cards, bid = hand
        res += (i + 1) * bid
    return res


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    hands = parse_input(data)
    categorised_hands = sort_by_category(hands)

    sorted_hands = []
    for category in CATEGORIES[::-1]:
        sorted_hands += sort_by_highest_card(categorised_hands[category])

    print(get_score(sorted_hands))
