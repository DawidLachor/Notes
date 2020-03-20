from notes import Note, Notebook


class Menu:
    def __init__(self):
        # self.notebook = Notebook()
        self._options = {"1": self.show_notes, "2": self.search_notes, "3": self.add_note, "4": self.modify_note,
                         "5": self.quit}
        self.n = Notebook()

    def show_menu(self):
        for i in range(1, len(self._options) + 1):
            print(i, self._options[str(i)].__name__)
        self.run()

    def show_notes(self):
        for note in self.n.notes:
            print(note)

    def search_notes(self):
        text = input("Podaj tekst: ")
        for note in self.n.search(text):
            print(note)

    def add_note(self):
        text = input("Podaj tekst notatki: ")
        tag = input("Podaj tag notatki: ")

        self.n.new_note(Note(text, tag))

    def modify_note(self):
        id = int(input("Podaj ID notatki do zmiany: "))
        text = input("Podaj nowy tekst: ")

        print(self.n.modify_text(id, text))

    def quit(self):
        exit()

    def run(self):
        number = input("Podaj numer opcji z menu by ją wybrać: ")
        if number in self._options:
            var = self._options[number]
            var()
        else:
            print("Nie ma takiej opcji w menu")
        self.show_menu()


menu1 = Menu()
menu1.show_menu()
menu1.run()
