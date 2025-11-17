from random import randint

class dec():
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self):
        res = self.func()
        self.data[self.func.__name__] = [res]
        while res == None:
            res = self.func()
            self.data[self.func.__name__].append(res)

@dec
def ran():
    if randint(0, 1):
        return True

ran()
print(ran.data)