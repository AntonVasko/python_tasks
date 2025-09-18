from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Task(BoxLayout):
    pass

class MainLayout(BoxLayout):
    def add_task(self, textlb):
        ly = BoxLayout(orientation='horizontal', size_hint_y=0.5)
        lb = Label(text=textlb.text)
        textlb.text = ''
        ly.add_widget(lb)
        btn = Button(text='Удалить')
        btn.bind(on_press=lambda x: self.remove_widget(ly))
        ly.add_widget(btn)
        self.add_widget(ly)

class plistApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    plistApp().run()