import time
from datetime import datetime
from functools import wraps
from typing import Any
from typing import List


def log(fn):
    @wraps(fn)
    def logger(*args, **kwargs):
        args_values_types: List[Any] = [(a, type(a)) for a in args]
        kwargs_values_types: List[Any] = [(k, v, type(v)) for k, v in kwargs.items()]
        arguments = args_values_types + kwargs_values_types
        time_ = datetime.utcnow()
        time_str = time_.strftime("%H:%M:%S")
        try:
            fn_result = fn(*args, **kwargs)
            print(
                f"Function {fn.__name__} was called at {time_str} "
                f"with params {arguments} and returned {fn_result}"
            )
            return fn_result
        except Exception as e:
            print(
                f"Function {fn.__name__} was called at {time_str} "
                f"with params {arguments} and raised an exception {e}"
            )
            return

    return logger


@log
def divide_integers(a: int, b: int) -> float:
    result = a / b
    return result


def main():
    for _ in range(10):
        time.sleep(1.5)
        print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
