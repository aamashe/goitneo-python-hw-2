from collections import UserDict


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for _, record in book.users.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "change":
                print(change_phone(args, book))
            elif command == "phone":
                print(get_contact(book, args))
            elif command == "all":
                print(book)
            elif command == "find":
                print(find_contact(book, args))
            elif command == "delete":
                print(delete_contact(book, args))
            else:
                print("Invalid command.")
        except Exception as e:
            # Handle any type of exception
            print(f"{e}")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        Field.__init__(self, name)
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        Field.__init__(self, phone)
        phone_digits = ''.join(filter(str.isdigit, phone))
        if len(phone_digits) != 10:
            raise Exception("Invalid phone number")
        self.phone = phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.phone == phone:
                self.phones[i] = Phone(new_phone)
                return "Phone edited successfully."
        raise Exception("Missing phone number")

    def find_phone(self, phone):
        return phone in self.phones

    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(str(p.phone) for p in self.phones)}"


class AddressBook():
    def __init__(self):
        self.users = {}

    def add_record(self, record):
        self.users[record.name.name] = record

    def find(self, name):
        if name in self.users:
            return self.users[name]
        raise Exception("Contact missing")

    def delete(self, name):
        self.users.pop(name)

    def __str__(self):
        all = str('\n')
        for record in self.users.values():
            all += str(record) + '\n'

        return all


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(error_message):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error_message

        return inner
    return decorator


@input_error("Give me name and phone please.")
def add_contact(args, adress_book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    adress_book.add_record(record)
    return "Contact added."


@input_error("Give me name and phone please.")
def change_phone(args, adress_book):
    name, phone, newPhone = args
    adress_book.find(name).edit_phone(phone, newPhone)
    return "Contact changed."


@input_error("Give me name please.")
def get_contact(adress_book, args):
    name, = args
    return adress_book.add_record(Record(name))


@input_error("Give me name please.")
def find_contact(adress_book, args):
    name, = args
    return adress_book.find(name)


@input_error("Give me name please.")
def delete_contact(address_book, args):
    name, = args
    if address_book.find(name):
        address_book.delete(name)
        return "Contact deleted"
    return "Contact missing"


if __name__ == "__main__":
    main()
