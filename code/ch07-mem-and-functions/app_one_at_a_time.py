import datetime
import os
import random
import sys
from itertools import islice
from typing import List, Generator, Iterator

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ch03-mem-and-variables'))
sys.path.insert(0, folder)
import size_util

random.seed(42)


def main():
    # Took 83 MB in naive mode
    start_mem = report("Starting")

    t0 = datetime.datetime.now()

    original = load_data(); report("Load")
    filtered = filter_data(original); report("filtered")
    scaled = scale_data(filtered, 2.718); report("scaled")

    # Need to work with it over and over and index it?
    # scaled = list(scaled)

    print("Head", list(islice(scaled, 0, 10)))
    tail = []
    for n in scaled:
        tail.append(n)
        if len(tail) > 10:
            tail.pop(0)
    print("Tail", tail)

    final_mem = report("done")
    dt = datetime.datetime.now() - t0
    print(f"Done, mem usage: {final_mem-start_mem:,.0f} MB, in {dt.total_seconds():.2f} sec")


def report(step_name: str):
    print(f"{step_name}:", end=' ')
    return size_util.report_process_mem()


def load_data() -> Iterator[int]:
    return (random.randint(1_000, 10_000) for _ in range(1, 1_000_000))


def filter_data(data: Iterator[int]) -> Iterator[int]:
    for n in data:
        if n % 5 != 0:
            yield n


def scale_data(data: Iterator[int], factor: float) -> Iterator[float]:
    return (
        n * factor
        for n in data
    )


if __name__ == '__main__':
    main()
