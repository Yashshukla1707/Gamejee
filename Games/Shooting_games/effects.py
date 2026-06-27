from kivy.uix.widget import Widget
from kivy.graphics import Rectangle , Color
from kivy.clock import Clock
from kivy.vector import Vector


class Piece(Widget):
    def __init__(self , pos , velocity , **kwargs):
        super().__init__(**kwargs)

        self.size = (12 , 12)

        self.pos = pos

        self.velocity = Vector(velocity)

        with self.canvas:
            Color(1,0.3 ,0)

            self.body = Rectangle(
                pos = self.pos ,
                size = self.size
            )

        Clock.schedule_interval(self.update , 1/60)

    def update(self , dt):
        self.x += self.velocity.x
        self.y += self.velocity.y

        self.velocity.y -= 0.3

        self.body.pos = self.pos

        if self.y < -50:
            if self.parent:
                self.parent.remove_widget(self)

                Clock.unschedule(self.update)

def break_block(game , x , y):
    directions = [
        (6 , 6),
        (6,6),
        (6 , -6),
        (-6 , -6)
    ]
    for direction in directions:
        piece = Piece(
            pos = (x , y),
            velocity=direction
        )

        game.add_widget(piece)