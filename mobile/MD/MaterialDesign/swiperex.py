from kivymd.material_resources import dp

from kivymd.app import MDApp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiper, MDSwiperItem


class MySwiper(MDSwiperItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widgets = [
            FitImage(
                source="bg.jpg",
                radius=[dp(20), ],
            )
        ]


class Main(MDApp):
    def on_start(self):
        swiper = self.root.get_ids().swiper
        swiper.height = (self.root.height - dp(40))
        swiper.y = (self.root.height - swiper.height - dp(20))

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDSwiper(
                    MySwiper(),
                    MySwiper(),
                    MySwiper(),
                    MySwiper(),
                    MySwiper(),
                    size_hint_y=None,
                    id="swiper",
                ),
                md_bg_color=self.theme_cls.backgroundColor,
            )
        )


Main().run()