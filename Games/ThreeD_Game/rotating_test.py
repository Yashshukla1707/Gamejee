import math

from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.graphics import Line
from kivy.clock import Clock
from kivy.app import App
from math import  sin , cos , radians
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Line , Mesh , Color
from math import *
from kivy.uix.floatlayout import FloatLayout
from Games.ThreeD_Game.chunk import ChunkManager
from Games.ThreeD_Game.camera import Camera
from Games.ThreeD_Game.obj_loader import OBJLoader
from hover_button import HoverButtonRed


class Model:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.x = 0
        self.y = 0
        self.z = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0
        self.pitch = 0
        self.move_speed  = 0.5
        self.turn_speed  = 2
        self.walk_angle = 0.0
        self.walk_speed  = 6.0
        self.walking = False
        self.swing = 0
class Renderer:
    def __init__(self):
        self.models = []
    def clear(self):
        self.models.clear()
class RotatorScreen(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        self.keys = {}
        self.update_event = None
        self.move_forwward = False
        self.move_backward = False
        self.move_left = False
        self.move_right = False
        self.touch_last_x = None
        self.touch_last_y = None
        self.touch_sensitivity = 0.01
        Window.bind(on_key_down = self.key_down)
        Window.bind(on_key_up = self.key_up)
        Window.bind(mouse_pos = self.on_mouse_move)
        self.mouse_senstivity = 0.08
        self.last_mouse_x = Window.width // 2
        self.last_mouse_y = Window.height // 2
        self.camera = Camera()
        self.player = Player()
        self.chunk_manager = ChunkManager()
        self.renderer = Renderer()
        self.world = []
        #for x in range(-2 ,3 ):
            #for z in range(-2 , 3):
                #self.world.append((x * 1 , 0 , z*1))
        self.road = OBJLoader()
        self.road.load("Images/road.obj")
        self.character = OBJLoader()
        self.character.load("Images/character-a.obj")
        print("Character Vertices:" , len(self.character.vertices))
        print("Character faces:", len(self.character.faces))
        self.controller = FloatLayout(size_hint=(1, 1))
        self.btn_W = Button(
            text="W",
            size_hint=(None, None),
            size=(70, 70),
            pos=(120, 170),
        )
        self.btn_S = Button(
            text="S",
            size_hint=(None, None),
            size=(70, 70),
            pos=(120, 30),
        )
        self.btn_A = Button(
            text="A",
            size_hint=(None, None),
            size=(70, 70),
            pos=(40, 100),
        )
        self.btn_D = Button(
            text = "D",
            size_hint=(None, None),
            size=(70, 70),
            pos=(200, 100),
        )
        normal_color = (0.55 , 0.55 , 0.55 , 1)
        pressed_color = (0.75 , 0.75 , 0.75 , 0.7)
        self.btn_W.background_color = normal_color
        self.btn_A.background_color = normal_color
        self.btn_S.background_color = normal_color
        self.btn_D.background_color = normal_color
        self.btn_W.bind(on_press=self.forward_press,
                        on_release=self.forward_release)
        self.btn_S.bind(on_press=self.backward_press,
                        on_release=self.backward_release)
        self.btn_A.bind(on_press=self.left_press,
                        on_release=self.left_release)
        self.btn_D.bind(on_press=self.right_press,
                        on_release=self.right_release)

        self.controller.add_widget(self.btn_W)
        self.controller.add_widget(self.btn_S)
        self.controller.add_widget(self.btn_A)
        self.controller.add_widget(self.btn_D)
        self.exit_btn = HoverButtonRed(
            text = "Exit",
            size_hint = (0.1 , 0.1),
            pos_hint = {"left" : 0.98 , "top" : 0.95}
        )
        self.exit_btn.bind(on_press = self.exit_game)
        self.add_widget(self.exit_btn)
        self.add_widget(self.controller)
    def exit_game(self , instance ):
        self.manager.current = "games"


    def on_enter(self):
        Window.clearcolor = (
            0.53 , 0.81 , 0.98 , 1
        ) # sky blue
        Clock.unschedule(self.update)
        self.update_event =Clock.schedule_interval(self.update , 1/60)

    def on_leave(self):
        Clock.unschedule(self.update)
        self.update_event = None
        self.canvas.after.clear()
        self.renderer.clear()
        Window.clearcolor = (
            0 , 0 , 0 , 1
        )
    def forward_press(self , instance):
        self.move_forwward = True
        self.btn_W.background_color = (0.75 , 0.75 , 0.75 , 0.7)
    def forward_release(self , instance):
        self.move_forwward = False
        self.btn_W.background_color = (0.55 , 0.55 , 0.55 , 1)
    def backward_press(self , instance):
        self.move_backward = True
        self.btn_S.background_color = (0.75 , 0.75 , 0.75 , 0.7)
    def backward_release(self , instance):
        self.move_backwward = False
        self.btn_S.background_color = (0.55 , 0.55 , 0.55 , 1)
    def left_press(self , instance):
        self.move_left = True
        self.btn_A.background_color = (0.75 , 0.75 , 0.75 , 0.7)
    def left_release(self , instance):
        self.move_left = False
        self.btn_A.background_color = (0.55 , 0.55 , 0.55 , 1)
    def right_press(self , instance):
        self.move_right = True
        self.btn_D.background_color = (0.75 , 0.75 , 0.75 , 0.7)
    def right_release(self , instance):
        self.move_right = False
        self.btn_D.background_color = (0.55 , 0.55 , 0.55 , 1)
    def project_point(self , x , y , z):
        dx = x - self.camera.camera_x
        dy = y - self.camera.camera_y
        dz = z - self.camera.camera_z
        yaw = radians(self.camera.camera_yaw)
        cos_y = cos(yaw)
        sin_y = sin(yaw)
        rx = dx * cos_y - dz * sin_y
        rz = dx * sin_y + dz * cos_y
        pitch = radians(self.camera.camera_pitch)
        cos_p = cos(pitch)
        sin_p = sin(pitch)
        ry = dy * cos_p - rz * sin_p
        rz = dy * sin_p + rz * cos_p
        if rz <= 0.1:
            return None
        f = 400
        sx = Window.width/2 + rx * f/rz
        sy = Window.height/2 + ry * f/rz
        return sx , sy
    def draw_obj(self):
        with self.canvas.after:
            Color(0 , 0 , 0)
            for chunk in self.chunk_manager.loaded_chunks.values():
                for world_x , world_z in chunk:
                    world_y = 0
                    for face in self.road.faces:
                        points = []
                        for index in  face :
                            vx , vy , vz = self.road.vertices[index]
                            x = vx + world_x
                            y = vy + world_y
                            z = vz + world_z
                            p = self.project_point(x , y , z)
                            if p:
                                points.append(p)

                            if len(points) >=2 :
                                for i in range(len(points)):
                                    x1 , y1 = points[i]
                                    x2 , y2 = points[(i+1)  % len(points)]

                                Line(points = [x1 , y1 , x2 , y2] , width = 1)

    def rotate_x(self , x, y, z, angle):
        angle = math.radians(angle)

        c = math.cos(angle)
        s = math.sin(angle)

        ny = y * c - z * s
        nz = y * s + z * c
        return x , ny , nz
    def draw_character(self):
        left_leg_angle = self.player.swing
        right_leg_angle = -self.player.swing
        left_arm_angle = - self.player.swing
        right_arm_angle = self.player.swing
        with self.canvas.after:
            Color(0 , 0 , 0)
            for group_name , group_data in self.character.groups.items():
                if group_name == "leg-left":
                    angle = left_leg_angle
                elif group_name == "leg-right":
                    angle = right_leg_angle
                elif group_name == "arm-left":
                    angle = left_arm_angle
                elif group_name == "arm-right":
                    angle = right_arm_angle
                else:
                    angle = 0
                pivot = self.character.pivots[group_name]
                for face in group_data["faces"]:
                    points = []
                    for index in face:
                        vx , vy , vz = self.character.vertices[index]
                        oy = vy
                        oz = vz

                        if group_name in ("leg-left" , "leg-right" , "arm-left" , "arm-right"):
                            vx , vy , vz = self.rotate_x_pivot(
                                vx , vy , vz , angle , pivot[0] , pivot[1] , pivot[2]
                            )
                        s = 1
                        x = vx * s + self.player.x
                        y = vy * s + self.player.y
                        z =-vz * s + self.player.z
                        p = self.project_point(x ,  y , z)
                        if p is not None:
                            points.append(p)
                        if len(points) >= 2 :
                            for i in range(len(points)):
                                x1 , y1 = points[i]
                                x2 , y2 = points[(i+1) % len(points)]
                            Line(points = [x1 , y1 , x2 ,y2], width =1)
    def rotate_x_pivot(self , x , y , z , angle , px , py  , pz):
        angle = math.radians(angle)
        x -= px
        y -= py
        z -= pz
        c = cos(angle)
        s = sin(angle)
        new_y = y*c - z*s
        new_z = y*s + z*c
        x += px
        new_y += py
        new_z += pz
        return x , new_y , new_z
    def update(self , dt):
        self.canvas.after.clear()
        self.renderer.clear()
        self.player.walking = False
        angle = radians(self.player.yaw)
        speed = self.player.move_speed
        direction = None
        if self.keys.get(ord('w') , False) or self.move_forwward:
            direction = "forward"
            self.player.walking = True
            self.player.x += math.sin(angle) * speed
            self.player.z += math.cos(angle) * speed
        if self.keys.get(ord('s') , False) or self.move_backward:
            direction = "back"
            self.player.walking = True
            self.player.x -= math.sin(angle) * speed
            self.player.z -= math.cos(angle) * speed
        if self.keys.get(ord('a') , False) or self.move_left:
            direction = "left"
            self.player.walking = True
            self.player.x -= math.cos(angle) * speed
            self.player.z += math.sin(angle) * speed
        if self.keys.get(ord('d') , False) or self.move_right:
            direction = "right"
            self.player.walking = True
            self.player.x += math.cos(angle) * speed
            self.player.z += math.sin(angle) * speed
        self.camera.camera_x =  self.player.x
        self.camera.camera_y = self.player.y + 2
        self.camera.camera_z = self.player.z -5
        self.camera.camera_yaw = self.player.yaw
        self.camera.camera_pitch = self.player.pitch
        if self.player.walking:
            self.player.walk_angle += dt * self.player.walk_speed
        else:
            self.player.walk_angle  = 0
        chunk_size = self.chunk_manager.chunk_size
        offset = chunk_size//2
        current_chunk_x = math.floor((self.player.x + offset)/chunk_size)
        current_chunk_z = math.floor((self.player.z + offset) / chunk_size)
        self.chunk_manager.update_chunks(
            current_chunk_x , current_chunk_z
        )
        self.draw_obj()
        self.player.swing = math.sin(self.player.walk_angle) * 25
        self.draw_character()
    def key_down(self  , window , key ,  scancode , codepoint , modifiers):
        self.keys[key] = True
        if key == ord('w'):
            self.btn_W.state = "down"
        elif key == ord('s'):
            self.btn_S.state = "down"
        elif key == ord('a'):
            self.btn_A.state = "down"
        elif key == ord('d'):
            self.btn_D.state = "down"
    def key_up(self , window , key  , scancode):
        self.keys[key] = False
        if key == ord('w'):
            self.btn_W.state = "normal"
        elif key == ord('s'):
            self.btn_S.state = "normal"
        elif key == ord('a'):
            self.btn_A.state = "normal"
        elif key == ord('d'):
            self.btn_D.state = "normal"
    def on_mouse_move(self , window , pos):
        x , y  = pos
        dx = x - self.last_mouse_x
        dy = y - self.last_mouse_y
        self.last_mouse_x = x
        self.last_mouse_y = y

        self.player.yaw += dx * self.mouse_senstivity
        self.player.pitch += dy * self.mouse_senstivity

        if self.player.pitch > 89:
            self.player.pitch = 89
        elif self.player.pitch < -89:
            self.player.pitch = -89
    def on_touch_down(self, touch):
        if self.controller.collide_point(*touch.pos):
            return super().on_touch_down(touch)
        self.touch_last_x = touch.x
        self.touch_last_y = touch.y
        return True
    def on_touch_move(self, touch):
        if self.touch_last_x is None:
            return super().on_touch_move(touch)
        if self.controller.collide_point(*touch.pos):
            return super().on_touch_move(touch)
        dx = touch.x - self.touch_last_x
        dy = touch.y - self.touch_last_y
        self.player.yaw += dx * self.touch_sensitivity
        self.player.pitch += dy * self.touch_sensitivity
        self.touch_last_x = touch.x
        self.touch_last_y = touch.y
        return True
    def on_touch_up(self, touch):
        self.touch_last_x = None
        self.touch_last_y = None
        return super().on_touch_up(touch)
