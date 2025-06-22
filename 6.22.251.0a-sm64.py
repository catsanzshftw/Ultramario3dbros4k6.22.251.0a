from ursina import *
from ursina.prefabs.button import Button

app = Ursina()

# --- Background color ---
camera.ui.background_color = color.cyan

# --- Title Text ---
title = Text("Ultra Mario 3D Bros",
             origin=(0,0),
             scale=3,
             y=0.45,
             color=color.yellow,
             outline=2,
             font='VeraMono.ttf')  # use any TTF you like, default is ok

# --- Buttons ---
start_btn = Button(text='START', color=color.orange, scale=(.35,.12), y=0.1)
options_btn = Button(text='OPTIONS', color=color.lime, scale=(.35,.12), y=-0.10)
quit_btn = Button(text='QUIT', color=color.red, scale=(.35,.12), y=-0.30)

# --- Simple button hover effect ---
for btn in (start_btn, options_btn, quit_btn):
    btn.animate_x(0, duration=0.4 + 0.1 * [start_btn, options_btn, quit_btn].index(btn), curve=curve.out_elastic)
    def _hover(b=btn):
        b.scale = (0.39, 0.13) if b.hovered else (0.35, 0.12)
    btn.on_mouse_enter = lambda b=btn: setattr(b, 'scale', (0.39, 0.13))
    btn.on_mouse_exit = lambda b=btn: setattr(b, 'scale', (0.35, 0.12))

def update():
    # You can put menu logic here, like keyboard navigation, etc.
    pass

app.run()
