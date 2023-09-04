import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, search_str):
        matching_contacts = []
        for contact in self.contacts:
            if search_str.lower() in contact.name.lower() or search_str in contact.phone:
                matching_contacts.append(contact)
        return matching_contacts

if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Зберегти адресну книгу")
        print("3. Відновити адресну книгу")
        print("4. Пошук контактів")
        print("5. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            contact = Contact(name, phone)
            address_book.add_contact(contact)
            print("Контакт додано!")

        elif choice == "2":
            filename = input("Введіть ім'я файлу для збереження: ")
            address_book.save_to_file(filename)
            print("Адресну книгу збережено!")

        elif choice == "3":
            filename = input("Введіть ім'я файлу для відновлення: ")
            address_book.load_from_file(filename)
            print("Адресну книгу відновлено!")

        elif choice == "4":
            search_str = input("Введіть рядок для пошуку: ")
            matching_contacts = address_book.search_contacts(search_str)
            if matching_contacts:
                print("Знайдено контакти:")
                for contact in matching_contacts:
                    print(f"Ім'я: {contact.name}, Номер телефону: {contact.phone}")
            else:
                print("Контакти не знайдено!")

        elif choice == "5":
            break