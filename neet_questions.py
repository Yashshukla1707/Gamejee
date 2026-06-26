from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from back_button import BackButton
from menu import BottomMenu
from hover_button import HoverButtonGreen
from kivy.uix.image import Image

class NEETScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        layout  = FloatLayout()

        bg = Image(source="Images/Neet2_bg.jpg", opacity=0.1, allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)

        neet_bio_btn = HoverButtonGreen(
            text = "Biology" ,
            size_hint = (0.5,0.1) ,
            pos_hint = {"center_x":0.5 , "center_y":0.3}
        )
        neet_bio_btn.bind(on_press = self.go_neet_bio)
        layout.add_widget(neet_bio_btn)

        neet_chem_btn = HoverButtonGreen(
            text="Chemistry",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        neet_chem_btn.bind(on_press=self.go_neet_chem)

        layout.add_widget(neet_chem_btn)

        neet_phy_btn = HoverButtonGreen(
            text="Physics",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        neet_phy_btn.bind(on_press=self.go_neet_phy)

        layout.add_widget(neet_phy_btn)


        back_btn = BackButton(
            self , size_hint = (0.2 , 0.08),
            pos_hint = {"x":0.02 , "top":0.95}
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

    def go_neet_bio(self , instance):
        pass

    def go_neet_phy(self , instance):
        pass

    def go_neet_chem(self , instance ):
        pass
