import os
import sys
from collections import Counter


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_data(args):
    if not len(args) == 2:
        print('Переданы некорректные параметры')
        return 1

    prog, dir_name = args
    if not len(dir_name.strip()):
        print('Передано пустое имя папки')
        return 1

    folder = os.path.join(BASE_DIR, args[1])
    if os.path.exists(folder):
        sizes = [10**len(str(item.stat().st_size-1)) if item.stat().st_size > 0 else 1
                 for item in os.scandir(folder)]
        result_nonsort = dict(Counter(sizes))

        result_sort = {}
        list_keys = list(result_nonsort.keys())
        list_keys.sort(reverse=True)
        for i in list_keys:
            result_sort.setdefault(i, result_nonsort[i])
        print(result_sort)
        return 0
    else:
        print(f'Не найден каталог {folder}')
        return 1


if __name__ == '__main__':
    sys.exit(get_data(sys.argv))
