from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from back_button import BackButton
from menu import BottomMenu

class StoreScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation = "horizontal")

        back_btn = BackButton(
            self ,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.02, "top": 0.95}
        )

        layout.add_widget(back_btn)

        self.add_widget(layout)

    def on_enter(self):
        main = BoxLayout(orientation="horizontal")
        if not hasattr(self, "menu_loaded"):
            menu = BottomMenu(self.manager)
            main.add_widget(menu)
            self.menu_loaded = True

        self.add_widget(main)


