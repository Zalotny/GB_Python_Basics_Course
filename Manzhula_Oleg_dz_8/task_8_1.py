import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """

    # для упрощения примем, что адрес не содержит нац. символов и длина домена верхн. уровня - не более 4 симв.
    re_mail = re.compile(r'^[0-9a-z_.-]+@[0-9a-z-]+\.[a-z]{2,4}$')
    if len(re_mail.findall(email)) == 1:
        parce_list = email.split('@')
    else:
        raise ValueError(f'wrong email: {email}')
    return dict(username=parce_list[0], domain=parce_list[1])


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
