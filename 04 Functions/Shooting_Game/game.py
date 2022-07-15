from glob import glob
from turtle import pos
import pgzrun
import random




HEIGHT = 400
WIDTH = 600


hero = Actor('hero',(30,280))
background = Actor('background')
enemy = Actor('enemy',(380,280))
bullets = []
enemies = []

max_bullet = 3
level = 1
score = 0
lives = 3


def draw():
    screen.clear()
    background.draw()
    hero.draw()
    
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    draw_text()



# Move Hero
def move_hero():
    if keyboard.left:
        hero.x -= 6
    if keyboard.right:
        hero.x += 6


# create enemy
# def create_enemies():
#     for x in range(0, 300, 10):
#         for y in range(0, 200, 80):
#             enemy = Actor('enemy', (x, y),(380,280))
#             enemy.vx = level * 2
#             enemies.append(enemy)

# create_enemies()
        
      
            

# # Move Eenemy
def move_enemy():
    global score
    global enemy
    for enemy in enemies:
        enemy.x = enemy.x - 2
        if enemy.x > WIDTH:
            enemy.x =  0
        if enemy.x <  0:
            enemy.x = 0
            animate(enemy, duration=0.2, x=enemy.x + 10)
    for bullet in bullets:
        if bullet.colliderect(enemy):
            enemies.remove(enemy)
            bullets.remove(bullet)
            score += 1
        if enemy.colliderect(hero):
            exit()




    # if enemy.x > WIDTH:
    #     enemy.x = 0
    # if enemy.x < 0:
    #     enemy.x = 0
    #     enemy.x = enemy.vx
    #     animate(enemy, duration=0.2, x=enemy.x + 10)
    # for bullet in bullets:
    #     if bullet.colliderect(enemy):
    #         enemies.remove(enemy)
    #         bullets.remove(bullet)
    #         score += 1
    #     if enemy.colliderect(hero):
    #         exit()


def draw_text():
    screen.draw.text("Level" + str(level), (0,0), color='red')
    screen.draw.text("Score" + str(score), (100,0), color='blue')
    screen.draw.text("Lives" + str(lives), (200,0), color="yellow")



def on_key_down(key):
    if key == keys.SPACE and len(bullets) < max_bullet:
        bullet = Actor("bullet",(150,250))   
        bullets.append(bullet)

        

def move_bullets(): 
    for bullet in bullets:
        bullet.x = bullet.x + 2
        if bullet.x > WIDTH:
            bullet.x = 10
  
           
            




# Call all function here

def update():

    move_hero()
    # create_enemies()
    move_enemy()
    move_bullets()
    # check_end_of_level()


pgzrun.go()