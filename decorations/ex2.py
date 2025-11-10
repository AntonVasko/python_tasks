def id_generator(pf):
    id = -1
    def postfix():
        nonlocal id
        id+=1
        return pf + '-' + str(id)
    return postfix

gen1 = id_generator('oleg')
print(gen1())
print(gen1())