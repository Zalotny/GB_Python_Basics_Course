from functools import wraps


def type_logger(func):
    @wraps(func)
    def logger_args(*args, **kwargs):
        result = func(*args, **kwargs)
        args_list = []
        for arg in args:
            args_list.append(f'{arg}: {type(arg)}')
        for kwarg in kwargs:
            args_list.append(f'{kwarg}={kwargs[kwarg]}: {type(kwargs[kwarg])}')
        print(f'{func.__name__}({", ".join(args_list)})')
        return result
    return logger_args


@type_logger
def calc_cube(x, y, z, arg1=0, arg2=''):
    return x ** 3


a = calc_cube(5, 'asd', [12, 22, 'wer'], arg1='po', arg2=33)
# $ a = calc_cube(5)
# 5: <class 'int'>
