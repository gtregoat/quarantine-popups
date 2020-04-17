from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from math import cos, sin, pi
from kivy.clock import Clock
from kivy.lang import Builder

import datetime


kv = """
#:import math math

[ClockNumber@Label]:
    text: str(ctx.i)
    pos_hint: {{"center_x": 0.5+0.42*math.sin(math.pi/6*(ctx.i-12)), "center_y": 0.5+0.42*math.cos(math.pi/6*(ctx.i-12))}}
    font_size: self.height/16

<MyClockWidget>:
    face: face
    ticks: ticks
    FloatLayout:
        id: face
        size_hint: None, None
        pos_hint: {{"center_x":0.5, "center_y":0.5}}
        size: 0.9*min(root.size), 0.9*min(root.size)
        canvas:
            Color:
                rgb: 0.1, 0.1, 0.1
            Ellipse:
                size: self.size     
                pos: self.pos
        {}
    Ticks:
        id: ticks
        r: min(root.size)*0.9/2
""".format(''.join([f"""
        ClockNumber:
            i: {j}
""" for j in range(1, 13)]))


Builder.load_string(kv)


class MyClockWidget(FloatLayout):
    pass


class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            # Color(0.2, 0.5, 0.2)
            # Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            # Color(0.3, 0.6, 0.3)
            # Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            # Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            # Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")
