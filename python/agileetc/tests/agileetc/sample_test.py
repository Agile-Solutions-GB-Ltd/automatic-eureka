import pytest

from src.agileetc.sample import read


def test_read_input_file() -> None:
    with pytest.raises(SystemExit):
        read("foo")
