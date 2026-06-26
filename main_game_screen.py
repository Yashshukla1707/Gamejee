from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle ,Ellipse ,Color
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.window import  Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from .effects import  break_block
from kivy.uix.screenmanager import Screen
from hover_button import HoverButtonRed

class Bird(Widget):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.size = (35,35)
        self.pos = (150,200)

        self.velocity = Vector(0,0)

        self.launched = False

        self.dragging = False

        with self.canvas:
            Color(1,0,0)
            self.shape = Ellipse(
                pos =self.pos ,
                size = self.size
            )

    def update_graphics(self):
        self.shape.pos = self.pos

    def update(self):
        if self.launched == False:
            return

        gravity = -0.3

        self.velocity.y += gravity

        self.x  += self.velocity.x
        self.y += self.velocity.y

        if abs(self.velocity.x) < 0.05:
            self.velocity.x = 0
        if self.y <= 50 :
            self.y = 100

            self.velocity.y += -0.5
            self.velocity.x  += 0.8

        self.update_graphics()

class Block(Widget):
    def __init__(self , x ,y , **kwargs):
        super().__init__(**kwargs)

        self.size = (40, 40)

        self.pos = (x,y)

        with self.canvas:
            Color(0,1,0)
            self.shape = Rectangle(
                pos =self.pos,
                size = self.size
            )

