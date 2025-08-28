from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import randint

class InfStack(StackLayout):
    def __init__(self, **kwargs):
        super(InfStack, self).__init__(**kwargs)
        self.ammount_objects = 1
        self.ammount_colums = 1
        self.sizexy = 1
        self.words = ['apple', 'table', 'car', 'cat', 'house', 'floor', 'wash', 'fish', 'deep', 'whale', 'bird', 'flower', 'witch', 'summer', 'force', 'speed']
        self.btn = Button(text = 'Нажми', size_hint = [self.sizexy, self.sizexy])
        self.objects = [self.btn]
        self.btn.on_press = self.add
        self.add_widget(self.btn)
            
    def add(self):
        self.ammount_objects += 1
        if self.ammount_objects > self.ammount_colums*self.ammount_colums:
            self.ammount_colums += 1
            self.sizexy = 1/self.ammount_colums
            self.refresh()
        self.lb = Label(text = self.words[randint(0, len(self.words)-1)], size_hint = [self.sizexy, self.sizexy])
        self.objects.append(self.lb)
        self.add_widget(self.lb)
    
    def refresh(self):
        for el in self.objects:
            el.size_hint = [self.sizexy, self.sizexy]
    
class ClickerApp(App):
    def build(self):
        bc = InfStack()
        return bc

if __name__ == '__main__':
    ClickerApp().run()