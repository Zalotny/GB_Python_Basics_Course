import sys


def add_data(argv) -> int:
    """Добавлет в файл одну или несколько записей (в зависимости от количества переданных параметров)"""
    program, *list_sales = argv

    with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        for sale in list_sales:
            bakery.write(f'{sale}\n')

    return 0


if __name__ == '__main__':
    sys.exit(add_data(sys.argv))
