from collections import namedtuple

Person = namedtuple("Person", "name, age")


def main():
    people = [
        Person('Sarah', 28),
        Person('Lilly', 24),
        Person('Matt', 32),
        Person('Zoe', 40),
        Person('Jake', 50),
        Person('Jake', 10),
    ]

    people.sort()
    print("Default sort:")
    print(people)
    print()

    people.sort(key=lambda p: -p.age)
    print("Sort by age:")
    print(people)
    print()

    cutoff = 30
    people.sort(key=lambda p: -p.age if p.age > cutoff else p.age)
    print("Sort by age (grouped):")
    print(people)


if __name__ == '__main__':
    main()
