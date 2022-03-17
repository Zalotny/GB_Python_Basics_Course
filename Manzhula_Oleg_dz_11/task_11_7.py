from __future__ import annotations


class ComplexNumbers:
    def __init__(self, real_part: float, complex_part: float):
        self.real_part = real_part
        self.complex_part = complex_part

    def __str__(self):
        real_part = self.real_part if self.real_part else ''
        complex_part = ''
        if self.complex_part:
            complex_part = f'{"+" if self.complex_part > 0 and self.real_part else ""}{self.complex_part}i'

        return f'{real_part}{complex_part}'

    @staticmethod
    def is_complex_number(obj):
        if not isinstance(obj, ComplexNumbers):
            raise TypeError('аргумент не является комплексным числом')

    def __add__(self, other: ComplexNumbers):
        ComplexNumbers.is_complex_number(other)
        real_part = self.real_part + other.real_part
        complex_part = self.complex_part + other.complex_part
        return ComplexNumbers(real_part, complex_part)

    def __sub__(self, other: ComplexNumbers):
        ComplexNumbers.is_complex_number(other)
        real_part = self.real_part - other.real_part
        complex_part = self.complex_part - other.complex_part
        return ComplexNumbers(real_part, complex_part)

    def __mul__(self, other: ComplexNumbers):
        ComplexNumbers.is_complex_number(other)
        real_part = self.real_part * other.real_part - self.complex_part * other.complex_part
        complex_part = self.real_part * other.complex_part + other.real_part * self.complex_part
        return ComplexNumbers(real_part, complex_part)

    def __truediv__(self, other: ComplexNumbers):
        ComplexNumbers.is_complex_number(other)

        real_part = (self.real_part * other.real_part + self.complex_part * other.complex_part) / \
                    (other.real_part ** 2 + other.complex_part ** 2)
        complex_part = (other.real_part * self.complex_part - self.real_part * other.complex_part) / \
                       (other.real_part ** 2 + other.complex_part ** 2)
        return ComplexNumbers(real_part, complex_part)


if __name__ == '__main__':
    while True:
        numb_lst = []
        for i in range(4):
            num = input(f'Введите {"действительную" if i in [0,2] else "комплексную"} часть '
                        f'{"первого" if i < 2 else "второго"} числа:\n')
            if num == 'stop':
                break

            try:
                if '.' in num:
                    numb_lst.append(float(num))
                else:
                    numb_lst.append(int(num))
            except ValueError:
                print(f'Введенное значение "{num}" не является числом - расчет прерван')
                break

        if not len(numb_lst) == 4:
            break

        a, b, c, d = numb_lst
        numb_1 = ComplexNumbers(a, b)
        numb_2 = ComplexNumbers(c, d)

        print(f'Первое число: {numb_1}')
        print(f'Второе число: {numb_2}')

        numb_add = numb_1 + numb_2
        print(f'{numb_1} + {numb_2} = {numb_add}')

        numb_sub = numb_1 - numb_2
        print(f'{numb_1} - {numb_2} = {numb_sub}')

        numb_mul = numb_1 * numb_2
        print(f'{numb_1} * {numb_2} = {numb_mul}')

        numb_truediv = numb_1 / numb_2
        print(f'{numb_1} / {numb_2} = {numb_truediv}')

