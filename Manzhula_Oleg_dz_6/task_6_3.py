import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as usrs:
        users_list = [users_line.replace(',', ' ').strip() for users_line in usrs.readlines()]

    with open(path_hobby_file, 'r', encoding='utf-8') as hobby:
        hobby_list = [hobby_line.strip().split(',') for hobby_line in hobby.readlines()]

    delta = len(users_list) - len(hobby_list)
    if delta > 0:
        hobby_list.extend([None] * delta)
    elif delta < 0:
        sys.exit(1)

    return dict(zip(users_list, hobby_list))


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
