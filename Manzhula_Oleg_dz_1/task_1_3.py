def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    last_numb = number % 10
    last_symbols = ''
    if (10 < number < 15) or last_numb == 0 or last_numb > 4:
        last_symbols = 'ов'
    elif last_numb > 1:
        last_symbols = 'а'
    return f'{number} процент{last_symbols}'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
