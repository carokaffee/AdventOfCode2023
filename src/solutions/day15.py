from src.tools.loader import load_data
from collections import OrderedDict

TESTING = False


def get_hash_val(string):
    current_value = 0
    for el in string:
        current_value += ord(el)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def sort_into_boxes(strings):
    boxes = [OrderedDict() for _ in range(256)]
    for string in strings:
        if "-" in string:
            label = string[:-1]
            hash_val = get_hash_val(label)
            if label in boxes[hash_val].keys():
                boxes[hash_val].pop(label)
        else:
            label, focal_length = string.split("=")
            hash_val = get_hash_val(label)
            boxes[hash_val][label] = int(focal_length)
    return boxes


def get_verification_number(boxes):
    num = 0
    for i, box in enumerate(boxes):
        for j, val in enumerate(box.values()):
            num += (i + 1) * (j + 1) * val
    return num


if __name__ == "__main__":
    strings = load_data(TESTING, ",")
    boxes = sort_into_boxes(strings)

    # PART 1
    # test:     1320
    # answer: 510013
    print(sum([get_hash_val(string) for string in strings]))

    # PART 2
    # test:      145
    # answer: 268497
    print(get_verification_number(boxes))
