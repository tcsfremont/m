import pgzrun
from random import random
player = Actor("crew")
player.x = 400
player.y=600 - player.height*0.5
aliens = []
def add_alien():
    alien = Actor('aliena')
    alien.x = alien.width * 0.5 + (800 - alien.width * 0.5) * random()
    alien.y = alien.height*0.5
    aliens.append(alien)
clock.schedule_interval(add_alien,5)   
lasers = []
def fire_laser():
    laser = Rect((player.x,player.y),(4,20))
    lasers.append(laser)
def update():
    if keyboard.left and player.x > player.width*0.5: 
        player.x -= 5
    if keyboard.right and player.x < 800 - player.width*0.5:
        player.x = player.x+5
    if keyboard.space:
        fire_laser()
    for alien in aliens:
        alien.y += 3
    for laser in lasers:
        laser.y -= 10
        for alien in aliens:
            if laser.x >alien.x - alien.width * 0.5:
                if laser.y > alien.y - alien.height * 0.5:
                    if laser.x < alien.x +alien.width * 0.5:
                        if laser.y < alien.y +alien.height * 0.5:
                           aliens.remove(alien)
def draw():
    screen.clear()
    player.draw()
    for laser  in lasers:
        screen.draw.filled_rect(laser,(230,30,200))
    for alien in aliens:
        alien.draw()
pgzrun.go()                             
