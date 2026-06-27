from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from  hover_button import HoverButtonYellow
from back_button import BackButton
from kivy.uix.image import Image



class ShootingGameHomeScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(
            source = "Images/ShootingGameLogo2.jpg" , opacity = 0.5 , allow_stretch = True , keep_ratio = False
        )
        layout.add_widget(bg)


        start_btn = HoverButtonYellow(
            text = "Start Game" ,
            size_hint = (0.1 , 0.1),
            pos_hint = {"center_x" : 0.2 ,  "center_y": 0.6}
        )
        start_btn.bind(on_press = self.go_level)


        back_btn = BackButton(
            self,
            text = "Back",
            size_hint = (0.1,0.1),
            pos_hint = {"center_x": 0.2 , "center_y" : 0.2}
        )



        Store = HoverButtonYellow(
            text = "Store",
            size_hint = (0.1,0.1),
            pos_hint = {"center_x":0.2, "center_y":0.4}
        )
        Store.bind(on_press = self.go_store)


        layout.add_widget(start_btn)
        layout.add_widget(Store)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_level(self,instance):
        self.manager.current = "level_screen"

    def go_store(self , instance):
        self.parent.manager.current = "store "



