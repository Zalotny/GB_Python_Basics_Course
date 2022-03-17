class Date:
    """
    Класс для работы со строковым представлением даты в формате день-месяц-год: DD-MM-YYYY
    """

    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def date_numbers(cls, date_str: str):
        day, month, year = map(lambda num: int(num), date_str.split('-'))
        return {'day': day, 'month': month, 'year': year}

    @staticmethod
    def date_validate(date_str):
        try:
            date_dict = Date.date_numbers(date_str)
        except ValueError:
            return False

        if 2100 < date_dict['year'] < 1900 or 12 < date_dict['month'] < 1 or 31 < date_dict['day'] < 1:
            # имеем заведомо некорректные данные:
            # корректным годом считаем год в периоде 1900 - 2100
            # корректным номером месяца значение от 1 до 12
            # корректной датой месяца считаем значение от 1 до 31
            return False

        # проверяем год на высокосность
        is_leap = (date_dict['year'] % 4 == 0 and date_dict['year'] % 100 != 0 or date_dict['year'] % 400 == 0)

        month_days = 31
        if date_dict['month'] == 2:
            if is_leap:
                month_days = 29
            else:
                month_days = 28
        elif date_dict['month'] in [4, 6, 9, 11]:
            month_days = 30
        if date_dict['day'] > month_days:
            return False

        return True


if __name__ == '__main__':
    print(Date.date_numbers('21-12-2022'))
    print(Date.date_validate('21-12-2022'))
    print(Date.date_validate('31-02-2022'))
    print(Date.date_validate('21122022'))
