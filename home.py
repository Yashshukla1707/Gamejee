from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from menu import BottomMenu
from hover_button import HoverButtonGreen
from back_button import BackButton
from kivy.uix.image import Image

#Creating Home Screen---------------------------------------------------------------------------------------------------
class HomeSreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(source="Images/Jee_Neet_bg.jpg", opacity = 0.2 ,  allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)


        title = Label(
            text = "Select your Exam", font_size = 30, pos_hint = {"center_x":0.5 , "center_y":0.85}
        )
        layout.add_widget(title)

#Creating JEE Exams Button
        jee_btn  = HoverButtonGreen(
            text = "JEE EXAMS", size_hint = (0.6,0.15) , pos_hint = {"center_x":0.5 , "center_y":0.6}
        )
        jee_btn.bind(on_press = self.open_jee)
        layout.add_widget(jee_btn)

#Creating NEET Exams Button
        neet_btn = HoverButtonGreen(
            text="NEET EXAMS", size_hint=(0.6, 0.15), pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        neet_btn.bind(on_press=self.open_neet)
        layout.add_widget(neet_btn)




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

    def open_jee(self , instance):
        self.manager.current = "jee"

    def open_neet(self,instance):
        self.manager.current = "neet"



