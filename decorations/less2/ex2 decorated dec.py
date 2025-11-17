def decorator(greet):
    def wrapper(func):
        def wrapped_wrapper(*args):
            print(greet)
            print(func(*args)) 
        return wrapped_wrapper
    return wrapper

@decorator(greet="Hello")
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
    
say_hi("/", 1, 2)