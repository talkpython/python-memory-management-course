import datetime
from typing import Union

from props_people import PersonEfficient, PersonEfficientSlotted


def main():
    standard_obj = PersonEfficient('Sarah', 'Sanderson', datetime.datetime.now(), 5000)
    print("Testing speed with standard class:")
    std_time = test_access(standard_obj)

    slot_obj = PersonEfficientSlotted('Sarah', 'Sanderson', datetime.datetime.now(), 5000)
    print("Testing speed with slot-based class:")
    slot_time = test_access(slot_obj)

    max_time = max(std_time, slot_time)
    if std_time < slot_time:
        print("Regular FASTER")
    else:
        print("Slots FASTER")

    print(f'Speed gain of slots: {(max_time / slot_time - 1) * 100:.1f}%')


def test_access(obj: Union[PersonEfficient, PersonEfficientSlotted]):
    t0 = datetime.datetime.now()
    count = 100_000
    for _ in range(count):
        # noinspection PyUnusedLocal
        a, b, c, d = obj.first, obj.last, obj.birthdate, obj.monthly_income

    dt = datetime.datetime.now() - t0
    print(f"{4 * count:,} ops done in {dt.total_seconds() * 1000:,.1f} ms, " +
          f"{4 * count / dt.total_seconds() :,.2f} ops per second")

    return dt.total_seconds()


if __name__ == '__main__':
    main()
