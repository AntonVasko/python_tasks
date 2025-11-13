def create_cached_calculator():
    cache = {}

    def calculate(operation, a, b):
        key = f"{operation}_{a}_{b}"

        if key in cache:
            print(f"Используем кеш для {key}")
            return cache[key]
        
        print(f"Вычисляем {key}")
        if operation == "add":
            result = a + b
        elif operation == "multiply":
            result = a * b
        elif operation == "power":
            result = a ** b
        else:
            print("Неизвестная операция")
        
        cache[key] = result
        return result
    
    return calculate

calculator = create_cached_calculator()

print(calculator("add", 5, 3))
print(calculator("multiply", 4, 5))
print(calculator ("add", 5, 3))
print(calculator("power", 2, 8))
print(calculator("multiply", 4, 5))