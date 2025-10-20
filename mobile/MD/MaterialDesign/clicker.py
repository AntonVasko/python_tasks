from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.modules import inspector

clicks = 0

class ClickerScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global clicks
        self.ids.click.on_press = self.add_click
        self.ids.bar.bind(on_switch_tabs = self.changesc)
    def add_click(self):
        global clicks
        clicks += 1
        self.ids.clicks.text = str(clicks) + " нажатий."
    def on_enter(self):
        global clicks
        self.ids.clicks.text = str(clicks) + " нажатий."
    def changesc(self, *args):
        self.manager.current = 'shop'

class ShopScreen(MDScreen):
    pass

class clickerApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(ClickerScreen(name='app'))
        sm.add_widget(ShopScreen(name='shop'))
        inspector.create_inspector(Window, sm)
        return sm
        
    
clickerApp().run()