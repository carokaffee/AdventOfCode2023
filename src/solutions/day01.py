from src.tools.loader import load_data

TESTING = False

CONVERSION_TABLE = {
    "one": "o1ne",
    "two": "tw2o",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "eig8ht",
    "nine": "ni9ne",
    "zero": "ze0ro",
}


def convert_words_to_numbers(str):
    for key in CONVERSION_TABLE.keys():
        str = str.replace(key, CONVERSION_TABLE[key])
    return str


def find_calibration_value(str, calibration):
    numbers = ""
    if calibration:
        str = convert_words_to_numbers(str)
    for el in str:
        if el.isdigit():
            numbers += el
    return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    # PART 1
    # test:   -----
    # answer: 55130
    print(sum(list(map(lambda x: find_calibration_value(x, False), data))))

    # PART 2
    # test:     281
    # answer: 54985
    print(sum(list(map(lambda x: find_calibration_value(x, True), data))))
