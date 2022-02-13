import sys
import utils


def print_currency_rates(argv):
    program, *args = argv
    for currency in args:
        kurs, date_value = utils.currency_rates_adv(currency.upper())
        print(kurs, date_value, sep=', ')

    return 0


if __name__ == '__main__':
    sys.exit(print_currency_rates(sys.argv))


'''
Console:
C:\Python38\python.exe C:/GeekBrains/PyProjects/GB_Python_Basics_Course/Manzhula_Oleg_dz_4/task_4_5.py

Process finished with exit code 0

Terminal:
PS C:\GeekBrains\PyProjects\GB_Python_Basics_Course\Manzhula_Oleg_dz_4> python task_4_5.py USD UaH eur plN RUR
74.8015, 2022-02-10
2.67306, 2022-02-10
85.3784, 2022-02-10
18.9184, 2022-02-10
None, 2022-02-10
PS C:\GeekBrains\PyProjects\GB_Python_Basics_Course\Manzhula_Oleg_dz_4> 
'''