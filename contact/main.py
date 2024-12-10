import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
    for i, person in enumerate(people):
        print(i+1, "-", person["name"], "|",
              person["age"], "|", person["email"])


def delete_contact(people):
    display_people(people)

    while True:
        num = input("Enter a number to delete: ")
        try:
            num = int(num)
            if num <= 0 or num > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number")

    people.pop(num - 1)
    print("Person Deleted.")


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)


print("Hi, welcome to the contact Management system.")
print()

with open("contact/data.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list size:", len(people))
    command = input(
        "You can 'Add', 'Delete' or 'Search' and 'Q' for quit 'p' for print contact: ").lower()

    if command == 'add' or command == 'a':
        person = add_person()
        people.append(person)
        print("Person Added!")
    elif command == 'delete' or command == 'd':
        delete_contact(people)
    elif command == 'search' or command == 's':
        search(people)
    elif command == 'q':
        break
    elif command == 'p':
        display_people(people)
    else:
        print("Invalid command.")

with open("contact/data.json", "w") as f:
    json.dump({"contacts": people}, f)
