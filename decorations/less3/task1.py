from random import randint

class dec():
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self):
        self.data[self.func.__name__] = self.func()

@dec
def ran():
    return randint(0, 100)

ran()
print(ran.data)