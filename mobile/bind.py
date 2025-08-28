from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from functools import partial


class DemoBox(BoxLayout):
    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"

        btn = Button(text="Normal binding to event")
        btn.bind(on_press=self.on_event)
        #btn.on_press = self.on_event
        
        btn2 = Button(text="Normal binding to a property change")
        btn2.bind(state=self.on_property)

        btn3 = Button(text="Using anonymous functions")
        btn3.bind(on_press=lambda x: self.on_event(None))

        btn4 = Button(text="Use a flexible function")
        btn4.bind(on_press=self.on_anything)

        btn5 = Button(text="Using partial functions. For hardcores.")
        btn5.bind(on_press=partial(self.on_anything, "1", "2", monthly="Python"))
        for but in [btn, btn2, btn3, btn4, btn5]:
            self.add_widget(but)
    
    def on_event(self, obj):
        print("Typical event from", obj)

    def on_property(self, obj, value):
        print("Typical propeerty chang from", obj, "to", value)

    def on_anything(self, *args, **kwargs):
        print('the flexible function has *args of', str(args), 'and **kwargs of', str(kwargs))

class DemoApp(App):
    def build(self):
        return DemoBox()
    
if __name__ == "__main__":
    DemoApp().run()