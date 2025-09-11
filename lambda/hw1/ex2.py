ls = [1, 2, 3, 4, 9, 10]
print('Before:', ls)
sort = list(filter(lambda x: x % 2 == 0, ls))
print('After:', sort)
