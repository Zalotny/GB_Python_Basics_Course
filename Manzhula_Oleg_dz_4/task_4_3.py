import requests
import datetime


def parse_tag(tag: str, cont: str, cur_start_pos: int) -> float:
    value_pos_start = cont.find(f'<{tag}>', cur_start_pos) + len(tag)+2
    value_pos_end = cont.find(f'</{tag}>', cur_start_pos)
    value_str = cont[value_pos_start:value_pos_end]
    value = float(value_str.replace(",", "."))

    return value


def currency_rates_adv(code: str) -> list:
    """
    Возвращает курс валюты `code` по отношению к рублю и дату которая передаётся в ответе сервера
    Варианты ответа:
    [None, None] - не удалось получить данные от сервера
    [None, `Дата`] - не удалось найти валюту по переданному code, `Дата` - дата в ответе от сервера
    [`Курс`, `Дата`] - успешно получен курс `Курс` на дату `Дата`
    """
    result_list = [None, None]

    if not isinstance(code, str):
        return result_list  # в качестве `code` передана не строка

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code != 200:
        return result_list  # не получены данные от сервера

    cont = response.text

    # Парсим дату ответа сервера
    cur_date_position = cont.find('<ValCurs Date="') + 15  # определяем начальную позицию строки даты
    cur_date_str = cont[cur_date_position:cur_date_position + 10]  # получаем дату строкой (ДД.ММ.ГГГГ = 10 символов)
    day, month, year = cur_date_str.split('.')
    cur_date = datetime.date(year=int(year), month=int(month), day=int(day))
    result_list[1] = cur_date

    # Ищем валюту в ответе сервера по строке `code` в верхнем регистре
    cur_start_pos = cont.find(f'<CharCode>{code.upper()}')
    if cur_start_pos == -1:
        return result_list  # валюты с таким `code` нет в ответе сервера

    value = parse_tag('Value', cont, cur_start_pos)  # Парсим курс валюты
    nominal = parse_tag('Nominal', cont, cur_start_pos)  # Парсим кратность валюты
    result_value = value / nominal  # Рассчитываем курс валюты для единицы
    result_list[0] = result_value

    return result_list


kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
