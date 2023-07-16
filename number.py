from file_work import File


class Number:
    @staticmethod
    def get_number(text, value):
        try:
            num = int(input(text))
        except ValueError:
            print('\tВведено не число.')
            return Number.get_number(text, value)
        if 1 <= num <= value:
            return num
        else:
            print('\tНе верное значение.')
            return Number.get_number(text, value)

    @staticmethod
    def get_key(text, dis):
        if len(dis) == 0:
            return 0
        elif len(dis) == 1 and [key for key in dis.keys()][0] == -1:
            return -1
        else:
            try:
                num = int(input(text))
            except ValueError:
                print('\tВведено не число.')
                return Number.get_key(text, dis)

            if str(num) in dis.keys():
                return num
            else:
                print('\tНе верное значение.')
                return Number.get_key(text, dis)

    @staticmethod
    def max_number():
        return max(File().reading().keys())