import time
import requests

def benchmark(func):
    def wrapper(*args, **kwargs):
        for el in args:
            if not func(el, *args):
                return "Есть отрицательное число"
        return "Все числа положительные"
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@benchmark
def check(num, *args):
    """Проверяет, является ли объект положительным числом"""
    if isinstance(num, int) or isinstance(num, float):
        if num > 0:
            return True
        return False
    return True

webpage = check(1, 2, 3, -1, 4, 5)
print(check.__name__)
print(check.__doc__)