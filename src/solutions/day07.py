from src.tools.loader import load_data

import itertools
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
        cards, _ = hand
        cropped_cards = cards[:5]
        counts = dict(Counter(cropped_cards))
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


def sort_hands(hands):
    hands = sort_by_category(hands)
    sorted_hands = []
    for category in CATEGORIES[::-1]:
        sorted_hands += sort_by_highest_card(hands[category])
    return sorted_hands


def sort_joker_hands(hands):
    category_hands = sort_by_joker_category(hands)
    sorted_hands = []
    for category in CATEGORIES[::-1]:
        sorted_hands += sort_by_highest_joker_card(category_hands[category])
    return sorted_hands


def sort_by_highest_joker_card(hands):
    return sorted(hands, key=lambda x: x[1][0])


def sort_by_joker_category(hands):
    categorised_hands = {category: [] for category in CATEGORIES}
    for hand in hands:
        normal_hand, joker_hand = hand
        cards, _ = normal_hand
        assert 11 not in cards
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


def get_score(hands):
    res = 0
    for i, hand in enumerate(hands):
        _, bid = hand
        res += (i + 1) * bid
    return res


def find_max_val_for_J(hand):
    cards, bid = hand
    num_J = cards.count(11)
    if num_J == 0:
        return (cards, bid), (cards, bid)
    else:
        possible_J = list(
            itertools.product([i for i in range(2, 15) if i != 11], repeat=num_J)
        )
        all_possible_hands = []
        for J_tuple in possible_J:
            counter = 0
            new_hand = []
            new_hand_joker = []
            for item in cards:
                if item == 11:
                    new_hand.append(J_tuple[counter])
                    new_hand_joker.append(1)
                    counter += 1
                else:
                    new_hand.append(item)
                    new_hand_joker.append(item)
            new_hand = (list(new_hand), bid)
            new_hand_joker = (list(new_hand_joker), bid)
            all_possible_hands.append((new_hand, new_hand_joker))
        all_possible_hands = sort_joker_hands(all_possible_hands)
        return all_possible_hands[-1]


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    hands = parse_input(data)
    sorted_hands = sort_hands(hands)

    # PART 1
    # test:        6440
    # answer: 249638405
    print(get_score(sorted_hands))

    new_best_hands = []
    for hand in hands:
        new_best_hands.append(find_max_val_for_J(hand))

    new_best_hands = sort_joker_hands(new_best_hands)
    score = get_score([new_best_hand[0] for new_best_hand in new_best_hands])

    # PART 2
    # test:        5905
    # answer: 249776650
    print(score)

# TODO: Joker-funktionen entfernen und stattdessen beim sorten joker ersetzen
