"""Minimal reproducible example of possible Pyre-check bug."""
from collections.abc import Generator


def infinite_stream(start: int) -> Generator[int, None, None]:
    """From https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines."""
    while True:
        yield start
        start += 1
