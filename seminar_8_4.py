from functools import wraps


def val_checker(arg1):
    def logger(func):

        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            if arg1(*args):
                return result
            else:
                raise ValueError(f'Wrong val{args}')
        return wrapper
    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(6))