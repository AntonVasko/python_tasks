def funcs_lim(lim):
    def f():
        nonlocal lim
        lim -= 1
        if lim >= 0:
            return f"Вы можете вызвать эту функцию ещё {lim} раз."
        return
    return f

f = funcs_lim(3)

for i in range(4):
    print(f())