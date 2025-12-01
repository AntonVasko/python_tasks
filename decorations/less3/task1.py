from random import randint

class dec():
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self):
        if not self.func.__name__ in self.data:
            self.data[self.func.__name__] = list()
        self.data[self.func.__name__].append(self.func())

@dec
def ran():
    return randint(0, 100)

ran()
ran()
print(ran.data)