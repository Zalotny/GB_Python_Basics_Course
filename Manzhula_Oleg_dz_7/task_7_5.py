import os
import sys
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def write_file(args):
    if not len(args) == 2:
        print('Переданы некорректные параметры')
        return 1

    prog, dir_name = args
    if not len(dir_name.strip()):
        print('Передано пустое имя папки')
        return 1

    folder = os.path.join(BASE_DIR, args[1])
    if os.path.exists(folder):
        result_nonsort = {}
        for item in os.scandir(folder):
            if item.is_file(follow_symlinks=False):
                size = 10 ** len(str(item.stat().st_size - 1)) if item.stat().st_size > 0 else 10
                execution = os.path.splitext(item.name)[1]
                is_key = result_nonsort.setdefault(size)
                if not is_key:
                    result_nonsort[size] = []
                list_execution = result_nonsort[size]
                list_execution.append(execution)
                result_nonsort[size] = list_execution

        result_sort = {}
        list_keys = list(result_nonsort.keys())
        list_keys.sort(reverse=True)
        for i in list_keys:
            result_sort.setdefault(i, (len(result_nonsort[i]), sorted(list(dict.fromkeys(result_nonsort[i])))))

        result_as_str = json.dumps(result_sort)
        with open(f'{dir_name}_summary.json', 'w', encoding='utf-8') as f:
            f.write(result_as_str)
        return 0
    else:
        print(f'Не найден каталог {folder}')
        return 1


if __name__ == '__main__':
    sys.exit(write_file(sys.argv))
