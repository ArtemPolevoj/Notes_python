import json


class File:
    __file = "resource/nodes.json"
    __dis = {}

    def write(self, note):
        data = {note.get_id(): {
            'id': note.get_id(),
            'title': note.get_title(),
            'text': note.get_text(),
            'date': note.get_date(),
        }
        }
        try:
            with open(self.__file, 'r', encoding="utf-8") as read_file:
                self.__dis = json.load(read_file, object_hook=None)
            self.__dis.update(data)
            with open(self.__file, 'w', encoding="utf-8") as file_json:
                json.dump(self.__dis, file_json, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    def cleaning(self):
        try:
            with open(self.__file, 'w', encoding="utf-8") as file_json:
                json.dump(self.__dis, file_json, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False

    def reading(self):
        try:
            with open(self.__file, 'r', encoding="utf-8") as read_file:
                return json.load(read_file, object_hook=None)
        except Exception:
            return {-1: {'Ошибка': 'чтения файла.'}}

    def update(self, dis):
        try:
            with open(self.__file, 'w', encoding="utf-8") as file_json:
                json.dump(dis, file_json, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False