class ShootingGame(Widget):
    def __init__(self , level = 1 , **kwargs):
        super().__init__(**kwargs)

        self.level = level

        self.score = 0
        self.hits = 0
        self.misses = 0

        with self.canvas:
            Color(0.3,0.7,1)

            self.background = Rectangle(
                pos = self.pos ,
                size = self.size
            )
            self.bind(
                pos = self.resize_game ,
                size = self.resize_game
            )

            Color(0.2,0.8,0.2)
            self.ground = Rectangle(
                pos = (0 ,50),
                size = (self.width , 50)
            )
            self.bind(size = self.update_ground)


        self.bird = Bird()
        self.add_widget(self.bird)

        self.blocks = []

        for i in range(3):
            block = Block(
                600 , 100 + i * 100
            )

            self.blocks.append(block)
            self.add_widget(block)

        Clock.schedule_interval(
            self.game_loop ,
            1/60
        )

        self.score = 0

        self.message = Label(
            text = "",
            font_size = 40 ,
            size_hint = (None , None),
            size =  (400 , 100),
            pos = (250 , 450)
        )

        self.add_widget(self.message)



        self.hud = FloatLayout(
            size = self.size,
            pos = self.pos
        )
        self.bind(size = self.update_hud_size)
        self.add_widget(self.hud)

        self.score_label = Label(
            text="Score : 0",
            font_size=15,
            color = (0,0,0,1),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint = {
                "right" : 0.98 , "top" : 0.95
            }
        )
        self.hit_label = Label(
            text="Hits : 0",
            font_size=15,
            color = (0,0,0,1),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={
                "right": 0.98, "top": 0.90
            }
        )
        self.miss_label = Label(
            text="Miss : 0",
            font_size=15,
            color = (0,0,0,1),

            size_hint=(None, None),
            size=(200, 50),

            pos_hint={
                "right": 0.98, "top": 0.85
            }
        )
        self.velocity_label = Label(
            text="Velocity:",
            font_size=15,
            color=(0, 0, 0, 1),

            size_hint=(None, None),
            size=(200, 50),

            pos_hint={
                "right": 0.98, "top": 0.80
            }
        )
        self.angle_label = Label(
            text="Projection Angle:",
            font_size=15,
            color=(0, 0, 0, 1),

            size_hint=(None, None),
            size=(200, 50),

            pos_hint={
                "right": 0.98, "top": 0.75
            }
        )
        self.horizontal_range_label = Label(
            text="Horizontal Range:",
            font_size=15,
            color=(0, 0, 0, 1),

            size_hint=(None, None),
            size=(200, 50),

            pos_hint={
                "right": 0.98, "top": 0.70
            }
        )
        self.hud.add_widget(self.score_label)
        self.hud.add_widget(self.hit_label)
        self.hud.add_widget(self.miss_label)
        self.hud.add_widget(self.velocity_label)
        self.hud.add_widget(self.angle_label)
        self.hud.add_widget(self.horizontal_range_label)


    def show_message(self , text):
        self.message.text = text

        Clock.schedule_once(self.clear_message , 3)

    def clear_message(self , dt):
        self.message.text = ""

    def update_hud_size(self, *args):
        self.hud.size = self.size

    def on_touch_down(self, touch):
        if self.bird.collide_point(*touch.pos):
            self.drag_start = touch.pos
            self.bird.dragging = True

        return True

    def on_touch_move(self, touch):
        if self.bird.dragging:
            self.bird.pos = (
                touch.x-25,
                touch.y-25
            )

        self.bird.update_graphics()
        return True

    def on_touch_up(self, touch):
        if self.bird.dragging:
            power_x = self.drag_start[0] - touch.x

            power_y = self.drag_start[1] - touch.y

            self.bird.velocity =Vector(
                power_x*0.15,
                power_y*0.15
            )
            self.bird.launched = True

            self.bird.dragging =    False

        return True

    def game_loop(self ,dt):
        self.bird.update()

        for block in self.blocks[:]:
            if self.bird.launched and self.bird.collide_widget(block):
                break_block(
                    self , block.x , block.y
                )
                self.score += 10
                self.hits += 1
                self.score += 10
                self.update_hud()
                self.show_message("Hit!!!")

                print("Hit!!!")
                self.create_new_bird()
                print("New Bird Created")
                break

        if self.bird.y < -50 or self.bird.x > self.width + 50:
            self.misses += 1
            self.update_hud()
            self.show_message("Miss!!")
            self.create_new_bird()

        if len(self.blocks) == 0 or self.misses >= 5:
            self.show_end_popup()


    def resize_game(self , *args):
        self.background.pos = self.pos
        self.background.size = self.size

    def update_ground(self , *args):
        self.ground.size = (
            self.width ,
            50)
        self.ground.pos = (
            0 , 0
        )
    def create_new_bird(self):
        self.remove_widget(self.bird)
        self.bird = Bird()
        self.add_widget(self.bird)

    def update_hud(self):
        self.score_label.text = (
            "Score :" + str(self.score)
        )
        self.hit_label.text = (
            "Hit :" + str(self.hits)
        )
        self.miss_label.text = (
            "Miss :" + str(self.misses)
        )
    def show_end_popup(self):
        layout  =BoxLayout(
            orientation  = "vertical" , spacing =10
        )
        result = Label (text = f"""

    GAME OVER!!!!!
    BLOCKS HITS : {self.hits}
    MISSED : {self.misses}
    TOTAL SCORE : {self.score}""")
        close = Button(text = "ok")

        layout.add_widget(result)
        layout.add_widget(close)

        popup = Popup(
            title = "Final Result",
            content = layout ,
            size_hint = (None , None ),
            size = (300 , 300)
        )
        close.bind(on_press = popup.dismiss)
        popup.open()


class ShootingGameMainGameScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.level = 1
        self.blocks = []

        game = ShootingGame()
        self.add_widget(game)
        self.exit_btn = HoverButtonRed(
            text = "Exit",
            size_hint = (0.1 , 0.1),
            pos_hint = {"left" : 0.98 , "top" : 0.95}
        )
        self.exit_btn.bind(on_press = self.exit_game)



        self.add_widget(self.exit_btn)

    def exit_game(self , instance ):
        self.manager.current = "home_screen"


    def start_level(self , level_number):
        self.level =level_number
        print("Starting level:" , level_number)

        self.blocks.clear()
        self.create_blocks()


    def create_blocks(self):
        for block in self.blocks:
            self.remove_widget(block)

        self.blocks = []

        total_blocks = min(5 + self.level , 20)

        rows = 5
        cols = 6

        for i in range(total_blocks):
            row = i // cols
            col =  i % cols


            x = 500 + col * 80
            y = 100 + row * 80
            block = Block(
                x = x , y= y
            )

            self.blocks.append(block)
            self.add_widget(block)




