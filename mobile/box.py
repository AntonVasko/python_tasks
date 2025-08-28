from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BoxClicker(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxClicker, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.counter = 0
        self.lb = Label(text = str(self.counter))
        self.btn = Button(text = 'Нажми')
        self.btn.bind(on_press = self.on_event)
        self.add_widget(self.lb)
        self.add_widget(self.btn)
        
    def on_event(self, obj):
        self.counter += 1
        self.lb.text = str(self.counter)
        
class ClickerApp(App):
    def build(self):
        bc = BoxClicker()
        return bc
    
#if __name__ == '__main__':    
#    ClickerApp().run()