from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyRootwidget(BoxLayout):
    def _init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def press_callback(self, instance):
        print(f"Кнопка {instance.text} была нажата!")
        self.ids.my_label.text = "Текст изменен!"

class designApp(App):
    def build(self):
        return MyRootwidget()
    
if __name__ == '__main__':
    designApp().run()