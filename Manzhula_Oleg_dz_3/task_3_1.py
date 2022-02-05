NUM_DICT = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = NUM_DICT.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
