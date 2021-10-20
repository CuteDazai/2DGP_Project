import os

from pico2d import*

background = None

class Background:
    def __init__(self):
        self.image = load_image('background-resources.assets-1727.png')

    def draw(self):
        self.image.draw(403,252)

def enter():
    global background
    background = Background()

def exit():
    global background
    del(background)

def handle_events():
    pass

def update():
    pass

def draw():
    clear_canvas()
    background.draw()
    update_canvas()

open_canvas(807, 505)
enter()
draw()
delay(10)
exit()
close_canvas()