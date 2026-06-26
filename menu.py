from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from hover_button import HoverButtonYellow , HoverButtonRed
from kivy.uix.floatlayout import FloatLayout



class BottomMenu(BoxLayout):
    def __init__(self, screen_manager ,  **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        self.orientation = "horizontal"

        layout = FloatLayout()

        home_btn = HoverButtonRed(text="Home" , size_hint = (0.2,0.08) , pos_hint ={"center_x":0.5 , "center_y":0.04} )
        store_btn = HoverButtonRed(text="Store" , size_hint = (0.2,0.08) , pos_hint = {"center_x":0.5 , "center_y":0.04})
        games_btn = HoverButtonRed(text="Games" , size_hint = (0.2,0.08) , pos_hint = {"center_x":0.5 , "center_y" : 0.04})

        home_btn.bind(on_press=self.go_home_screen)

        store_btn.bind(on_press=self.go_store_screen)

        games_btn.bind(on_press=self.go_games_screen)


        self.add_widget(home_btn)
        self.add_widget(store_btn)
        self.add_widget(games_btn)

    def go_home_screen(self , instance):
        self.screen_manager.current = "home"

    def go_store_screen(self , instance ):
        self.screen_manager.current = "store"

    def go_games_screen(self , instance):
        self.screen_manager.current = "games"



