from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import randint

class AnchorClicker(AnchorLayout):
    def __init__(self, **kwargs):
        super(AnchorClicker, self).__init__(**kwargs)
        self.randx = ['left', 'center', 'right'] 
        self.randy = ['top', 'center', 'bottom']
        self.shuffle()
        self.btn = Button(text = 'Нажми', size_hint = [0.3, 0.3])
        self.btn.on_press = self.shuffle
        self.add_widget(self.btn)
        
    def shuffle(self):
        self.anchor_x = self.randx[randint(0,2)]
        self.anchor_y = self.randy[randint(0,2)]
           
class ClickerApp(App):
    def build(self):
        bc = AnchorClicker()
        return bc

if __name__ == '__main__':    
    ClickerApp().run()