import weakref

from person import Person


def main():
    print("VERSION WITH NO CYCLES!")
    p1 = Person('Michael')
    p2 = Person('Sarah')
    p3 = Person('Zoe')

    if input('Create cycle [y/n]? ') == 'y':
        # TODO: Improve this with new data structures
        p1.friends.append(p2)
        p2.friends.append(p1)

    print(f"Is {p1.name} a friend of {p2.name}? {'Yes' if p1 in p2.friends else 'No'}.")
    print(f"Is {p1.name} a friend of {p3.name}? {'Yes' if p1 in p3.friends else 'No'}.")

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
