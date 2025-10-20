from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Button"
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)
    
if __name__ == "__main__":
    Example().run()