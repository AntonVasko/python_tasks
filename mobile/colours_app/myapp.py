from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle

class Colours(BoxLayout):
    def __init__(self):
        super().__init__()
        self.rgbcolours = [0, 0, 0, 1]

    def txt1(self, obj):
        self.rgbcolours[0] = obj.value
        with self.canvas.before:
            Color(self.rgbcolours[0], self.rgbcolours[1], self.rgbcolours[2], self.rgbcolours[3])
            self.rect = Rectangle(size = self.size)

    def txt2(self, obj):
        self.rgbcolours[1] = obj.value
        with self.canvas.before:
            Color(self.rgbcolours[0], self.rgbcolours[1], self.rgbcolours[2], self.rgbcolours[3])
            self.rect = Rectangle(size = self.size)
    
    def txt3(self, obj):
        self.rgbcolours[2] = obj.value
        with self.canvas.before:
            Color(self.rgbcolours[0], self.rgbcolours[1], self.rgbcolours[2], self.rgbcolours[3])
            self.rect = Rectangle(size = self.size)
    
class gesignApp(App):
    def build(self):
        return Colours()
    
gesignApp().run()