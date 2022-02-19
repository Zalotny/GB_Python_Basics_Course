import sys


def add_data(argv) -> int:
    program, *list_sales = argv
    num_param = len(list_sales)
    bakery_lines = []

    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        if num_param > 2:
            print('Неправильное количество параметров!')
            return 1
        elif num_param == 0:
            bakery_lines = bakery.readlines()
        else:
            start_num = int(list_sales[0])
            end_num = 0
            if num_param == 2:
                end_num = int(list_sales[1])

            i = 0
            while True:
                i += 1
                line_bakery = bakery.readline()
                if line_bakery == '' or i > end_num > 0:
                    break
                elif not i < start_num:
                    bakery_lines.append(line_bakery)

    for line in bakery_lines:
        print(line.strip())

    return 0


if __name__ == '__main__':
    sys.exit(add_data(sys.argv))
