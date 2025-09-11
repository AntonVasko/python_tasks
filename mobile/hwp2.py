from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, StringProperty
from random import randint as rnd

class CustomInput(TextInput):
    mytext = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(text = self.change_mtext)

    def change_mtext(self, *args):
        self.mytext = self.text

class myLay(BoxLayout):
    check = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.num = rnd(10, 99)
        self.lb = Label(text='Введите число')
        self.inp = CustomInput()
        self.inp.bind(mytext = self.send)
        self.bind(check = self.win)
        self.add_widget(self.lb)
        self.add_widget(self.inp)

    def send(self, *args):
        if len(self.inp.mytext) == 2:
            self.usnum = int(self.inp.mytext)
            self.inp.text = ''
            if self.num > self.usnum:
                self.lb.text = 'Больше'
            elif self.num < self.usnum:
                self.lb.text = 'Меньше'
            else:
                self.check = True

    def win(self, *args):
        self.lb.text = "Поздравляем! Вы выиграли!"
        self.remove_widget(self.inp)

class CoolApp(App):
    def build(self):
        return myLay()
    
if __name__ == "__main__":
    CoolApp().run()