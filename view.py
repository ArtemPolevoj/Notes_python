class View:
    @staticmethod
    def main_menu():
        return ("\n\t\tПриложение \"ЗАМЕТКИ\".\n"
                "Главное меню:\n"
                "\t1. Добавить заметку.\n"
                "\t2. Редактировать заметку.\n"
                "\t3. Удалить заметку.\n"
                "\t4. Показать все заметки.\n"
                "\t5. Удалить все заметки.\n"
                "\t6. Выход.\n"
                "Выберите пункт меню: ")

    @staticmethod
    def info_create_msg(result):
        if result:
            print("\tЗаметка записана.")
        else:
            print("\tПри записи заметки произошла ошибка.")

    @staticmethod
    def input_note_title():
        return input("Введите заголовок заметки: ")

    @staticmethod
    def input_note_text():
        return input("Введите текст заметки: ")

    @staticmethod
    def input_remove_text():
        return "Введите номер заметки для удаления: "

    @staticmethod
    def input_update_text():
        return "Введите номер заметки для редактирования: "

    @staticmethod
    def show_remove(dis):
        if len(dis) == 0:
            View.lack_note()
        else:
            for key, value in dis.items():
                print(key, value)

    @staticmethod
    def info_remove_msg(result):
        if result:
            print("\tЗаметка удалена.")
        else:
            print("\tПри удалении заметки произошла ошибка.")

    @staticmethod
    def info_update_msg(result):
        if result:
            print("\tЗаметка обновлена.")
        else:
            print("\tПри обновлении заметки произошла ошибка.")

    @staticmethod
    def show_note(dis):
        if len(dis) == 0:
            View.lack_note()
        else:
            for value in dis.values():
                for key, val in value.items():
                    print(key, val)
                print()

    @staticmethod
    def info_cleaning_msg(result):
        if result:
            print("\tВсе заметки удалены.")
        else:
            print("\tПри удалении заметок произошла ошибка.")

    @staticmethod
    def exit_msg():
        print("\t\tДо свидания.")

    @staticmethod
    def lack_note():
        print("\tЗаметки отсутствуют.")
