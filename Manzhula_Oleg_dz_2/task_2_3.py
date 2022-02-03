def convert_list_in_str(list_in: list) -> str:
    """Не создавая новый список (как говорят, in place),
        обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    numbers = ('+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    element_position = 0
    while element_position < len(list_in):
        # определяем является ли элемент списка числом
        element_sign = ''  # знак числа, если он указан явно
        element_new = ''  # число без знака
        for idx, element_symbol in enumerate(list_in[element_position]):
            if numbers.count(element_symbol) == 0 or idx > 0 and numbers.index(element_symbol) < 2:
                element_new = ''
                break
            elif numbers.index(element_symbol) < 2:
                element_sign = element_symbol
            else:
                element_new += element_symbol
        if element_new != '':
            # элемент списка является числом: приведем его к виду двузначного с лидирующими нулями и обрамим кавычками
            element_new = f'{element_sign}{int(element_new):02d}'
            if element_new != list_in[element_position]:
                list_in[element_position] = element_new
            list_in.insert(element_position + 1, '"')
            list_in.insert(element_position, '"')
            element_position += 2
        element_position += 1
    str_new = " ".join(list_in)

    # перекомпонуем результирующую строку: удалим лишние пробелы у кавычек
    str_out = ''
    str_start = 0
    str_position = 0
    quote_even = True  # признак указывающий на четность обрабатываемой кавычки
    while str_position < len(str_new):
        if str_new[str_position] == '"':
            quote_even = not quote_even
            if quote_even:
                # если кавычка четная в строке - убираем пробел перед ней
                str_out += str_new[str_start:str_position-1]+'" '
            else:
                # если кавычка нечетная в строке - убираем пробел после нее
                str_out += str_new[str_start:str_position+1]
            str_position += 2
            str_start = str_position
        else:
            str_position += 1
    if str_start < len(str_new)-2:
        # добавим остаток строки после последней найденной кавычки
        str_out += str_new[str_start:len(str_new)]
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
