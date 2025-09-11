from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class CustomBtn(Button):
    pressed = NumericProperty(0)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.text = 'Нажми'
        self.size_hint_y = None
        self.bind(on_press = lambda x: x.height + 10)
        self.bind(height = print(self.height))

class VeryCoolLt(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
        self.btn = CustomBtn()
        self.btn.bind(pressed = self.func)
        self.add_widget(self.btn)

    def func(self, *args):
        if self.btn.pressed == 2:
            self.btn.size_hint = [0.5, 0.5]
            self.lb = Label(text='Привет!')
            self.add_widget(self.lb)
        elif self.btn.pressed == 5:
            self.btn.pressed = 0
            self.btn.size_hint = [1, 1]
            self.remove_widget(self.lb)

class VeryCoolApp(App):
    def build(self):
        return VeryCoolLt()
    
if __name__ == '__main__':
    VeryCoolApp().run()