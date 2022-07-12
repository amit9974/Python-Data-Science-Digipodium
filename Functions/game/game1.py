import pgzrun
import random

# Step1 Start your game startup here

HEIGHT = 500
WIDTH = 700

MAX_BULLETS = 3

level = 1
lives = 3
score = 0

background = Actor("background")
player = Actor('player', (350, 460))
enemies = []
bombs = []
bullets = []
music.play('m1.mp3')

# Step 2  Draw your all actors here
def draw():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()


# Step3 Move your Actors

def update(delta):
    move_player()
    move_enemies()
    move_bullets()
    create_bombs()
    move_bombs()
    check_for_end_of_level()



# Step4 Define your Function
def move_player():
    if keyboard.left:
        player.x -= 2
    if keyboard.right:
        player.x += 2
    if keyboard.up:
        player.y -= 2
    if keyboard.down:
        player.y +=2



# Step5 Create enemies

def create_enemies():
    for x in range(0, 600, 60):
        for y in range(0, 200, 60):
            enemy = Actor('enemy', (x, y))
            enemy.vx = level * 2
            enemies.append(enemy)

create_enemies()



# Step6 Move the enemy
def move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            exit()
        



# step7 Draw text on the screen

def draw_text():
    screen.draw.text("Level" + str(level), (0,0), color='red')
    screen.draw.text("Score" + str(score), (100,0), color='blue')
    screen.draw.text("Lives" + str(lives), (200,0), color="yellow")



# step8 Player Bullet
def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor("bullet", pos=(player.x, player.y))
        bullets.append(bullet)

        

def move_bullets(): 
    for bullet in bullets:
        bullet.y = bullet.y -6
        if bullet.y < 0:
            bullets.remove(bullet)



def create_bombs():
    if random.randint(0, 100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor('bomb', enemy.pos)
        bombs.append(bomb)
        

 

def move_bombs():
    global lives
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives = lives -1
            if lives == 0:
                exit()
        


def check_for_end_of_level():
    global level
    if len(enemies) == 0:
        level = level + 1
        create_enemies()



pgzrun.go()