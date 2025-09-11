'''mydict = {'слива':5,
          'папая':6,
          'лук':56,
          'маракуя':67,
          'ежевика':45}

print('Before sort:', mydict)
sorted_mydict = dict(sorted(mydict.items(), key=lambda item: len(item[0]))) 
print('After:', sorted_mydict)'''

"""a = 0
b = lambda a: a + 10, a-5
print(b[0](0))"""
"""
def my_function(n):
    return lambda a: a*n
print(my_function(2)(15))"""
"""
st = "язжцутеьячштйнфчбхфи"
vowels = "уеыаоэяиюё"
result = list(map(lambda x: 'Гласная' if x in vowels else 'Согласная', st))
print(result)"""
"""
def get_min_or_max(value = "max"):
    return eval(f'lambda x: {value}(x)')

ls = [1, 7, 9, 0 , -1, -8, 3, -11, 6]

max_func = get_min_or_max()
min_func = get_min_or_max('min')
print(max_func(ls))
print(min_func(ls))"""
