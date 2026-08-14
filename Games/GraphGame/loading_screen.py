from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.image import Image

class GraphGameLoadingScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(
            source="Images/GraphGameLoadingScreenLogo.jpg", opacity=0.5, allow_stretch=True, keep_ratio=False
        )
        layout.add_widget(bg)


        label = Label(
            text = "Loading Graph Game....",
            font_size=12, pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        layout.add_widget(label)

        self.bar = ProgressBar(
            max =100 ,
            value = 0,
            size_hint=(0.8, 0.05),
            pos_hint={"center_x": 0.5, "center_y": 0.15}
        )
        layout.add_widget(self.bar)

        self.percent = Label(
            text = "0%",
            font_size = 13,
            pos_hint = {"center_x":0.5 , "center_y": 0.08}
        )
        layout.add_widget(self.percent)
        self.add_widget(layout)

        self.progress = 0

    def on_enter(self):
        Clock.schedule_interval(
            self.fill_bar , 0.05
        )

    def fill_bar(self , dt):
        if self.bar.value < 100:
            self.progress += 1.5
            self.bar.value = self.progress
            self.percent.text = str(int(self.progress)) + "%"


        else:
            Clock.unschedule(self.fill_bar )
            Clock.schedule_once(self.go_home ,2)

    def go_home(self , instance):
        self.manager.current = "graph_game_home_screen"







