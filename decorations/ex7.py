def add_prefix(func):
    def addp(pref):
        return pref+'-'+func()
    return addp

@add_prefix
def addpref():
    return "qwerty"

print(addpref('abcd'))
print(addpref('hello'))
