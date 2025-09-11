def fibb(x):
    if x <= 1:
        return x
    return fibb(x-1) + fibb(x-2)
 

def sum_num(snum, ans=0):
    x = len(snum)-1
    if x == -1:
        return ans
    ans += int(snum[x])
    return sum_num(snum[:-1], ans)

def reverse(s, ans=''):
    x = len(s)-1
    if x == -1:
        return ans
    ans += s[x]
    return reverse(s[:-1], ans)

def is_pal(s):
    x = len(s) - 1
    if x <= 0:
        return True
    if s[0] == s[x]:
        return is_pal(s[1:-1])
    return False

def sum_list(slist, ans=0):
    x = len(slist)-1
    if x == -1:
        return ans
    ans += slist[x]
    return sum_num(slist[:-1], ans)

print(fibb(int(input('Введите порядковый номер числа фиббоначи, начиная с 0 включительно: '))))
print(sum_num(input('Введите число, сумму которого хотите узнать: ')))
print(reverse(input('Введите текст, который хотите развернуть: ')))
print(is_pal(input('Введите текст, про который вы хотите узнать - палиндром он или нет: ')))
print(sum_list(list(map(int, input('Введите ряд чисел через пробел, сумму которых вы хотите узнать: ').split()))))