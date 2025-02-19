"""Minimal reproducible example of possible Pyre-check bug."""
from typing import Generator


def infinite_stream(start: int) -> Generator[int]:
    """From https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines."""
    while True:
        yield start
        start += 1
