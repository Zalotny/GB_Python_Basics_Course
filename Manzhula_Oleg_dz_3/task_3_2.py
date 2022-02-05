NUM_DICT = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = NUM_DICT.get(value)
    return str_out


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский
    работает с числительными, начинающимися с заглавной буквы —
    результат тоже выводится с заглавной."""
    str_out = num_translate(value.lower())
    if str_out is not None and value != value.lower():
        str_out = str_out.capitalize()

    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("two"))
