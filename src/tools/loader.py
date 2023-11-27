from pathlib import Path
from sys import argv
from typing import List
from src.tools.download import download_data, get_filename


def get_day_number() -> int:
    script_path = Path(argv[0])
    day_no = script_path.stem[-2:]
    return int(day_no)


def load_data(use_test_input: bool, sep: str, strip: bool = True) -> List[str]:
    day_no = get_day_number()
    filename = get_filename(day_no, use_test_input)
    download_data(day_no)
    with open(filename) as f:
        if strip:
            return f.read().strip().split(sep)
        else:
            return f.read().split(sep)
