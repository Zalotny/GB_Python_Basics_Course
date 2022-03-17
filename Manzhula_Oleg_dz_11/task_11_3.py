class CreateNumbersList(Exception):
    def __init__(self):
        self.num_list = []

    def __str__(self):
        return ', '.join(map(lambda num: str(num), self.num_list))

    @staticmethod
    def is_number(check_str: str):
        temp_str = check_str
        if check_str[0] == '-':
            temp_str = check_str[1:]
        if temp_str[0].isdigit() and temp_str[-1].isdigit() and temp_str.count('.') < 2:
            pos_pnt = temp_str.find('.')
            if pos_pnt > 0:
                return temp_str[:pos_pnt].isdigit() and temp_str[pos_pnt+1:].isdigit()
            else:
                return temp_str.isdigit()
        return False

    def add_to_list(self, add_str: str):
        try:
            if not self.is_number(add_str):
                raise CreateNumbersList
            add_num = float(add_str) if '.' in add_str else int(add_str)
            self.num_list.append(add_num)
        except CreateNumbersList:
            print(f'Значение {add_str} не является числом!')


if __name__ == '__main__':
    numbers_list = CreateNumbersList()
    while True:
        str_in = input('Введите число:\n')
        if str_in == 'stop':
            break
        numbers_list.add_to_list(str_in)
    print(numbers_list)
