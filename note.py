class Note:
    __id = 0
    __title = ""
    __date = ""
    __text = ""
    __count = 0

    def __init__(self):
        self.set_date()
        self.__set_id()

    def __set_id(self):
        self.__id = int(Number.max_number()) + 1

    def set_title(self, title):
        if title == "":
            self.__title = str(self.get_id())
        else:
            self.__title = title

    def set_text(self, text):
        if text == "":
            self.__text = "Текст отсутствует."
        else:
            self.__text = text

    def set_date(self):
        self.__date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_date(self):
        return self.__date

    def get_text(self):
        return self.__text