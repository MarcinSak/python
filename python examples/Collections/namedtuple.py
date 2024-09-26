from collections import namedtuple

if __name__ == "__main__":
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    print("Point 1:", p1)
    print("X coordinate:", p1.x)
    print("Y coordinate:", p1.y)

    Person = namedtuple('Person', ['name', 'age', 'city'])
    person1 = Person(name='Alice', age=30, city='New York')
    print("\nPerson 1:")
    print("Name:", person1.name)
    print("Age:", person1.age)
    print("City:", person1.city)

    people = [
        Person(name='Bob', age=25, city='Los Angeles'),
        Person(name='Charlie', age=35, city='Chicago'),
    ]
    print("\nList of People:")
    for person in people:
        print(f"{person.name} is {person.age} years old and lives in {person.city}.")

    Book = namedtuple('Book', ['title', 'author', 'year'])
    book1 = Book(title='1984', author='George Orwell', year=1949)
    print("\nBook Details:")
    print(f"'{book1.title}' by {book1.author}, published in {book1.year}.")

    person_dict = person1._asdict()
    print("\nPerson Dictionary:")
    print(person_dict)
