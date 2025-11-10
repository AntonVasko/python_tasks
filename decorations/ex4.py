def check_password(min_length):
    def password(pw):
        if len(pw) >= min_length:
            return "ОК"
        return "Пароль слишком короткий!"
    return password
    
l1 = check_password(2)
print(l1('qwerty'))
print(l1('q'))