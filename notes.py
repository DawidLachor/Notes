from datetime import date as d


class Note:
    id = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = d.today()
        self.id = Note.new_id()

    def __str__(self):
        return f"ID: {self.id} | Text: {self.text} | Tag: {self.tag} | Date: {self.date}"

    def match(self, value):
        if value in self.text or value in self.tag:
            return True
        else:
            return False

    @staticmethod
    def new_id():
        Note.id += 1
        return Note.id


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, note):
        self.notes.append(note)

    def modify_text(self, id, new_text):
        for note in self.notes:
            if note.id == id:
                note.text = new_text
                return "Pomyślnie zmieniono tekst"
        return "Brak notatki o takim ID"

    def modify_tag(self, id, new_tag):
        self.notes[self.notes.index(Note.id == id)].tag = new_tag

    def search(self, value):
        matching_notes = []
        for note in self.notes:
            if note.match(value):
                matching_notes.append(note)
        return matching_notes
