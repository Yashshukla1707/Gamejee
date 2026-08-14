from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from hover_button import HoverButtonRed
from back_button import BackButton
from kivy.uix.floatlayout import FloatLayout
from image_button import ImageButton
from kivy.metrics import dp

class GameScreen(Screen):

    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        shooting_game_btn = ImageButton(
            source = "Images/ShootingGameIcon.jpg",
            size_hint = (0.15,0.15),
            pos_hint = {"center_x": 0.2 , "center_y": 0.7},
            allow_stretch = True ,
            keep_ratio = True
        )
        shooting_game_btn.bind(on_press = self.go_shooting_game)


        graph_game_btn = ImageButton(
            source = "Images/GraphGameIcon.jpg",
            size_hint = (0.15,0.15),
            pos_hint = {"center_x": 0.2 , "center_y": 0.5},
            allow_stretch = True ,
            keep_ratio = True
        )
        graph_game_btn.bind(on_press = self.go_graph_game)

        ThreeD_game_btn =ImageButton(
            source = "Images/3DGameIcon.jpg",
            size_hint = (0.15,0.15),
            pos_hint = {"center_x": 0.2 , "center_y": 0.3},
            allow_stretch = True ,
            keep_ratio = True
        )
        ThreeD_game_btn.bind(on_press = self.go_threed_game)

        layout.add_widget(shooting_game_btn)
        layout.add_widget(graph_game_btn)
        layout.add_widget(ThreeD_game_btn)

        back_btn = BackButton(
            self, size_hint=(0.2, 0.08),
            pos_hint={"x": 0.02, "top": 0.95}
        )

        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_shooting_game(self , instance):
        self.manager.current  = "shooting_game_loading_screen"

    def go_graph_game(self , instance):
        self.manager.current = "graph_game_loading_screen"
    def go_threed_game(self , instance):
        self.manager.current = "3D_game_loading_screen"















