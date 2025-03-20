class Cassa():
    def __init__(self):
        self.products = {'Молоко': 75,
                    'Хлеб': 50,
                    'Вода': 30,
                    'Колбаса': 100,
                    'Курица': 500,
                    'Сыр': 120,
                    'Носки': 100,
                    'Сок': 130,
                    'Сухарики': 50}
        
        self.discount = {'Молоко': .03,
                    'Хлеб': .1,
                    'Вода': .2,
                    'Колбаса': .05,
                    'Курица': .25,
                    'Сыр': .05,
                    'Носки': .99,
                    'Сок': .02,
                    'Сухарики': 0.0}
        
        self.check = list()

    def showProducts(self):
        for i in range(1, len(self.products)+1):
            product = list(self.products)[i-1]
            print(i, '. ', product, ' - ', round(self.products[product]*(1-self.discount[product]), 2), ' Руб.', sep='')
            if self.discount[product] > 0:
                print('СКИДКА:', str(self.discount[product]*100) + '%')
                print('Цена без скидки -', self.products[product])
        print()

    def doPurchases(self):
        purchaseDict = dict()
        input_text = 'Введите номер продукта, который вы хотите купить.\nВведите "0" если хотите закончить покупки\n'
        purchase = int(input(input_text)) - 1
        while purchase != -1:
            product = list(self.products)[purchase]
            try:
                purchaseDict[product][0] += 1
                purchaseDict[product][2] += self.products[product]
            except:
                purchaseDict[product] = [1, self.products[product], self.products[product]]
            purchase = int(input(input_text)) - 1
        print()
        return purchaseDict

    def doCheck(self):
        purchases = self.doPurchases()
        result = 0
        for i in range(1, len(purchases)+1):
            about_product = dict()
            product = list(purchases)[i-1]
            discount = self.discount[product]
            ammount = purchases[product][0]
            price = float(purchases[product][1])
            offered_price = round(price*(1 - discount), 2)
            ammount_price = float(purchases[product][2])
            offered_ammount_price = round(ammount_price*(1 - discount), 2)
            result += offered_ammount_price
            about_product['Товар'] = product
            about_product['Цена'] = price
            about_product['Скидка'] = discount
            about_product['Цена со скидкой'] = offered_price
            about_product['Количество'] = ammount
            about_product['Сумма'] = offered_ammount_price
            about_product['Сумма без скидки'] = ammount_price
            self.check.append(about_product)
    
    def showPurchases(self):
        x = 16
        result = 0
        print(f"{'Наименование':{x}}{'Количество':{x}}{'Цена-Руб.':{x}}{'Стоимость-Руб.ыыы':{x}}")
        for i in range(len(self.check)):
            purchases = self.check[i]
            result += purchases['Цена со скидкой']
            print(f"{purchases['Товар']:<{x}}{purchases['Количество']:<{x}}{purchases['Цена со скидкой']:<{x}}{purchases['Сумма']:<{x}}")
            if purchases['Скидка'] > 0:
                print('Скидка на товар -', str(purchases['Скидка']*100) + '%')
                print(f"Цена без скидки: {purchases['Цена']}", end='    ')
                print(f"Стоимость без скидки: {purchases['Сумма без скидки']}")
        print('ИТОГО:', str(result) + '-Руб.')
cassa = Cassa()
cassa.showProducts()
cassa.doCheck()
cassa.showPurchases()
print(cassa.check)