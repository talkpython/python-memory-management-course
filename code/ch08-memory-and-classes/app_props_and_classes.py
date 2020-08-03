import datetime
import os
import sys
from typing import List

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ch03-mem-and-variables'))
sys.path.insert(0, folder)
import size_util

from props_people import PersonNaive, PersonEfficient, PersonEfficientSlotted

Person = PersonNaive


def main():
    global Person

    print(f"Running with person implementation: {Person.__name__}...")
    retirement_summary()
    crowd = create_a_crowd()
    print(f"Size of crowd: {size_util.get_full_size(crowd) / 1024 / 1024:,.0f} MB")
    print()

    Person = PersonEfficient
    print(f"Running with person implementation: {Person.__name__}...")
    retirement_summary()
    crowd = create_a_crowd()
    print(f"Size of crowd: {size_util.get_full_size(crowd) / 1024 / 1024:,.0f} MB")
    print()

    Person = PersonEfficientSlotted
    print(f"Running with person implementation: {Person.__name__}...")
    retirement_summary()
    crowd = create_a_crowd()
    print(f"Size of crowd: {size_util.get_full_size(crowd) / 1024 / 1024:,.0f} MB")
    print()


def retirement_summary():
    birthday = datetime.datetime(year=1974, day=7, month=8)
    monthly_income = 7_000
    p = Person('Sarah', 'Sampson', birthday, monthly_income)
    print(f"Hi {p.full_name}. Let's review your retirement.")
    print(f"You're {p.age_in_years} years old.")
    print(f"You currently make ${p.yearly_income:,} dollars per year.")
    print(f"You have {p.years_to_retire} years until retirement.")
    print("Be sure to put some in the bank/retirement account each month.")


def create_a_crowd() -> List[Person]:
    t0 = datetime.datetime.now()
    try:
        return [
            Person("First", "Last", datetime.datetime.now(), 5000)
            for _ in range(0, 100_000)
        ]
    finally:
        dt = datetime.datetime.now() - t0
        print(f"Crowd created in {dt.total_seconds() * 1000:,.0f} ms.")


if __name__ == '__main__':
    main()
