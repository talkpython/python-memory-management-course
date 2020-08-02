import weakref

from person import Person


def main():
    p1 = Person('Michael')
    p2 = Person('Sarah')

    if input('Create cycle [y/n]? ') == 'y':
        p1.friends.append(p2)
        p2.friends.append(p1)

    w1 = weakref.ref(p1)
    w2 = weakref.ref(p2)

    p1 = None
    p2 = None

    print("Program closing, kthxbye!", flush=True)

    if w1() or w2():
        print("Cycle found! Objects still alive beyond references.")
    else:
        print("No cycles found.")


if __name__ == '__main__':
    main()
