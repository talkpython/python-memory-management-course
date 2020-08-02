# ################################
#
# Pattern inspired by this article from the creator of FIL
# Clinging to memory: How Python function calls can increase your memory usage
# https://pythonspeed.com/articles/function-calls-prevent-garbage-collection/
# Hear more on Talk Python: https://talkpython.fm/274
#
import os
import random
import sys
from typing import List

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ch03-mem-and-variables'))
sys.path.insert(0, folder)
import size_util

random.seed(42)


def greedy_main():
    # Took 83 MB in naive mode
    start_mem = report("Starting")

    original = load_data(); report("Load")
    filtered = filter_data(original); report("filtered")
    scaled = scale_data(filtered, 2.718); report("scaled")

    print("Head", scaled[:5])
    print("Tail", scaled[-5:])

    final_mem = report("done")
    print(f"Done, mem usage: {final_mem-start_mem:,.0f} MB.")


def main():
    # Took 69 MB in single-variable mode
    start_mem = report("Starting")

    # Using single variable name to ensure data is cleaned
    # as soon as possible by dropping references to intermediate step data.
    data = load_data(); report("Load")
    data = filter_data(data); report("filtered")
    data = scale_data(data, 2.718); report("scaled")

    print("Head", data[:5])
    print("Tail", data[-5:])

    final_mem = report("done")
    print(f"Done, mem usage: {final_mem-start_mem:,.0f} MB.")


def report(step_name: str):
    print(f"{step_name}:", end=' ')
    return size_util.report_process_mem()


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
