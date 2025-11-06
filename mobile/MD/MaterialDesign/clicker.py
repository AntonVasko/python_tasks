from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.modules import inspector

clicks = 0
mpc = 1

class ClickerScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global clicks
        self.ids.click.on_press = self.add_click
        self.ids.bar.bind(on_switch_tabs = self.changesc)
    def on_enter(self):
        self.ids.bar.set_active_item(self.ids.toapp)
    def add_click(self):
        global clicks, mpc
        clicks += mpc
        self.ids.clicks.text = str(clicks) + " нажатий."
    def on_enter(self):
        global clicks
        self.ids.clicks.text = str(clicks) + " нажатий."
    def changesc(self, *args):
        if self.ids.toshop.active:
            self.manager.transition.direction = 'left'
            self.manager.current = 'shop'

class ShopScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.first_upgrade.on_press = self.fupgrade
        self.ids.second_upgrade.on_press = self.supgrade
        self.ids.third_upgrade.on_press = self.tupgrade
        self.ids.navi.bind(on_switch_tabs = self.changesc)
    def on_enter(self):
        self.ids.navi.set_active_item(self.ids.toshop)
    def upgrade(self, a, b):
        global clicks, mpc
        if clicks >= a:
            clicks -= a
            mpc += b
    def fupgrade(self):
        self.upgrade(20, 1)
    def supgrade(self):
        self.upgrade(100, 1)
    def tupgrade(self):
        self.upgrade(500, 1)
    def changesc(self, *args):
        if self.ids.toapp.active:
            self.manager.transition.direction = 'right'
            self.manager.current = 'app'

class clickerApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(ClickerScreen(name='app'))
        sm.add_widget(ShopScreen(name='shop', ))
        inspector.create_inspector(Window, sm)
        return sm
        
    
clickerApp().run()