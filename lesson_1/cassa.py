class cassa():
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
        
        self.offers = {'Молоко': .03,
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
            print(i, '. ', product, ' - ', self.products[product]*(1-self.offers[product]), ' Руб.', sep='')
            if self.offers[product] > 0:
                print('СКИДКА:', str(self.offers[product]*100) + '%')
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

    def showPurchases(self):
        x = 16
        purchases = self.doPurchases()
        result = 0
        print(f"{'Наименование':{x}}{'Количество':{x}}{'Цена':{x}}{'Стоимость':{x}}")
        for i in range(1, len(purchases)+1):
            about_product = dict()
            product = list(purchases)[i-1]
            offer = self.offers[product]
            ammount = purchases[product][0]
            price = purchases[product][1]
            offered_price = price*(1 - offer)
            ammount_price = purchases[product][2]
            offered_ammount_price = ammount_price*(1 - offer)
            result += offered_ammount_price
            print(f"{product:<{x}}{ammount:<{x}}{offered_price:<{x}}{offered_ammount_price:<{x}}")
            if offer > 0:
                print('Скидка на товар -', str(offer*100) + '%')
                print(f"Цена без скидки: {price}", end='    ')
                print(f"Стоимость без скидки: {ammount_price}")
            print('ИТОГО:', str(result) + 'Руб.')
            about_product['Товар'] = product
            about_product['Цена'] = price
            about_product['Скидка'] = offer
            about_product['Цена со скидкой'] = offered_price
            about_product['Количество'] = ammount
            about_product['Сумма'] = offered_ammount_price
            about_product['Сумма без скидки'] = ammount_price
            self.check.append(about_product)

Cassa = cassa()
Cassa.showProducts()
Cassa.showPurchases()
print(Cassa.check)