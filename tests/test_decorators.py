import os
from typing import Optional

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


def test_log_exception(capsys: pytest.CaptureFixture) -> None:
    @log()
    def function(x: Optional[int]) -> int:
        if not x:
            raise TypeError("Отсутствие данных")

        return x

    with pytest.raises(Exception):
        function(None)
    captured = capsys.readouterr()
    assert captured.out == "function error: TypeError: Отсутствие данных. Inputs: (None,), {}\n"
