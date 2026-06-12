from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar


questions = [
    {
        "question": "What s the value of g ?" ,
        "options": ["9.8" , "8.9" , "10.8" , "12"] ,
        "answer": "9.8",
        "explanation":"Acceleration due to gravity is approximately 9.8 m/s2"


    },
    {
        "question": "Chemical formulae of water?",
        "options": ["HCl", "CO2", "H2O", "NaCl"],
        "answer": "H2O",
        "explanation": "Water contains two hydrogen atoms and one oxygen atoms "
    }
]

score = 0

class LoadingScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.progress = 0

        layout = FloatLayout()

        self.label = Label(text = "Loading Game......" , font_size = 15 ,pos_hint={"center_x":0.5 , "center_y":0.20})

        self.bar = ProgressBar(max = 100, value = 0 , size_hint = (0.8,0.05) , pos_hint = {"center_x":0.5 , "center_y":0.15})
        layout.add_widget(self.label)
        layout.add_widget(self.bar)
        self.add_widget(layout)
    def on_enter(self):
        Clock.schedule_interval(self.load_animation, 0.05)
    def load_animation(self,dt):
        self.progress += 1
        self.bar.value = self.progress

        if self.progress >= 100:
            Clock.unschedule(self.load_animation)
            self.manager.current = "home"
    def go_home(self , dt):
        Clock.unschedule(self.animate_dots)
        self.manager.current = "home"
class HomeScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(source = "Images/1774112483851.jpg" , allow_stretch = True , keep_ratio = False)
        layout.add_widget(bg)
        title = Label(text="WELCOME TO GAME" , font_size = 30 , size_hint = (0.5,0.2) , pos_hint = {"center_x":0.5 , "center_y":0.75} )
        start_btn = Button(text = "Start Quiz" , size_hint = (0.4,0.12) , pos_hint = {"center_x":0.5 , "center_y":0.25})
        start_btn.bind(on_press = self.start_quiz)
        layout.add_widget(title)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def start_quiz(self, instance):
        self.manager.current = "quiz"

class QuizScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.q_no = 0
        self.layout = BoxLayout(orientation = "vertical")
        self.question = Label(font_size = 25)
        self.buttons = []
        self.result = Label()
        self.layout.add_widget(self.question)

        for i in range(4):
            btn = Button()
            btn.bind(on_press = self.check_answer)

            self.buttons.append(btn)

            self.layout.add_widget(btn)
        self.layout.add_widget(self.result)
        self.add_widget(self.layout)

    def on_enter(self):
            self.show_question()

    def show_question(self):
        q = questions[self.q_no]
        self.question.text = q["question"]

        for i in range(4):
            self.buttons[i].text = q["options"][i]

    def check_answer(self,button):
        global score
        correct = questions[self.q_no]["answer"]

        if button.text == correct:
            score +=10
            self.result.text = "Correct +10 points"

        else:
            self.result.text = (
            "Wrong\n" + questions[self.q_no]["explanation"]
        )
        self.q_no +=1
        if self.q_no < len(questions):
            self.show_question()

        else:
            self.result.text = ("Quiz Finished\nScore:" + str(score))


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name= "loading"))
        sm.add_widget(HomeScreen(name = "home"))
        sm.add_widget(QuizScreen(name="quiz"))
        return sm

MyApp().run()