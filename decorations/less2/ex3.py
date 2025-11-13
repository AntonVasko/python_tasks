def decorator(func):
    def wrapper(*args):
        return func(*args) * 2
    return wrapper

@decorator
def say_hi(*args):
    if args[0] == "/":
        return args[1] / args[2]
    if args[0] == "*":
        return args[1] * args[2]
    if args[0] == "+":
        return args[1] + args[2]
    if args[0] == "-":
        return args[1] - args[2]
    if args[0] == "^":
        return args[1] ** args[2]

print(say_hi("/", 1, 2))