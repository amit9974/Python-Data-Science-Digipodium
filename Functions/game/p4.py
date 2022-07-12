import pgzrun

HEIGHT = 500
WIDTH = 500


box1 = Rect((140,160), (50,50))
box2 = Rect((160,200), (50,50))
box3 = Rect((250,140), (50,50))

box1_vx = 5
box2_vx = 6
box3_vx = 7

rect = Rect((20, 60), (20, 200))
rect1 = Rect((460, 60), (20, 200))

def item_control(obj,plt,speed,plt1):
    obj.x += speed
    if obj.x > WIDTH:
        obj.x = 0
    if obj.x > WIDTH:
        obj.x = 0
    
    if obj.colliderect(plt):
        speed = - speed
    
    if obj.colliderect(plt1):
        speed = - speed
    return speed

 #Plateform control  Function
def plateform_cobtrol():
    # keyboard
    if keyboard.up:
        rect.y -= 6
    if keyboard.up:
        rect1.y += 6
    if keyboard.down:
        rect.y += 6
    if keyboard.down:
        rect1.y -= 6



def draw():
    screen.fill("black")
    screen.draw.filled_rect(rect, "blue")
    screen.draw.filled_rect(rect1, "blue")
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box3, "green")
    screen.draw.filled_rect(box2, "yellow")


def update():
    global box1_vx
    global box2_vx
    global box3_vx

    box1_vx = item_control(box1, rect1, box1_vx, rect)  # We use our custom function here
    box2_vx = item_control(box2, rect1, box2_vx, rect)  # We use our custom function here
    box3_vx = item_control(box3, rect1, box3_vx, rect)  # We use our custom function here
    plateform_cobtrol()  # We use plateform control custom function here


pgzrun.go()
