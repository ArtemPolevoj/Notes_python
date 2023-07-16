from datetime import datetime

from file_work import File
from note import Note


class Functional:
    @staticmethod
    def create_new_note(title, text):
        note = Note()
        note.set_title(title)
        note.set_text(text)
        return File().write(note)

    @staticmethod
    def cleaning_file():
        return File().cleaning()

    @staticmethod
    def reading_file():
        return File().reading()

    @staticmethod
    def update(id_note, title, text):
        dis = File().reading()
        data = {str(id_note): {
            'id': id_note,
            'title': title,
            'text': text,
            'date': datetime.now().strftime('%Y, %B %d, %A | %H:%M'),
        }
        }
        try:
            dis.update(data)
            return File().update(dis)
        except Exception:
            return False

    @staticmethod
    def remove_note(id_note):
        try:
            dis = File().reading()
            dis.pop(str(id_note))
            return File().update(dis)
        except Exception:
            return False
