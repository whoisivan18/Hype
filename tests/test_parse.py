import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from bot import parse_schedule_args  # noqa: E402


def test_parse_ok():
    minutes, message = parse_schedule_args(["10", "hello", "world"])
    assert minutes == 10
    assert message == "hello world"


def test_parse_error():
    try:
        parse_schedule_args(["a"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
