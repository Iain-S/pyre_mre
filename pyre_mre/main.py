"""Minimal reproducible example of possible Pyre-check bug."""

from collections.abc import Generator

type Nothing = None | None

def infinite_stream(start: int) -> Generator[int, Nothing, Nothing]:
    """From https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines."""
    while True:
        yield start
        start += 1
