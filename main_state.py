import os

import game_framework
from pico2d import*

background = None
player = None
monster = None

class Background:
    def __init__(self):
        self.image = load_image('background-resources.assets-1727.png')

    def draw(self):
        self.image.draw(403,252)

class Player:
    def __init__(self):
        self.x, self.y = 403, 30
        self.frame = 0
        self.image = load_image('Will_Idle35.35.png')
        self.dirx, self.diry = 0, 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dirx *5
        self.y += self.diry *5

    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 60, self.x, self.y)

class Monster:
    def __init__(self):
        self.x, self.y = 403, 252
        self.speed = 5  #몬스터의 속도
        self.frame = 0
        self.image = load_image('monster.png')
        self.i = 0
    def update(self):
        self.frame = (self.frame + 1) % 21
        if self.i/100 <1 and self.frame==20:    #몬스터가 점프해서 착지할때만 이동
            t = self.i/100
            self.i+=self.speed
            self.x = (1-t)*self.x+t*player.x
            self.y = (1-t)*self.y+t*player.y
            #플레이어에게로 다가감
        delay(0.04)

    def draw(self):
        self.image.clip_draw(self.frame * 73, 0, 73, 133, self.x, self.y)

def enter():
    global background, player, monster
    player = Player()
    background = Background()
    monster = Monster()

def exit():
    global background, player, monster
    del(player)
    del(background)
    del(monster)

def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            player.image = load_image('will animation cycle35.35.png')
            if event.key == SDLK_RIGHT:
                player.dirx += 1
            elif event.key == SDLK_LEFT:
                player.dirx -= 1
            elif event.key == SDLK_UP:
                player.diry += 1
            elif event.key == SDLK_DOWN:
                player.diry -= 1
        elif event.type == SDL_KEYUP:
            player.image = load_image('Will_Idle35.35.png')
            if event.key == SDLK_RIGHT:
                player.dirx -= 1
            elif event.key == SDLK_LEFT:
                player.dirx += 1
            elif event.key == SDLK_UP:
                player.diry -= 1
            elif event.key == SDLK_DOWN:
                player.diry += 1

def update():
    monster.update()
    player.update()

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    monster.draw()
    update_canvas()


