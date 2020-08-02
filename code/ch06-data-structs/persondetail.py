class PersonDetail:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def __repr__(self):
        return f"{self.name} is {self.age}"

