import resources
import sys
import os
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from cassa_ui import Ui_Ui_Dialog
import json

with open('cassa.json', encoding='utf-8') as f:
    data = json.load(f)

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Ui_Dialog()
ui.setupUi(window)
obj = ui.listView
purchases = ui.listView_2
canc = ui.pushButton_2
sum_label = ui.label
tobuy = ui.pushButton

class Cassa():
    def __init__(self, data, listView, listView2, canc, slabel, buybtn):
        self.data = data
        self.obj = listView
        self.purchases = listView2
        self.canc = canc
        self.slabel = slabel
        self.buybtn = buybtn

        self.check = str()
        self.purchases_text = dict()
        self.purchases_ammount = dict()
        self.summ = 0

        self.show_products()
        self.obj.itemClicked.connect(self.to_purchases)
        self.purchases.itemClicked.connect(self.dell)
        self.canc.clicked.connect(self.cancel)
        self.buybtn.clicked.connect(self.buy)

    def show_products(self):
        for el in self.data:
            text = el
            text += ' | Было: '
            text += str(data[el]['Цена'])
            text += '₽'
            text += ' | Стало: '
            text += str(data[el]['Цена со скидкой'])
            text += '₽'
            self.obj.addItem(text)

    def to_purchases(self):
        self.purchases.clear()
        text = self.obj.selectedItems()[0].text()
        name = text.split()[0]
        try:
            self.purchases_ammount[name] += 1
        except:
            self.purchases_ammount[name] = 1
        text = name
        text += ' '
        self.summ += self.data[name]['Цена со скидкой'] 
        text += str(self.data[name]['Цена со скидкой'])
        text += '₽ '
        text += str(self.purchases_ammount[name])
        text += ' '
        text += str(round(self.purchases_ammount[name] * self.data[name]['Цена со скидкой'], 2))
        text += '₽'
        for el in self.purchases_text:
            if name == el:
                self.purchases_text[name] = str()
        self.purchases_text[name] = text
        for el in self.purchases_text:
            if self.purchases_ammount[el] != 0:
                self.purchases.addItem(self.purchases_text[el])
        self.slabel.setText(str(round(self.summ, 2)))

    def dell(self):
        text = self.purchases.selectedItems()[0].text()
        self.purchases.clear()
        name = text.split()[0]
        self.purchases_ammount[name] -= 1
        text = name
        text += ' '
        self.summ -= self.data[name]['Цена со скидкой']
        text += str(self.data[name]['Цена со скидкой'])
        text += '₽ '
        text += str(self.purchases_ammount[name])
        text += ' '
        text += str(round(self.purchases_ammount[name] * self.data[name]['Цена со скидкой'], 2))
        text += '₽'
        for el in self.purchases_text:
            if name == el:
                self.purchases_text[name] = str()
        self.purchases_text[name] = text
        for el in self.purchases_text:
            if self.purchases_ammount[el] != 0:
                self.purchases.addItem(self.purchases_text[el])
        self.slabel.setText(str(round(self.summ, 2)))

    def cancel(self):
        self.purchases_ammount = dict()
        self.purchases_text = dict()
        self.slabel.setText(str())
        self.summ = 0
        self.purchases.clear()

    def buy(self):
        question = QMessageBox()
        question.setText('Печатать чек?')
        ye = question.addButton("Да", QMessageBox.ButtonRole.YesRole)
        question.addButton("Нет", QMessageBox.ButtonRole.NoRole)
        ye.clicked.connect(self.show_check)
        question.exec()
    
    def show_check(self):
        self.check = str()
        w = 15
        self.check += f"{'Наименование':{w}}{'Цена':{w}}{'Кол-во':{w}}{'Стоимость':{w}}\n"
        for el in self.purchases_text:
            text = self.purchases_text[el].split()
            name = text[0]
            price = text[1]
            ammount = text[2]
            sum = text[3]
            if ammount != '0':
                self.check += f"{name:{w}}{price:{w}}{ammount:{w}}{sum:{w}}\n"
        self.check += 'Итого: ' + str(self.summ) + '₽\n'
        self.cancel()
        self.check_toF()

    def check_toF(self):
        files = os.listdir('checks')
        name = 'checks/' + 'check' + str(len(files) + 1)
        with open(name, 'w', encoding='utf-8') as f:
            f.write(self.check)
            

cassa = Cassa(data, obj, purchases, canc, sum_label, tobuy)

window.show()
sys.exit(app.exec())