from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout

class MainScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ml = MDBoxLayout(orientation = 'horizontal')
        self.ml.add_widget(MDButton(MDButtonText(text='Hello, World'), pos_hint = {"center_x":0.5, "center_y":0.5}))
        self.ml.add_widget(MDButton(MDButtonText(text='World, Hello'), pos_hint = {"center_x":0.5, "center_y":0.5}))
        self.add_widget(self.ml)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        return MainScreen()
    
if __name__ == '__main__':
    MainApp().run()