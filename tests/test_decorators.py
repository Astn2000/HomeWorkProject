import os

import pytest

from src.decorators import log


def test_log_in_file() -> None:
    filename = "test_mylog.txt"

    @log(filename)
    def function(x: int, y: int) -> int:
        return x + y

    function(1, 2)

    directory = "log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    with open(filename, "r", encoding="utf-8") as f:
        assert f.readline() == "function ok\n"
    os.remove(filename)


def test_log_in_terminal(capsys: pytest.CaptureFixture) -> None:
    @log()
    def function(x: int, y: int) -> int:
        return x + y

    function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "function ok\n"
