from pathlib import Path
from functools import wraps
from time import perf_counter as timer


datadir = "dev/advent-of-code/src"


class InvalidEvent:
    pass


class ProblemNotFound:
    pass


def profiler(func):
    @wraps(func)
    def wrapper_profiler(*args, **kwargs):
        tic = timer()
        value = func(*args, **kwargs)
        toc = timer()
        elapsed = toc - tic
        print(f"{func.__name__!r} took {elapsed:.6f} s")
        return value
    return wrapper_profiler


def load_data(year: int, day: int, test=False) -> list[str]:
    if 2015 <= year <= 2021 and 1 <= day <= 25:
        try:
            zero = "0"*(day < 10)
            filename = "test.txt" if test else "input.txt"
            path = Path.home() / datadir / f"{year}/{zero}{day}/{filename}"
            with open(path) as f:
                data = [line.strip() for line in f.readlines()]
            return data
        except FileNotFoundError:
            raise ProblemNotFound
    else:
        raise InvalidEvent
