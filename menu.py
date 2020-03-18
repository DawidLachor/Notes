class Menu:
    def __init__(self):
        # self.notebook = Notebook()
        self._options = {"1": self.show_notes, "2": self.search_notes, "3": self.add_note, "4": self.modify_note,
                         "5": self.quit}

    def show_menu(self):
        for i in self._options:
            print(i)

    def show_notes(self):
        print("show_notes")

    def search_notes(self):
        print("search_notes")

    def add_note(self):
        print("add_note")

    def modify_note(self):
        print("modify_note")

    def quit(self):
        exit()

    def run(self):
        number = input("Podaj numer opcji z menu by ją wybrać: ")
        if number in self._options:
            var = self._options[number]
            var()
        else:
            print("Nie ma takiej opcji w menu")


menu1 = Menu()
menu1.show_menu()
menu1.run()
