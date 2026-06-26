from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

class ShootingGameLoadingScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(
            source = "Images/ShootingGameLogo7.jpg" , opacity = 0.5 , allow_stretch = True , keep_ratio = False
        )
        layout.add_widget(bg)
        self.bar_progress = 0

        loading = Label(
            text = "Loading Shooting Game...." , font_size = 12 , pos_hint = {"center_x" : 0.5 , "center_y":0.2}
        )
        layout.add_widget(loading)

        self.shooting_game_bar_percent = Label(
            text = "0%",
            font_size = 13,
            pos_hint = {"center_x":0.5 , "center_y": 0.08}
        )


        self.shooting_game_bar = ProgressBar(
            max =100,
            value = 0 ,
            size_hint=(0.8, 0.05),
            pos_hint={"center_x": 0.5, "center_y": 0.15}
        )




        layout.add_widget(self.shooting_game_bar_percent)
        layout.add_widget(self.shooting_game_bar)

        self.add_widget(layout)

    def on_enter(self):
        Clock.schedule_interval(
            self.fill_shooting_game_bar, 0.05
        )

    def fill_shooting_game_bar(self, dt):
        if self.bar_progress < 100:
            self.bar_progress += 1.5
            self.shooting_game_bar.value = self.bar_progress

            self.shooting_game_bar_percent.text = str(int(self.bar_progress)) + "%"

        else:
            Clock.unschedule(self.fill_shooting_game_bar)
            Clock.schedule_once(self.home, 2)

    def home(self, dt):
        self.manager.current = "home_screen"
