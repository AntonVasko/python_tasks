from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class ClickerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ClickerBox, self).__init__(**kwargs)
        self.count = 0
        self.orientation = "vertical"
        self.btn = Button(text='Нажми!')
        self.btn.bind(on_press=self.on_event)
        self.counter = Label(text=str(self.count))
        self.add_widget(self.counter)
        self.add_widget(self.btn)
    
    def on_event(self, obj):
        self.count += 1
        self.counter.text = str(self.count)

class ClickerApp(App):
    def build(self):
        layout = ClickerBox()
        return layout 
    
if __name__ == "__main__":
    ClickerApp().run()