from kivy.uix.button import Button
from kivy.core.window import Window

class HoverButtonYellow(Button):

    normal_color = (0.1,0.1,0.1,1)
    hover_color_yellow = (1 , 1,0,1)

    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.background_color = self.normal_color

        Window.bind(mouse_pos = self.on_mouse_move_yellow)

    def on_mouse_move_yellow(self , window , pos):
        if self.collide_point(*pos):
            self.background_color = self.hover_color_yellow
        else:
            self.background_color = self.normal_color


class HoverButtonGreen(Button):
    normal_color = (0.1,0.1,0.1,1)
    hover_color_green = (0,1,0,1)
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.background_color  = self.normal_color

        Window.bind(mouse_pos = self.on_mouse_move_green)

    def on_mouse_move_green(self ,window , pos):
        if self.collide_point(*pos):
            self.background_color = self.hover_color_green
        else:
            self.background_color = self.normal_color



class HoverButtonRed(Button):
    normal_color = (0.1,0.1,0.1,1)
    hover_color_green = (1 ,0,0,1)
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.background_color  = self.normal_color

        Window.bind(mouse_pos = self.on_mouse_move_green)

    def on_mouse_move_green(self ,window , pos):
        if self.collide_point(*pos):
            self.background_color = self.hover_color_green
        else:
            self.background_color = self.normal_color
