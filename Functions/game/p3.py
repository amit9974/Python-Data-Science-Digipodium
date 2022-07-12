import pgzrun

HEIGHT = 500
WIDTH = 500


box1 = Rect((110,-300), (50,50))
box2 = Rect((180,20), (50,50))
box3 = Rect((250, 60), (50,50))

box1_vx = 5
box2_vx = 6
box3_vx = 7

rect = Rect((100, 300), (300, 10))

def item_control(obj,plt,speed):
    obj.y += speed
    if obj.y > HEIGHT:
        obj.y = 0
    if obj.y < 0:
        obj.y = 0
        speed = - speed

    if obj.colliderect(plt):
        speed = - speed
    return speed

 #Plateform control  Function
def plateform_cobtrol():
    # keyboard
    if keyboard.left:
        rect.x -= 3
    elif keyboard.right:
        rect.x += 3



def draw():
    screen.fill("black")
    screen.draw.filled_rect(rect, "blue")
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box3, "green")
    screen.draw.filled_rect(box2, "yellow")


def update():
    global box1_vx
    global box2_vx
    global box3_vx

    box1_vx = item_control(box1, rect, box1_vx)  # We use our custom function here
    box2_vx = item_control(box2, rect, box2_vx)  # We use our custom function here
    box3_vx = item_control(box3, rect, box3_vx)  # We use our custom function here
    plateform_cobtrol()  # We use plateform control custom function here


pgzrun.go()
