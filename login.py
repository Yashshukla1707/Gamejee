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

store = JsonStore("user_data.json")

class LoginScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

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

        #name input
        self.name_input = TextInput(
            hint_text = "Enter your name",
            size_hint = (0.7,0.08),
            pos_hint = {
                "center_x":0.5,
                "center_y":0.75
            }
        )

        layout.add_widget(self.name_input)

        #class buttons
        self.class_choice = "12"
        class11 = ToggleButton(
            text =  "Class 11",
            group = "class",
            pos_hint = {
                "center_x":0.35,
                "center_y":0.6
            }
        )

        class12 = ToggleButton(
            text = "Class 12",
            group = "class",
            state = "down",
            pos_hint = {
                "center_x":0.65,
                "center_y":0.6
            }
        )

        class11.bind(on_press = lambda x:self.set_class("11"))
        class12.bind(on_press=lambda x: self.set_class("12"))

        layout.add_widget(class11)
        layout.add_widget(class12)

        #stream
        self.stream = "Engineering"

        eng = ToggleButton(
            text = "Engineering",
            group = "stream",
            state = "down",
            pos_hint = {
                "center_x":0.35,
                "center_y":0.45,
            }
        )

        med = ToggleButton(
            text = "Medical",
            group = "stream",
            pos_hint = {
                "center_x":0.65,
                "center_y":0.45
            }
        )

        eng.bind(on_press = lambda x:self.set_stream("Engineering"))
        med.bind(on_press = lambda x:self.set_stream("Medical"))

        layout.add_widget(eng)
        layout.add_widget(med)

        #continue button

        btn = Button(
            text = "Continue",
            size_hint = (0.4,0.1),
            pos_hint = {
                "center_x":0.5,
                "center_y":0.2
            }
        )

        btn.bind(on_press=self.create_profile)
        layout.add_widget(btn)
        self.add_widget(layout)

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


