import pgzrun

HEIGHT = 500
WIDTH = 500

rect = Rect((100, 300), (300, 50))
rect1 = Rect((100, 10), (300, 2))
box1 = Rect((110,60), (50,50))
box2 = Rect((180,20), (50,50))
box3 = Rect((250,40), (50,50))
box4 = Rect((320,60), (50,50))

box1_vx = 2
box2_vx = 3
box3_vx = 1.5
box4_vx = 2


# Box Motion Control Function ( Custome function is create here)
def box_motion_control():
    global box1_vx
    box1.y += box1_vx
    if box1.y > WIDTH:
        box1.y = 0
    if box1.y < 0:
        box1.y = WIDTH

    global box2_vx
    box2.y += box2_vx
    if box2.y > WIDTH:
        box2.y = 0
    if box2.y < 0:
        box2.y = WIDTH

    
    global box3_vx
    box3.y += box3_vx
    if box3.y > WIDTH:
        box3.y = 0
    if box3.y < 0:
        box3.y = WIDTH

    
    global box4_vx
    box4.y += box4_vx
    if box4.y > WIDTH:
        box4.y = 0
    if box4.y < 0:
        box4.y = WIDTH


    if box1.colliderect(rect):
        box1_vx = - box1_vx

    if box2.colliderect(rect):
        box2_vx = - box2_vx

    if box3.colliderect(rect):
        box3_vx = -box3_vx

    if box4.colliderect(rect):
        box4_vx = - box4_vx

    #cheat
    if box1.colliderect(rect1):
        box1_vx = - box1_vx
    
    if box2.colliderect(rect1):
        box2_vx = - box2_vx
    
    if box3.colliderect(rect1):
        box3_vx = - box3_vx

    if box4.colliderect(rect1):
        box4_vx = -box4_vx


# Plateform control  Function
def plateform_cobtrol():
    # keyboard
    if keyboard.left:
        rect.x -= 3
    elif keyboard.right:
        rect.x += 3

def draw():
    screen.fill("black")
    screen.draw.filled_rect(rect, "blue")
    screen.draw.filled_rect(rect1, "black")
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box2, "yellow")
    screen.draw.filled_rect(box3, "green")
    screen.draw.filled_rect(box4, "orange")


def update():
    box_motion_control()  # We use our custom function here
    plateform_cobtrol()  # We use plateform control custom function here
    



pgzrun.go()