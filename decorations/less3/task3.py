from random import randint

class Dec():
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.data = {}

    def __call__(self, func):
        def new_func():
            if input("Введите логин: ") == self.login and input("Введите пароль: ") == self.password:
                res = func()
                print(res)
                self.data[func.__name__] = res
                return
            print("Неверный логин или пароль!")
        return new_func

@Decec(login="Oleg", password="qwerty1")
def ran():
    return randint(0, 100)

ran()