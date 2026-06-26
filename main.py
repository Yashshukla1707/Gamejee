from kivy.config import Config

Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'resizable', '1')

import os

os.environ["KIVY_GL_BACKEND"] = "sdl2"
os.environ["KIVY_WINDOW"] = "sdl2"


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.clock import Clock



class LogoScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        self.logo = Image(
            source="Images/Path_Logo.jpg",
            opacity=0,
            size_hint=(0.3,0.3),
            pos_hint={"center_x":0.5,"center_y":0.6}
        )

        self.text = Label(
            text="WELCOME TO THE PATH OF YOUR JOURNEY",
            opacity=0,
            font_size=15,
            pos_hint={"center_x":0.5,"center_y":0.2}
        )


        layout.add_widget(self.logo)
        layout.add_widget(self.text)

        self.add_widget(layout)



    def on_enter(self):

        Animation(
            opacity=1,
            duration=3
        ).start(self.logo)

        Clock.schedule_once(self.show_text,3)



    def show_text(self,dt):

        Animation(
            opacity=1,
            duration=2
        ).start(self.text)

        Clock.schedule_once(self.zoom_logo,2)



    def zoom_logo(self,dt):

        Animation(
            size_hint=(3,3),
            opacity=0,
            duration=3
        ).start(self.logo)

        Animation(
            opacity=0,
            duration=1
        ).start(self.text)


        Clock.schedule_once(self.go_loading,2.5)



    def go_loading(self,dt):

        self.manager.current="loading"







class LoadingScreen(Screen):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)

        self.progress=0

        layout=FloatLayout()


        image=Image(
            source="Images/Path_loading.jpg",
            allow_stretch=True,
            keep_ratio=False
        )

        layout.add_widget(image)



        self.percent=Label(
            text="0%",
            font_size=13,
            pos_hint={"center_x":0.5,"center_y":0.08}
        )


        self.bar=ProgressBar(
            max=100,
            value=0,
            size_hint=(0.8,0.05),
            pos_hint={"center_x":0.5,"center_y":0.15}
        )


        layout.add_widget(self.percent)
        layout.add_widget(self.bar)

        self.add_widget(layout)



    def on_enter(self):

        Clock.schedule_interval(
            self.fill_bar,
            0.05
        )



    def fill_bar(self,dt):

        if self.progress < 100:

            self.progress += 1.5

            self.bar.value=self.progress

            self.percent.text=str(int(self.progress))+"%"


        else:

            Clock.unschedule(self.fill_bar)

            Clock.schedule_once(
                self.open_welcome,
                2
            )



    def open_welcome(self,dt):

        self.manager.current="welcome"








class WelcomeScreen(Screen):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)

        layout=FloatLayout()


        self.bg=Image(
            source="Images/Path_loading2.jpg",
            allow_stretch=True,
            keep_ratio=False
        )


        self.image=Image(
            source="Images/hanuman.jpg",
            opacity=0,
            size_hint=(0.6,0.6),
            pos_hint={"center_x":0.5,"center_y":0.6}
        )


        self.text=Label(
            text="You Are Very Welcomed To The Game",
            opacity=0,
            font_size=15,
            pos_hint={"center_x":0.5,"center_y":0.20}
        )


        layout.add_widget(self.bg)
        layout.add_widget(self.image)
        layout.add_widget(self.text)

        self.add_widget(layout)



    def on_enter(self):

        Animation(
            opacity=1,
            duration=3
        ).start(self.image)


        Clock.schedule_once(
            self.show_text,
            3
        )



    def show_text(self,dt):

        Animation(
            opacity=1,
            duration=2
        ).start(self.text)








class MyApp(App):

    def build(self):

        sm=ScreenManager(
            transition=FadeTransition(duration=0.5)
        )


        sm.add_widget(
            LogoScreen(name="logo")
        )

        sm.add_widget(
            LoadingScreen(name="loading")
        )

        sm.add_widget(
            WelcomeScreen(name="welcome")
        )


        return sm





MyApp().run()
