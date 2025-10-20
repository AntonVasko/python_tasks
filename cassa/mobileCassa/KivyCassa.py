from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
import sqlite3
import json

try:
    conn = sqlite3.connect("cassa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = list(cursor.fetchall())
    for i in range(len(data)):
        data[i] = tuple(list(data[i])[1:])
except:
    with open('cassa.json') as f:
        file = json.load(f)
        data = []
        for el in file:
            pr = file[el]
            data.append((el, pr['Цена'], pr['Скидка'], pr['Цена со скидкой']))
add_to_cart = {}
print(data)

class Product(Button):
    pass

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.summ = 0
        self.ids.cost.text = f'[b]{str(self.summ)}[/b]'
        self.ly = self.ids.productsList
        for el in data:
            add_to_cart[el[0]] = 0
            btn = Product(text=f'{el[0]} | Было: [s]{el[1]}₽[/s] | Стало: [b]{el[3]}₽[/b]', size_hint_y = None, height = '50sp')
            btn.bind(on_press = self.inf_to_cart)
            self.ly.add_widget(btn)

    def inf_to_cart(self, obj):
        add_to_cart[obj.text.split()[0]] += 1
        self.summ = 0
        for el in add_to_cart:
            for i in range(add_to_cart[el]):
                for i in range(len(data)):
                    if data[i][0] == el:
                        self.summ += data[i][3]
                        break
        self.ids.cost.text = f'[b]{str(self.summ)}[/b]'

    def on_enter(self):
        self.summ = 0
        for el in add_to_cart:
            for i in range(add_to_cart[el]):
                for i in range(len(data)-1):
                    if data[i][0] == el:
                        self.summ += data[i][3]
                        break
        self.ids.cost.text = f'[b]{str(self.summ)}[/b]'

    def clear_cart(self):
        for el in add_to_cart:
            add_to_cart[el] = 0
        self.summ = 0
        for el in add_to_cart:
            for i in range(add_to_cart[el]):
                for i in range(len(data)-1):
                    if data[i][0] == el:
                        self.summ += data[i][3]
                        break
        self.ids.cost.text = f'[b]{str(self.summ)}[/b]'

class CartScreen(Screen):
    def on_enter(self):
        self.ly = self.ids.productsList
        self.ly.clear_widgets()
        for el in add_to_cart:
            for el1 in data:
                if el1[0] == el:
                    price = el1[3]
            if add_to_cart[el] != 0:
                btn = Product(text=f'{el}, [u]{add_to_cart[el]}[/u], [b]{price*add_to_cart[el]}[/b]', size_hint_y = None, height = '50sp')
                btn.bind(on_press = self.update)
                self.ly.add_widget(btn)
    
    def update(self, obj):
        add_to_cart[obj.text.split(',')[0]] -= 1
        self.on_enter()


    def buy(self):
        pass

class mainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CartScreen(name='cart'))
        return sm

if __name__ == '__main__':
    mainApp().run()