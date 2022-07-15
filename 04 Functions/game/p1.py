import pgzrun

HEIGHT = 500
WIDTH = 500

box1 = Rect((100, 200), (50,50))
box2 = Rect((10, 50), (50,50))
# box3 = Rect((50, 50), (50,50))

box1_vx = 2
box2_vx = 3
# box3_vx = 2


def draw():
    screen.fill('black')
    screen.draw.text("Hello World", (10, 20), color="white")
    screen.draw.filled_rect(box2, "white")
    screen.draw.filled_rect(box1, "blue")
    # screen.draw.filled_rect(box3, "red")

def update():
    global box1_vx
    box1.x += box1_vx
    if box1.x > WIDTH:
        box1.x = 0
    if box1.x < 0:
        box1.x = WIDTH
    

    global box2_vx
    box2.y += box2_vx
    if box2.y > HEIGHT:
        box2.y = 0
    if box2.y < 0:
        box2.y = HEIGHT

    # global box3_vx
    # box2.y += box3_vx
    # if box3.y > WIDTH:
    #     box3.y = 0
    # if box3.y < 0:
    #     box3.y = HEIGHT

    if box1.colliderect(box2):
        box1_vx = -box1_vx

    if box2.colliderect(box1):
        box2_vx = - box2_vx

    # if box3.colliderect(box1):
    #     box3_vx = - box3_vx

pgzrun.go()