from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from hover_button import HoverButtonRed , HoverButtonYellow
from kivy.graphics import Color , Rectangle , Line
from kivy.uix.checkbox import CheckBox
from kivy.uix.relativelayout import RelativeLayout



class FunctionPanel(BoxLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing =5
        self.padding = 10


        row_make = self.create_input()

    def create_input(self ,*args):
        self.row = BoxLayout(
            orientation = "horizontal" , size_hint_y = None , height = 40 , spacing = 10
        )
        self.cb = CheckBox(
            active = True , size_hint = (None, None) , size = (40 , 40))
        self.func_input = TextInput(text = "" , multiline = False)

        self.row.add_widget(self.cb)
        self.row.add_widget(self.func_input)
        self.add_widget(self.row)

class LeftPanel(BoxLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_x = 0.30

        clicked = None
        with self.canvas.before:
            Color(0,0,0,1)
            self.bg = Rectangle(pos = self.pos , size = self.size)


        self.bind(pos  = self.update_bg , size = self.update_bg)

        add_btn = Button(
            text="Add",
            size = (30 , 40),
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        add_btn.bind(on_press=self.call_root)
        self.add_widget(add_btn)

    def call_root(self, *args):
        root = BoxLayout(orientation = "horizontal")
        self.func_panel = FunctionPanel()
        root.add_widget(self.func_panel)
        self.add_widget(root)
        self.add_widget(Widget())

    def update_bg(self  , *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class GraphPanel(Widget):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.size_hint_x = 0.70


        with self.canvas.before:
            Color(0.18 , 0.18 , 0.18 , 1)

            self.panel_bg = Rectangle(pos = self.pos , size = self.size)

            self.bind(pos = self.update_panel)
            self.bind(size = self.update_panel)

            self.graph = GraphCanvas(size_hint = (None  , None))

            self.add_widget(self.graph)
            self.bind(size = self.update_graph, pos = self.update_graph)



    def update_graph(self , *args):
        margin  = 20
        available_width = self.width  - margin*2
        available_height = self.height - margin*2

        graph_size = min(available_width , available_height)
        self.graph.size = (graph_size , graph_size)

        self.graph.pos = (
            self.x + margin*2 , self.y +(self.height - graph_size)/2
        )




    def update_panel(self , *args):
        self.panel_bg.pos = self.pos
        self.panel_bg.size = self.size


class GraphCanvas(Widget):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.show_grid = True

        self.minor_grid_spacing  = 20
        self.major_grid_spacing  =100

        self.axis_width = 3
        self.minor_grid_width = 1
        self.major_grid_width = 1.5


        with self.canvas.before:
            Color(0.92 , 0.98 , 0.92 , 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.redraw, size=self.redraw)



    def redraw(self , *args):

        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.08 , 0.10 , 0.18 ,1)
            self.bg = Rectangle(pos = self.pos  , size = self.size)




            center_x = self.center_x
            center_y = self.center_y

            if self.show_grid:
                Color(0.72 , 0.80 , 1 , 0.08)
                x = center_x
                while x <= self.right:
                    Line(points = [
                        x, self.y , x ,self.top] , width = self.minor_grid_width)
                    x += self.minor_grid_spacing

                x = center_x
                while x >= self.x:
                    Line(points=[
                        x, self.y, x, self.top], width=self.minor_grid_width)
                    x -= self.minor_grid_spacing

                y = center_y
                while y <= self.top:
                    Line(points = [
                        self.x , y , self.right , y
                    ] , width = self.minor_grid_width)
                    y += self.minor_grid_spacing

                y = center_y
                while y >= self.y:
                    Line(points=[
                        self.x, y, self.right, y
                    ], width=self.minor_grid_width)
                    y -= self.minor_grid_spacing

                Color(0.82 , 0.990 , 1 ,0.18)
                x = center_x
                while x >= self.x:
                    Line(points=[
                        x, self.y, x, self.top], width=self.major_grid_width)
                    x -= self.major_grid_spacing
                x = center_x
                while x <= self.right:
                    Line(points = [
                        x , self.y , x , self.top
                    ] , width = self.major_grid_width)

                    x += self.major_grid_spacing
                y = center_y
                while y >= self.y:
                    Line(points=[
                        self.x, y, self.right, y
                    ], width=self.major_grid_width)
                    y -= self.major_grid_spacing
                y = center_y
                while y <= self.top:
                    Line(points=[
                        self.x, y, self.right, y
                    ], width=self.major_grid_width)
                    y += self.major_grid_spacing
            Color(1 ,1 , 1, 0.95)
            Line(
                points = [
                    self.x ,
                    center_y,
                    self.right,
                    center_y
                ],
                width = self.axis_width
            )
            Line(
                points = [
                    center_x ,
                    self.y,
                    center_x,
                    self.top
                ],
                width = self.axis_width
            )




class GraphGameScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation = "horizontal")
        root.add_widget(LeftPanel())
        root.add_widget(GraphPanel())

        self.add_widget(root)