products = {'Молоко': 75,
            'Хлеб': 50,
            'Вода': 30,
            'Колбаса': 100,
            'Курица': 500,
            'Сыр': 120,
            'Носки': 100,
            'Сок': 130,
            'Сухарики': 50}

def showProducts(products):
    for i in range(1, len(products)+1):
        product = list(products)[i-1]
        print(i, '. ', product, ' - ', products[product], ' Руб.', sep='')
    print()

def purchases(products):
    purchaseDict = dict()
    input_text = 'Введите номер продукта, который вы хотите купить.\nВведите "0" если хотите закончить покупки\n'
    purchase = int(input(input_text)) - 1
    while purchase != -1:
        product = list(products)[purchase]
        try:
            purchaseDict[product][0] += 1
            purchaseDict[product][2] += products[product]
        except:
            purchaseDict[product] = [1, products[product], products[product]]
        purchase = int(input(input_text)) - 1
    print('\n')
    return purchaseDict

def showPurchases(purchases):
    x = 16
    print(f"{'Наименование':{x}}{'Количество':{x}}{'Цена':{x}}{'Стоимость':{x}}")
    for i in range(1, len(purchases)+1):
        product = list(purchases)[i-1]
        ammount = purchases[product][0]
        price = purchases[product][1]
        ammount_price = purchases[product][2]
        print(f"{product:<{x}}{ammount:<{x}}{price:<{x}}{ammount_price:<{x}}")

showProducts(products)
showPurchases(purchases(products))
