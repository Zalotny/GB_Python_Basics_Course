from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pars_line = line.split(' ')
    return pars_line[0], pars_line[5][1:], pars_line[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for fr_line in fr:
        list_out.append(get_parse_attrs(fr_line))

pprint(list_out)
