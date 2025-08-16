import os
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional

BASEDIR = Path(__file__).resolve().parent.parent


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                return result
            except Exception as error_message:
                message = (
                    f"{func.__name__} error: {error_message.__class__.__name__}:"
                    f" {error_message}. Inputs: {args}, {kwargs}"
                )
                raise error_message
            finally:
                if filename:
                    os.chdir(BASEDIR)
                    directory = "log"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    with open(os.path.join(directory, filename), "a", encoding="utf-8") as f:
                        f.write(f"{message}\n")
                else:
                    print(f"{message}")

        return wrapper

    return decorator


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def function(x: int, y: int) -> int:
        """Функция сложения чисел и логирования результата"""
        return x + y

    print(function(1, 2))

    @log()
    def function_1(x: int, y: int) -> int:
        """Функция сложения чисел и логирования результата"""
        return x + y

    print(function_1(1, 2))

    # print(help(function))
