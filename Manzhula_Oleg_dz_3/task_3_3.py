def thesaurus(*args, sort=False) -> dict:
    """Формирует словарь, в котором ключи — первые буквы слов,
    а значения — списки, содержащие слова, начинающиеся с соответствующей буквы

    :param *args: перечень слов
    :param sort: признак необходимости сортировки словаря по алфавиту (True - сортировать, False - не сортировать)
    :return: словарь слов по первым буквам"""

    if sort:
        args = sorted(list(args))  # Changed in version 3.7: Dictionary order is guaranteed to be insertion order

    dict_out = {}
    for word in args:
        dict_value = dict_out.setdefault(word[0], list())
        if word not in dict_value:
            dict_value.append(word)
            dict_out[word[0]] = dict_value

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
