import os
import shutil

import task_7_1


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(BASE_DIR, 'my_project')
if os.path.exists(path):
    path_list = os.walk(path, topdown=False)
    path = os.path.join(path, 'templates')
    if not os.path.exists(path):
        task_7_1.create_path(path)
    for path_step in path_list:
        if path_step[0][-9:] == 'templates':
            for mk_path in path_step[1]:
                path_new = os.path.join(path, mk_path)
                if not os.path.exists(path_new):
                    shutil.copytree(os.path.join(path_step[0], mk_path), path_new)
            for mk_path in path_step[2]:
                path_new = os.path.join(path, mk_path)
                if not os.path.exists(path_new):
                    shutil.copy(os.path.join(path_step[0], mk_path), path_new)
else:
    print(f'Не найден каталог {path}')
