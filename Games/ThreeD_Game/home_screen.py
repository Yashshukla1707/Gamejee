from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from hover_button import HoverButtonYellow , HoverButtonGreen , HoverButtonRed

class ThreeDGameHomeScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(
            source="Images/3DGameHomeScreenLogo.jpg", opacity=0.5, allow_stretch=True, keep_ratio=False
        )
        layout.add_widget(bg)
        start_btn = HoverButtonYellow(
            text="Start Game",
            size_hint=(0.1, 0.1),
            pos_hint={"center_x": 0.2, "center_y": 0.6}
        )
        start_btn.bind(on_press=self.go_game)
        back_btn = HoverButtonYellow(
            text="Back",
            size_hint=(0.1, 0.1),
            pos_hint={"center_x": 0.2, "center_y": 0.2}
        )
        back_btn.bind(on_press=self.go_back)
        Store = HoverButtonYellow(
            text="Store",
            size_hint=(0.1, 0.1),
            pos_hint={"center_x": 0.2, "center_y": 0.4}
        )
        Store.bind(on_press=self.go_store)

        layout.add_widget(start_btn)
        layout.add_widget(Store)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_game(self , instance):
        self.manager.current = "3D_rotating_game_screen"
    def go_back(self , instance):
        self.manager.current = "games"
    def go_store(self , instance):
        self.parent.manager.current = "store"