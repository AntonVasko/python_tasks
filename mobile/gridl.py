from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import randint

def random_color():
    return (randint(0,100)/100, randint(0,100)/100, randint(0,100)/100, 1)

class BoxColours(GridLayout):
    def __init__(self, **kwargs):
        super(BoxColours, self).__init__(**kwargs)
        self.cols = 3
        for i in range(9):
            self.btn = Button(text = 'Нажми!', background_color = random_color())
            self.btn.bind(on_press = lambda x: self.random_color(x))
            self.add_widget(self.btn)

    def random_color(self, obj):
        obj.background_color = (randint(0,100)/100, randint(0,100)/100, randint(0,100)/100, 1)
        
class ColoursApp(App):
    def build(self):
        bc = BoxColours()
        return bc
    
if __name__ == '__main__':    
    ColoursApp().run()