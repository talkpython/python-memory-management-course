import sys

def main():
    print("See block/pool/arena stats:")

    # noinspection PyProtectedMember,PyUnresolvedReferences
    sys._debugmallocstats()

    # Make it do memory things!
    data = []
    for i in range(100_000):
        x = i ** 2
        data.append(list(str(x) * 100))

    print("After doing lots of stuff!", flush=True)
    # noinspection PyProtectedMember,PyUnresolvedReferences
    sys._debugmallocstats()


if __name__ == '__main__':
    main()
