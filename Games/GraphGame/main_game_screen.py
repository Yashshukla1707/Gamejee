from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from hover_button import HoverButtonYellow, HoverButtonRed






class GraphGameMainGameScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)


        layout = FloatLayout()


        graph_btn = HoverButtonRed(
            text = "Create" ,
            size_hint = (0.3 , 0.1),
            pos_hint = {"center_x": 0.2 , "center_y" : 0.8}
        )
        graph_btn.bind(on_press = self.go_create_graph)

        layout.add_widget(graph_btn)

        back_btn = HoverButtonYellow(
            text = "Back",
            size_hint = (0.1,0.1),
            pos_hint = {"center_x": 0.2 , "center_y":0.2}
        )
        back_btn.bind(on_press = self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_create_graph(self , instance):
        self.manager.current = "graph_game_screen"

    def go_back(self , instance):
        self.manager.current = "games"