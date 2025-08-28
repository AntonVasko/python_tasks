from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from box import BoxClicker
from anchor import AnchorClicker
from gridl import BoxColours
from stack import InfStack

class comb(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(BoxClicker())
        self.add_widget(AnchorClicker())
        self.add_widget(BoxColours())
        self.add_widget(InfStack())

class CombApp(App):
    def build(self):
        layout = comb()
        return layout 
    
if __name__ == '__main__':
    CombApp().run()