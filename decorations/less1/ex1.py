def counter():
    count = 0
    def add_count():
        nonlocal count
        count += 1
        return count
    return add_count

counter1 = counter()
counter2 = counter()

counter1()
print(counter1())
print(counter2())