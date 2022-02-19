def prepare_dataset(path_users_file: str, path_hobby_file: str, users_hobby_file: str) -> None:
    """
    Считывает данные из файлов и сохранить объединенные данные в новый файл, где:
    строки имеют вид '<ФИО>: <данные о хобби>'
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :param users_hobby_file: путь до результирующего файла, содержащий пары вида '<ФИО>: <данные о хобби>'
    :return: None
    """
    users_file = open(path_users_file, 'r', encoding='utf-8')
    hobby_file = open(path_hobby_file, 'r', encoding='utf-8')
    with open(users_hobby_file, 'a', encoding='utf-8') as users_hobby:
        while True:
            users_line = users_file.readline().strip()
            hobby_line = hobby_file.readline().strip()
            if not (users_line or hobby_line):
                # Оба файла закончились - заканчиваем писать в файл
                # Тут же можно прописать контроли на неравенство к-ва строк в файлах
                # с соответствующим поведением (как в прошлом здании)
                break
            users_hobby.write(f'{users_line}: {hobby_line}\n')
    users_file.close()
    hobby_file.close()


prepare_dataset('users.csv', 'hobby.csv', 'users_hobby.txt')
