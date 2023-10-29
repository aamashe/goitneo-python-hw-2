
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
