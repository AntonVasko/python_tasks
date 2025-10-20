from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = Window.width//2, Window.height//2

class TestApp(App):
    def build(self):
        return MyWidget()
    
if __name__ == '__main__':
    TestApp().run()