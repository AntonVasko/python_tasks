def decorator(func):
    def wrapper(*args):
        print(args[0])
        func(*args)
    return wrapper

@decorator
def say_hi(arg):
    print("2 * 8 = 16")

say_hi("hello")