from requests import get
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


def get_sessionname() -> str:
    with open(ROOT / "session_name.txt") as f:
        return f.read()


def get_filename(day_no: int, use_test_input: bool) -> Path:
    data_path = ROOT / "data"
    if use_test_input:
        return data_path / f"input{day_no:02d}_test.txt"
    else:
        return data_path / f"input{day_no:02d}.txt"


def download_data(day_no: int):
    filename = get_filename(day_no, use_test_input=False)
    if filename.exists():
        return
    with open(filename, "w") as f:
        cookie_dict = {"session": get_sessionname()}
        request = get(
            f"https://adventofcode.com/2023/day/{day_no}/input", cookies=cookie_dict
        )
        f.write(request.text)
