from src.tools.loader import load_data

TESTING = False


def get_hash_val(string):
    current_value = 0
    for el in string:
        current_value += ord(el)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def sort_into_boxes(strings):
    boxes = [dict() for _ in range(256)]
    for string in strings:
        focal_length = None
        if "-" in string:
            label = string[:-1]
        else:
            label, focal_length = string.split("=")
            focal_length = int(focal_length)
        hash_val = get_hash_val(label)
        if focal_length is not None:
            if label not in boxes[hash_val].keys():
                boxes[hash_val][label] = [focal_length, len(boxes[hash_val].items())]
            else:
                boxes[hash_val][label][0] = focal_length
        else:
            if label in boxes[hash_val].keys():
                orig_pos = boxes[hash_val][label][1]
                boxes[hash_val].pop(label)
                for key, val in boxes[hash_val].items():
                    if val[1] > orig_pos:
                        boxes[hash_val][key][1] = boxes[hash_val][key][1] - 1
    return boxes


def get_verification_number(boxes):
    num = 0
    for i, box in enumerate(boxes):
        for val in box.values():
            num += (i + 1) * (val[1] + 1) * val[0]
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
