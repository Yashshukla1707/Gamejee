from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
import string
import random
from kivy.graphics import Color , Line
from hover_button import HoverButtonRed
from kivy.uix.image import Image

store = JsonStore("user_data.json")

class LoginScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        layout = FloatLayout()

        bg = Image(source ="Images/Login_bg.jpg" , opacity = 0.5 , allow_stretch = True , keep_ratio = False)
        layout.add_widget(bg)

        #title
        title = Label(
            text = "Create Profile",
            font_size = 30,
            pos_hint = {
                "center_x":0.5,
                "center_y":0.9
            }
        )
        layout.add_widget(title)





        self.name_input = self.create_input(
            "Enter Your Name" , 0.8
        )

        self.mobile_input = self.create_input(
            "Enter Your Mobile Number" , 0.7
        )

        self.UID_input = self.create_input(
            "Enter Your Unique Id" , 0.6
        )

        layout.add_widget(self.name_input)
        layout.add_widget(self.mobile_input)
        layout.add_widget(self.UID_input)
        # ----------------------------------------------------------------------------------------------------------------------

        # class buttons
        self.class_choice = "12"

        class11 = ToggleButton(
            text="Class 11",
            group="class",
            size_hint = (0.1 , 0.04),
            pos_hint={
                "center_x": 0.35,
                "center_y": 0.4
            }
        )

        class12 = ToggleButton(
            text="Class 12",
            group="class",
            size_hint = (0.1 , 0.04),
            pos_hint={
                "center_x": 0.65,
                "center_y": 0.4
            }
        )

        class11.bind(on_press=lambda x: self.set_class("11"))
        class12.bind(on_press=lambda x: self.set_class("12"))
        layout.add_widget(class11)
        layout.add_widget(class12)

        # -----------------------------------------------------------------------------------------------------------------------

        # stream
        self.stream = "Engineering"

        eng = ToggleButton(
            text="Engineering",
            group="stream",
            size_hint = (0.1,0.04),
            pos_hint={
                "center_x": 0.35,
                "center_y": 0.3,
            }
        )

        med = ToggleButton(
            text="Medical",
            group="stream",
            size_hint=(0.1, 0.04),
            pos_hint={
                "center_x": 0.65,
                "center_y": 0.3
            }
        )

        eng.bind(on_press=lambda x: self.set_stream("Engineering"))
        med.bind(on_press=lambda x: self.set_stream("Medical"))

        layout.add_widget(eng)
        layout.add_widget(med)

        #Store Button
        store = HoverButtonRed(
            text="Store", size_hint=(0.1, 0.04), pos_hint={"center_x": 0.03, "center_y": 0.98}
        )
        store.bind(on_press=self.go_store)
        layout.add_widget(store)

        #Continue button
        btn = HoverButtonRed(
            text="Continue",
            size_hint=(0.4, 0.08),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.2
            }
        )

        btn.bind(on_press=self.create_profile)
        layout.add_widget(btn)



        #Submit Button
        submit_btn = HoverButtonRed(
            text = "Submit", size_hint = (0.4, 0.1) ,pos_hint = {"center_x":0.5  , "center_y":0.1}
        )

        submit_btn.bind(on_press = self.go_home)
        layout.add_widget(submit_btn)

        self.add_widget(layout)

    def create_input(self, hint, y):
        box = TextInput(
            hint_text=hint,
            size_hint=(0.4, 0.05),
            pos_hint={"center_x": 0.5, "center_y": y},
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            font_name="Roboto",
        )
        with box.canvas.before:
            Color(1, 1, 1, 1)
            border_line  = Line(
                rectangle = (
                    box.x,
                    box.y,
                    box.width ,
                    box.height
                ),width = 1 )

        box.bind(pos=lambda instance , value:self.update_border(instance,border_line) ,
                 size = lambda instance , value:self.update_border(instance , border_line))
        return box

    def go_home(self,instance):
        self.manager.current = "home"

    def set_class(self , value):
        self.class_choice = value

    def set_stream(self,value):
        self.stream = value

    def generate_id(self):
        chars = string.ascii_uppercase+string.digits
        return "".join(random.choice(chars) for i in range(8))

    def create_profile(self,instance):
        user_id = self.generate_id()

        store.put(
            "profile",
            name = self.name_input.text,
            class_name = self.class_choice,
            stream = self.stream,
            id  = user_id
        )
        print("User ID",user_id)


    def go_store(self , instance):
        self.manager.current = "store"

    def update_border(self , instance , border_line):

        border_line.rectangle = (
            instance.x ,
            instance.y,
            instance.width ,
            instance.height
        )





