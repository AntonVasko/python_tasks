from time import sleep

def funcs_lim(func):
    def f(lim):
        func()
        print(f"Вы можете вызвать эту функцию ещё раз через {lim} секунд.")
        sleep(lim)
        return
    return f

@funcs_lim
def say_hi():
    print("Hello!")

say_hi(1)
say_hi(3)
say_hi(2)
say_hi(4)