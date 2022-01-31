def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = list()
    for elem in list_in:
        list_words = elem.split(' ')
        list_out.append(f'Привет, {list_words[len(list_words) - 1].capitalize()}!')
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
