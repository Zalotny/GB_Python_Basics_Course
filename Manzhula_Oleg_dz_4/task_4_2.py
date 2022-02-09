import requests
from decimal import Decimal


def currency_rates(code: str) -> float:
    """
    возвращает курс валюты `code` по отношению к рублю
    если валюта не найдена на сервере или сервер не отвечает - возвращается None
    """

    if not isinstance(code, str):
        return None  # в качестве `code` передана не строка

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code != 200:
        return None  # не получены данные от сервера

    cont = response.text

    # Ищем валюту в ответе сервера по строке `code` в верхнем регистре
    cur_start_pos = cont.find(f'<CharCode>{code.upper()}')
    if cur_start_pos == -1:
        return None  # валюты с таким `code` нет в ответе сервера

    # Парсим курс валюты
    value_pos_start = cont.find('<Value>', cur_start_pos) + 7
    value_pos_end = cont.find('</Value>', cur_start_pos)
    value = cont[value_pos_start:value_pos_end]

    # Парсим кратность валюты
    nominal_pos_start = cont.find('<Nominal>', cur_start_pos) + 9
    nominal_pos_end = cont.find('</Nominal>', cur_start_pos)
    nominal = cont[nominal_pos_start:nominal_pos_end]

    # Рассчитываем курс валюты для единицы, преобразовав строковые значения курса и кратности в числовые
    # (курс может быть дробным, а кратность - всегда целая)
    result_value = float(value.replace(",", ".")) / int(nominal)

    return result_value


print(currency_rates("USD"))
print(currency_rates("eur"))
print(currency_rates("noname"))

"""
1. Eсть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
При работе с имено с курсами валют, скорее - нет, т.к. разрядность дробной части курса может быть разной 
для разных валют, и она может увеличиваться для конкретной валюты (и это будет значимым) при приведении курса к кратности 1  
Decimal же предполагает использование фиксированной разрядности дробной части (либо по максимальной кратности
чисел участвующих в расчете, либо принудительно заданной).
Исключением будет случай, когда нам нужно будет ограничить разрядность каким-то значением, но в этом случае,
можно просто применить округление для значения типа float.
Если же говорить о денежных единицах, как о денежных суммах, то использование Decimal выглядит более оправданным,
т.к. у всех денежных величин кратность фиксирована и равна 2 знакам после запятой - до копеек, 
и такое представление сумм является обшепринятым.

2. Сильно ли усложняется код функции при этом?
    - Необходимо будет дополнительно импортировать класс Decimal модуля decimal (from decimal import Decimal)
    - Необходимо будет вместо преобразования курса из строки во float, а кратности из строки в int
        выполнять преобразование и курса и кратности в Decimal, т.к. этот класс не поддерживает 
        выполнение арифметических операций с другими типами
    - Возможно, необходимо будет принудительно увеличить разрядность результата преобразования курса к кратности 1
"""