import sys
import size_util


def main():
    print("Let's explore some sizes of objects")

    print("How big is the number 4?")
    print(sys.getsizeof(4))
    print(size_util.get_full_size(4))

    print("How big is the letter 'a'?")
    print(sys.getsizeof('a'))
    print(size_util.get_full_size('a'))

    print("How big is the string 'abcdefghijklmnopqrstuvwxyz'?")
    print(sys.getsizeof('a' * 26))
    print(size_util.get_full_size('a' * 26))

    print("How big is a list?")
    print(sys.getsizeof([]))
    print(size_util.get_full_size([]))

    print("How big is a list with 10 items?")
    print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(size_util.get_full_size([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print("How big is a list with 10 lists in it?")
    data = []
    for i in range(1, 11):
        item = [i] * (i * i * 10)
        data.append(item)

    print(sys.getsizeof(data))
    print(f"{size_util.get_full_size(data):,}")


if __name__ == '__main__':
    main()
