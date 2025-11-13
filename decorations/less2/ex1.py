import time
import requests

def benchmark(func):
    def wrapper(*args, **kwargs):
        for el in args:
            if not func(el, *args):
                return "Есть отрицательное число"
        return "Все числа положительные"
    return wrapper

@benchmark
def check(num, *args):
    if isinstance(num, int) or isinstance(num, float):
        if num > 0:
            return True
        return False
    return False 

webpage = check(1, 2, 3, 4, 5)
print(webpage)