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
print(data)

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ly = self.ids.productsList
        self.add_to_cart = {}
        for el in data:
            btn = Button(text=f'{el[0]} | Было: {el[1]}₽ | Стало: {el[3]}₽')
            btn.on_press = self.inf_to_cart
            self.ly.add_widget(btn)

    def inf_to_cart(self):
        print('dasasada')

    def clear_cart(self):
        pass

class CartScreen(Screen):
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