import weakref
from collections import defaultdict
from typing import List, Dict

from person import Person

__map: Dict[int, List] = defaultdict(list)


def add_friend(person: Person, friend: Person):
    if not person or not friend:
        return
    if person.id == friend.id:
        return

    if is_friend(person, friend):
        return

    current_friends = __map[person.id]
    current_friends.append(weakref.ref(friend))


def is_friend(person: Person, friend: Person) -> bool:
    if not person or not friend:
        return False
    if person.id == friend.id:
        return True

    friends: List[weakref] = __map[person.id]
    for ref in friends:
        f: Person = ref()
        if f and f.id == friend.id:
            return True

    return False


def get_friends(person: Person) -> List[Person]:
    friends: List[weakref] = __map[person.id]

    realized_friends = [p for ref in friends if (p := ref())]
    return realized_friends


def erase_person(person: Person):
    if person.id in __map:
        del __map[person.id]

    for lst in __map.values():
        for wr in lst:
            if (p := wr()) and p.id == person.id:
                lst.remove(wr)
