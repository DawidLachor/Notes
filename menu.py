### Wykonał Dawid Lachor 142940
from notes import Note, Notebook


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self._options = {"1": self.show_notes, "2": self.search_notes, "3": self.add_note, "4": self.modify_note,
                         "5": self.quit}

    def show_menu(self):
        for i in range(1, len(self._options) + 1):
            print(str(i) + '. ' + self._options[str(i)].__name__.capitalize().replace('_', " "))
        self.run()
        print()

    def show_notes(self):
        if self.check_is_note() is True:
            for note in self.notebook.notes:
                print(note)

    def search_notes(self):
        if self.check_is_note() is True:
            text = input("Enter the text: ")
            for note in self.notebook.search(text):
                print(note)

    def add_note(self):
        text = input("Enter the text of the note: ")
        tag = input("Enter the tag of the note: ")

        self.notebook.new_note(Note(text, tag))

    def modify_note(self):
        if self.check_is_note() is True:
            id = int(input("Enter the ID of the note: "))
            text = input("Enter the new text: ")

            print(self.notebook.modify_text(id, text))

    def quit(self):
        exit()

    def check_is_note(self):
        if self.notebook.notes.__len__() == 0:
            print("No notes.")
            return False
        else:
            return True

    def run(self):
        number = input("Enter the option number from the menu to select it: ")
        if number in self._options:
            var = self._options[number]
            var()
        else:
            print("There is no such option in the menu.")
        self.show_menu()
