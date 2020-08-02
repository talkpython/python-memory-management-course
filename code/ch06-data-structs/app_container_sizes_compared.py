import array
import os
import random
import sys
from typing import List

from persondetail import PersonDetail

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ch03-mem-and-variables'))
sys.path.insert(0, folder)

import size_util


def main():
    random.seed(42)
    count = 100_000
    ages: List[int] = generate_ages(count)
    names: List[str] = generate_names(count)

    print("Storing them just as lists:")
    age_size = size_util.get_full_size(ages)
    name_size = size_util.get_full_size(names)
    total = age_size + name_size
    print(f"Ages: \t{age_size / 1024:,.0f} KB")
    print(f"Names: \t{name_size / 1024:,.0f} KB")
    print(f"Total: \t{total / 1024:,.0f} KB")

    print("Storing them as classes:")
    people = [PersonDetail(n, a) for n, a in zip(names, ages)]
    people_size = size_util.get_full_size(people)
    print(f"Cls: \t{people_size / 1024:,.0f} KB")

    print("Storing them as arrays:")
    ar = array.array('B')
    ar.fromlist(ages)
    array_size = size_util.get_full_size(ar)
    print(f"Array: \t{array_size / 1024:,.0f} KB")


def generate_ages(count):
    return [
        random.randint(18, 100)
        for _ in range(0, count)
    ]


def generate_names(count) -> List[str]:
    with open('./MOCK_NAMES.txt', 'r', encoding='utf-8') as fin:
        raw_full_names: List[str] = [
            name.strip()
            for name in fin.readlines()
            if name and name.strip()]

    data = []
    for _ in range(count):
        data.append(random.choice(raw_full_names))

    return data


if __name__ == '__main__':
    main()
