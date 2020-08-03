# ################################
#
# Pattern inspired by this article from the creator of FIL
# Clinging to memory: How Python function calls can increase your memory usage
# https://pythonspeed.com/articles/function-calls-prevent-garbage-collection/
# Hear more on Talk Python: https://talkpython.fm/274
#
import datetime
import os
import random
import sys
from typing import List

from memory_profiler import profile

random.seed(42)


@profile
def main():
    original = load_data()
    filtered = filter_data(original)
    scaled = scale_data(filtered, 2.718)

    print("Head", scaled[:5])
    print("Tail", scaled[-5:])

    print(f"Done!")


def load_data() -> List[int]:
    return [random.randint(1_000, 10_000) for _ in range(1, 1_000_000)]


def filter_data(data: List[int]) -> List[int]:
    return [
        n
        for n in data
        if n % 5 != 0
    ]


def scale_data(data: List[int], factor: float) -> List[float]:
    return [
        n * factor
        for n in data
    ]


if __name__ == '__main__':
    main()
