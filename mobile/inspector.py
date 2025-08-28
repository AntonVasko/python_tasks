from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.modules import inspector

class DemoApp(App):
    def build(self):
        button = Button(text = "Test")
        inspector.create_inspector(Window, button)
        return button
    
if __name__ == '__main__':
    DemoApp().run()