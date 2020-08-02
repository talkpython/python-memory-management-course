class Person:
    __next_id = 1

    def __init__(self, name: str):
        self.id = self.__gen_id()
        self.name = name
        self.friends = []

    @classmethod
    def __gen_id(cls) -> int:
        nxt = cls.__next_id
        cls.__next_id += 1

        return nxt

    def __del__(self):
        print(f"Person object cleaned up: {self.name} with id: {self.id}.", flush=True)
