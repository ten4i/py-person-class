class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        if not name:
            raise ValueError("Name cannot be empty")

        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for one_person in people:
        person_list.append(Person(one_person["name"], one_person["age"]))

    for one_person in people:
        curent = Person.people[one_person["name"]]
        if "husband" in one_person and one_person["husband"] is not None:
            curent.husband = Person.people[one_person["husband"]]

        if "wife" in one_person and one_person["wife"] is not None:
            curent.wife = Person.people[one_person["wife"]]

    return person_list
