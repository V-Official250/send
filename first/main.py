from data.window import Window
from data.player import Player
from data.level import Level
import time

window = Window(360,640,"game")
player = Player()
level = Level()

last_time = time.time()

while True:
    window.clear(0,0,0)

    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    window.blit(window.load("./data/img/bg.png"),0,0)

    player.update(window,dt)
    level.update(dt,player,window)

    window.loop()