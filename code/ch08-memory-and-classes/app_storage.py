import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ch03-mem-and-variables'))
sys.path.insert(0, folder)

import size_util


class Thing:
    def __init__(self, t1: str, t2: str):
        self.thing1 = t1
        self.thing2 = t2

        # self.__dict__['thing1'] = 1
        # self.thing1 = t1

    def __repr__(self):
        things = [self.thing1, self.thing2]
        if hasattr(self, 'thing3'):
            things.append(self.thing3)

        return f"Thing OBJ @{id(self)} with {things}"

    def __str__(self):
        return self.__repr__()


def main():
    things = [
        Thing("hat", "mat"),
        Thing("dog", "cat"),
        Thing("bat", "bird"),
        Thing("car", "bike"),
    ]

    print(things)
    print()

    dicts = [
        obj.__dict__
        for obj in things
    ]

    print(dicts)
    print()

    size = size_util.get_full_size(dicts[0])
    print(f"Size of a class dict: {size} bytes.")
    size = size_util.get_full_size(things[0])
    print(f"Size of a class itself: {size} bytes.")
    print()

    locations = [id(d) for d in dicts]
    print(locations)
    print()

    # noinspection PyUnresolvedReferences
    things[-1].thing3 = "Dynamic lang!"

    print(dicts)


if __name__ == '__main__':
    main()
