def sort_dictionary(dict_unsort: dict) -> dict:
    """Формирует словарь, отсортированный по ключам (по алфавиту по всей глубине вложенности)

    :param dict_unsort: словарь передаваемый для сортировки
    :return: новый словарь, отсортированной по ключам по алфавиту"""

    dict_sort = {}

    key_list = sorted(list(dict_unsort))
    for key in key_list:
        dict_value = dict_unsort[key]
        if type(dict_value) is dict:
            dict_in = sort_dictionary(dict_value)
            dict_sort.setdefault(key, dict_in)
        else:
            dict_sort.setdefault(key, dict_value)

    return dict_sort


def thesaurus_adv(*args, sort=False) -> dict:
    """Формирует словарь, в котором ключи — первые буквы вторых слов переданных пар, а значения —
    словари, в которых ключи — первые буквы первых слов переданных пар, удовлетворяющих ключу, а значения —
    списки, содержащие строки пар целиком

    :param *args: перечень строк с парами слов
    :param sort: признак необходимости сортировки словаря по алфавиту (True - сортировать, False - не сортировать)
    :return: словарь пар слов по первым буквам"""

    dict_temp = {}  # результирующий словарь значений без сортировки
    for word in args:
        couple = word.split(" ")
        first_name = couple[0]
        second_name = couple[1]
        second_name_value = dict_temp.setdefault(second_name[0], dict())
        first_name_value = second_name_value.setdefault(first_name[0], list())
        if word not in first_name_value:
            first_name_value.append(word)
            second_name_value[first_name[0]] = first_name_value
            dict_temp[second_name[0]] = second_name_value

    if sort:
        dict_out = sort_dictionary(dict_temp)
    else:
        dict_out = dict_temp

    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
