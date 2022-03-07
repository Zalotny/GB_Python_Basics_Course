import re
import os


def log_parse(line: str) -> list:
    """
    Парсит файл логa web-сервера из nginx_logs.txt, расположенного в папке файла модуля,
    для получения информации вида:
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
    :param line: строка файла лога
    :return: кортеж (<remote_addr>, <request_datetime>, <request_type>,
                     <requested_resource>, <response_code>, <response_size>)
            | ValueError , если строка не соответствует шаблону лог-файла
    """

    re_line = re.compile(r'^([0-9a-z:.]+)\s-\s-\s\[([0-9]{2}/[A-Za-z]+/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}\s\+[0-9]{4})\]\s\"([A-Z]+)\s([0-9a-z/_-]+)\s[0-9A-Z/.]+\"\s([0-9]{,3})\s([0-9]+)')
    parce_line = re_line.findall(line)
    if not parce_line:
        raise ValueError(f'Wrong line\n{line}')
    return parce_line[0]


if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(project_dir, 'nginx_logs.txt')
    if os.path.exists(path_file):
        with open(path_file, 'r') as fl:
            for line in fl:
                log_parse(line.strip())
                # print(log_parse(line.strip()))
    else:
        print(f'Data-file not found:\n{path_file}')
