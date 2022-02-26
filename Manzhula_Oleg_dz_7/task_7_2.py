import os

import task_7_1


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(BASE_DIR, 'config.yaml'), 'r', encoding='utf-8') as config:
        for name in config:
            path = os.path.join(BASE_DIR, name.strip())
            if not os.path.exists(path):
                mk_dir, mk_file = os.path.split(path)
                task_7_1.create_path(mk_dir)
                if mk_file:
                    open(path, 'a').close()
except FileNotFoundError as err:
    print(f'Не удалось найти файл config.yaml:\n', rf'{err}')
