from functools import wraps


def check_arg(arg):
    return bool(isinstance(arg, int) and arg > 0)


def val_checker(check_func):
    def val_checker_in(func):
        @wraps(func)
        def valide_wrap(arg):
            if check_func(arg):
                return func(arg)
            else:
                raise ValueError(f'wrong val {arg}')
        return valide_wrap
    return val_checker_in


@val_checker(check_arg)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
