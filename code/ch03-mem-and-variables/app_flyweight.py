def main():
    print("Example showing which numbers are precomputed and reused")
    print("AKA: The flyweight design pattern")
    print()
    print("Let's compare integers in [-1000, 1000] to see if any are reused.")

    list1 = list(range(-1000, 1000 + 1))
    list2 = list(range(-1000, 1000 + 1))

    reused = []
    for n1, n2 in zip(list1, list2):
        if id(n1) == id(n2):
            print(f"Found REUSED {n1}!")
            reused.append(n1)

    lowest = min(reused)
    highest = max(reused)

    print(f"Flyweight pattern from [{lowest}, {highest}]")


if __name__ == '__main__':
    main()
