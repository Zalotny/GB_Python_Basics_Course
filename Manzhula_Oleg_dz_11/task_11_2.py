class DivZeroExeption(ZeroDivisionError):
    _out_message = 'попытка деления на 0'

    def __init__(self, message: str = ''):
        if message:
            self._out_message = message

    def __str__(self):
        return self._out_message

    @staticmethod
    def is_zero(num):
        if num == 0:
            raise DivZeroExeption


arg_1 = input('Введите делимое:\n')
arg_2 = input('Введите делитель:\n')

num_1 = int(arg_1)
num_2 = int(arg_2)

try:
    DivZeroExeption.is_zero(num_2)
    print(f'{num_1} / {num_2} = {num_1 / num_2}')
except DivZeroExeption:
    print(f'Попытка разделить {num_1} на 0!')
