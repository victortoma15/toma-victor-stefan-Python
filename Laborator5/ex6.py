class LibraryItem:
    def __init__(self, title, author, item_id, checked_out):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = checked_out

    def check_out(self):
        if self.checked_out:
            print("Produsul a fost deja imprumutat")
        else:
            self.checked_out = True
            print("Produsul a fost imprumutat cu succes")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print("Produsul a fost returnat cu succes")
        else:
            print("Produsul este deja returnat")

    def display_info(self):
        print("--------------------")
        print(f"Titlu: {self.title}")
        print(f"Autor: {self.author}")
        print(f"ID: {self.item_id}")
        print(f"Imprumutat: {self.checked_out}")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, num_pages):
        super().__init__(title, author, item_id, checked_out)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Numarul de pagini: {self.num_pages}")
        print("--------------------")


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, runtime):
        super().__init__(title, author, item_id, checked_out)
        self.runtime = runtime

    def display_info(self):
        super().display_info()
        print(f"Durata: {self.runtime}")
        print("--------------------")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, year):
        super().__init__(title, author, item_id, checked_out)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Anul publicarii: {self.year}")
        print("--------------------")


def main():
    book = Book("White Fang", "Jack London", 1, False, 180)
    dvd = DVD("Liceenii", "Nicolae Corjos", 2, False, 175)
    magazine = Magazine("CanCan", "Presa Romana", 3, False, 2021)

    book.check_out()
    dvd.check_out()
    magazine.check_out()

    book.display_info()
    dvd.display_info()
    magazine.display_info()

    book.return_item()
    dvd.return_item()
    magazine.return_item()

    book.display_info()
    dvd.display_info()
    magazine.display_info()


main()
