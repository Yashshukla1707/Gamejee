from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from hover_button import HoverButtonRed
from kivy.uix.scrollview import ScrollView


class GraphGameLevelScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)


        m_layout = BoxLayout(orientation = "vertical")


        self.score_label = Label(
            text = "Score : 0",
            size_hint_y =None ,
            height = dp(50),
            font_size = 15
        )
        m_layout.add_widget(self.score_label)


        scroll = ScrollView()

        self.level_layout = GridLayout(
            cols=3,
            spacing=dp(10),
            padding=dp(10),
            size_hint_y=None
        )

        self.level_layout.bind(
            minimum_height=self.level_layout.setter("height")
        )

        for level in range(1, 101):
            btn = HoverButtonRed(
                text=f"level {level}",
                size_hint_y=None,
                font_size=16
            )

            btn.bind(on_release=lambda instance, x=level: self.open_level(x))

            self.level_layout.add_widget(btn)

        scroll.add_widget(self.level_layout)

        m_layout.add_widget(scroll)

        self.add_widget(m_layout)

    def open_level(self, level_number):
        game_screen = self.manager.get_screen("graph_game_main_game_screen")

        self.manager.current = "graph_game_main_game_screen"






