import weakref

import friend_map
from person import Person


def main():
    print("VERSION WITH NO CYCLES!")
    p1 = Person('Michael')
    p2 = Person('Sarah')
    p3 = Person('Zoe')

    if input('Create cycle [y/n]? ') == 'y':
        friend_map.add_friend(p1, p2)
        friend_map.add_friend(p2, p1)

    print(f"Is {p1.name} a friend of {p2.name}? {'Yes' if friend_map.is_friend(p2, p1) else 'No'}.")
    print(f"Is {p1.name} a friend of {p3.name}? {'Yes' if friend_map.is_friend(p3, p1) else 'No'}.")

    print([p.name for p in friend_map.get_friends(p1)])

    w1 = weakref.ref(p1)
    w2 = weakref.ref(p2)

    p1 = None
    p2 = None
    p3 = None

    print("Program closing, kthxbye!", flush=True)

    if w1() or w2():
        print("Cycle found! Objects still alive beyond references.")
    else:
        print("No cycles found.")


if __name__ == '__main__':
    main()
