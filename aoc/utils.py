import inspect
import sys
from functools import wraps
from pathlib import Path
from time import perf_counter as timer

datadir = "dev/advent-of-code/src"


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


def load_data(test=False) -> list[str]:
    try:
        filename = "test.txt" if test else "input.txt"
        source = inspect.getsourcefile(sys._getframe(1))
        path = Path(source).parent / filename
        with open(path) as f:
            data = [line.strip() for line in f.readlines()]
        return data
    except FileNotFoundError as e:
        raise e
