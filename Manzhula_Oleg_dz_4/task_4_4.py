import utils


def print_currency_rates(code: str):
    kurs, date_value = utils.currency_rates_adv(code)
    print(kurs, date_value, sep=', ')


print_currency_rates("USD")
print_currency_rates("eur")
print_currency_rates(None)


"""
C:\Python38\python.exe C:/GeekBrains/PyProjects/GB_Python_Basics_Course/Manzhula_Oleg_dz_4/task_4_4.py
74.8015 2022-02-10
85.3784, 2022-02-10
None 2022-02-10

Process finished with exit code 0

Terminal:
PS C:\GeekBrains\PyProjects\GB_Python_Basics_Course\Manzhula_Oleg_dz_4> python task_4_4.py                    
74.8015 2022-02-10
85.3784, 2022-02-10
None 2022-02-10
PS C:\GeekBrains\PyProjects\GB_Python_Basics_Course\Manzhula_Oleg_dz_4> 
"""