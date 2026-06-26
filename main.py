import sys
import traceback

def exception_handler(exc_type, exc_value, exc_traceback):
    with open("crash_log.txt", "w") as f:
        traceback.print_exception(
            exc_type,
            exc_value,
            exc_traceback,
            file=f
        )

sys.excepthook = exception_handler



#Importing Modules----------------------------------------------------------------------------------------------

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.uix.scatter import Scatter
from login import LoginScreen
from home import HomeSreen
from jee_questions import JEEScreen
from neet_questions import NEETScreen
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivy.uix.togglebutton import ToggleButton
from store import StoreScreen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from Games.Game_Screen import GameScreen
from Games.Shooting_games.loading_screen import ShootingGameLoadingScreen
from Games.Shooting_games.home_screen import ShootingGameHomeScreen
from Games.Shooting_games.level_screen import ShootingGameLevelScreen
from Games.Shooting_games.main_game_screen import ShootingGameMainGameScreen
from Games.Shooting_games.effects import break_block
#Creating Logo Screen---------------------------------------------------------------------------------------------------

class LogoScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.logo = Image(source = "Images/Path_Logo.jpg" ,opacity = 0 , size_hint = (0.3,0.3), pos_hint = {"center_x":0.5 , "center_y":0.6})


        self.text = Label(text = "WELCOME TO THE PATH OF YOUR JOURNEY" ,opacity=0, font_size = 15, pos_hint = {"center_x":0.5 , "center_y":0.2})
        layout.add_widget(self.logo)
        layout.add_widget(self.text)
        self.add_widget(layout)

    def on_enter(self):
        animation = Animation(opacity = 1 , duration = 3)
        animation.start(self.logo)
        Clock.schedule_once(self.show_welcome, 3)

    def show_welcome(self,dt):
        welcome_animation = Animation(opacity=1,duration=2)
        welcome_animation.start(self.text)

        Clock.schedule_once(self.zoom_logo,2)

    def zoom_logo(self,dt):

        zoom = Animation(size_hint = (3,3),
                         opacity = 0,
                         duration=3)
        zoom.start(self.logo)
        Clock.schedule_once(self.go_loading , 2.5)

        fade_text = Animation(
            opacity = 0 , duration = 1
        )
        fade_text.start(self.text)

    def go_loading(self,dt):
        self.manager.current = "loading"


#Creating Loading Screen------------------------------------------------------------------------------------------------

class LoadingScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.progress = 0

        layout = FloatLayout()


        image = Image(source = "Images/Path_loading.jpg" , allow_stretch = True , keep_ratio = False)
        layout.add_widget(image)

        text = Label(text = "Loading Game....." , font_size = 13 , pos_hint = {"center_x": 0.5 , "center_y":0.20})
        layout.add_widget(text)


        self.bar = ProgressBar(
            max = 100 ,
            value = 0 ,
            size_hint = (0.8 , 0.05),
            pos_hint = {"center_x":0.5 , "center_y":0.15}
        )

        self.percent = Label(
            text = "0%",
            font_size = 13,
            pos_hint={
                "center_x":0.5 , "center_y":0.08
            }
        )
        layout.add_widget(self.percent)
        layout.add_widget(self.bar)
        self.add_widget(layout)

    def on_enter(self):
        Clock.schedule_interval(
            self.fill_bar ,
            0.05
        )

    def fill_bar(self ,dt):
        if self.progress < 100:
            self.progress += 1.5
            self.bar.value = self.progress

            self.percent.text = str(int(self.progress)) + "%"
        else:
            Clock.unschedule(self.fill_bar)
            Clock.schedule_once(self.open_wel, 2)

    def open_wel(self, dt):
        self.manager.current = "welcome"


#Creating Welcome Screen------------------------------------------------------------------------------------------------

class WelcomeScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        self.image = Image(source = "Images/hanuman.jpg" , opacity = 0 ,size_hint = (0.6,0.6), pos_hint = {"center_x":0.5 , "center_y":0.6} )
        layout.add_widget(self.image)
        self_image_bg = Image(source = "Images/Path_loading2.jpg" , opacity = 0.2 , allow_stretch = True , keep_ratio = False)
        layout.add_widget(self_image_bg)
        self.text = Label(text = "You Are Very Welcomed To The Game , We hope You will Enjoy playing and learning throughout the Journey" , font_size = 15 ,pos_hint = {"center_x": 0.5 , "center_y":0.20} )
        layout.add_widget(self.text)
        self.add_widget(layout)

    def on_enter(self):
        animation = Animation(opacity=1, duration=3)
        animation.start(self.image)
        Clock.schedule_once(self.show_text, 3)

    def show_text(self, dt):
        welcome_animation = Animation(opacity=1, duration=2)
        welcome_animation.start(self.text)

        Clock.schedule_once(self.zoom_out_logo_hanu, 2)


    def zoom_out_logo_hanu(self, dt):
        zoom = Animation(size_hint=(0, 0),
                             opacity=0,
                             duration=3)
        zoom.start(self.image)
        Clock.schedule_once(self.go_loading, 2.5)

        fade_text = Animation(
                opacity=0, duration=3, font_size = 0,
            )
        fade_text.start(self.text)

    def go_loading(self, dt):
        self.manager.current = "login"






#Main App---------------------------------------------------------------------------------------------------------------
class MyApp(App):
    def build(self):

        sm = ScreenManager(transition = FadeTransition(duration =0.5 ))

        sm.add_widget(LogoScreen(name = "logo"))
        sm.add_widget(LoadingScreen(name="loading"))
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeSreen(name="home"))
        sm.add_widget(JEEScreen(name = "jee"))
        sm.add_widget(NEETScreen(name = "neet"))
        sm.add_widget(StoreScreen(name = "store"))
        sm.add_widget(GameScreen(name = "games"))
        sm.add_widget(ShootingGameLoadingScreen(name = "loading_screen"))
        sm.add_widget(ShootingGameHomeScreen(name = "home_screen"))
        sm.add_widget(ShootingGameLevelScreen(name = "level_screen"))
        sm.add_widget(ShootingGameMainGameScreen(name = "main_game_screen"))

        return sm


MyApp().run()

