import datetime


class PersonNaive:

    def __init__(self, first: str, last: str, birthdate: datetime.datetime, monthly_income: int):
        self.first = first
        self.last = last
        self.monthly_income = monthly_income
        self.birthdate = birthdate

        self.full_name = f'{first} {last}'
        now = datetime.datetime.now()
        age_delta = (now - birthdate) / datetime.timedelta(days=365)
        self.age_in_years = int(age_delta)

        self.yearly_income = 12 * monthly_income
        self.years_to_retire = max(0, 65 - self.age_in_years)


class PersonEfficient:
    def __init__(self, first: str, last: str, birthdate: datetime.datetime, monthly_income: int):
        self.first = first
        self.last = last
        self.monthly_income = monthly_income
        self.birthdate = birthdate

    @property
    def full_name(self) -> str:
        return f'{self.first} {self.last}'

    @property
    def age_in_years(self) -> int:
        now = datetime.datetime.now()
        age_delta = (now - self.birthdate) / datetime.timedelta(days=365)
        return int(age_delta)

    @property
    def yearly_income(self):
        return 12 * self.monthly_income

    @property
    def years_to_retire(self):
        return max(0, 65 - self.age_in_years)
