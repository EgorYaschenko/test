import json


def load_data(file_name: str):
    librari = []
    with open(file_name, "r") as file:
        lib = json.load(file)
    for b in lib:
        librari.append(Library(b['id'], b['title'], b['author'], b['year'], b['status']))
    return librari


def save_data(librari: list):
    save_data = []
    for book in librari:
        save_data.append(book.__dict__)
    save_json = json.dumps(save_data)
    with open("data.json", "w") as file:
        file.writelines(save_json)


def print_info(librari: list):
    for l in librari:
        print(f'id: {l.id} {l.title}, автор: {l.author}, год издания: {l.year}. Cтатус - {l.status}')


def dell_book(id: str, librari: list):
    for book in librari:
        if id == book.id:
            librari.remove(book)


def search_book(search_value: str, librari: list):
    for book in librari:

        if search_value in [book.id, book.title, book.author, book.year]:
            return book


class Library():
    def __init__(self, id, title, author, year, status='в наличии'):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def change_status(self):
        if self.status == 'в наличии':
            self.status = 'выдана'
        elif self.status == 'выдана':
            self.status = 'в наличии'
