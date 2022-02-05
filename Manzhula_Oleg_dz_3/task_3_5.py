from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = list()
    for num in range(count):
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count=1, uniq=False) -> list:
    """Формирует заданное количество шуток, сформированных из трех случайных слов,
    взятых из трёх списков (по одному из каждого) с возможностью запретить повторное
    использование слов уже использованных ранее

    :param count: количество шуток
    :param uniq: признак запрещающий повторы слов в шутках
                 (True - каждое слово можно использовать только в одной шутке,
                 False - количество использований слов не ограничено)
    :return: список с шутками"""

    list_out = list()
    max_uniq_jokes = min(len(nouns), len(adverbs), len(adjectives))
    if uniq:
        if count > max_uniq_jokes:
            print(f'Зпрошенное количество уникальных шуток ({count} шт.) превышает количество доступное для формирования на основе заданных списков слов.')
            print(f'Будет сформировано максимально возможное количество: {max_uniq_jokes} шт. \n')
            count = max_uniq_jokes

        list_used = list()
        for num in range(count):
            joke = f'{choice(list(filter(lambda word: word not in list_used, nouns)))} ' \
                   f'{choice(list(filter(lambda word: word not in list_used, adverbs)))} ' \
                   f'{choice(list(filter(lambda word: word not in list_used, adjectives)))}'
            list_out.append(joke)
            list_used.extend(joke.split(" "))
    else:
        list_out = get_jokes(count)

    return list_out

print(get_jokes_adv(count=2, uniq=True))
print(get_jokes_adv(count=10, uniq=True))
