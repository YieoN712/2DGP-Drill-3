from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)

def run_top():
    print('Top')
    for x in range(0,800,10):
        draw_boy(x, 550)
    pass

def run_right():
    print('Right')
    for y in range(600,0,-10):
        draw_boy(780, y)
    pass

def run_bottom():
    print('Bottom')
    for x in range(780,0,-10):
        draw_boy(x, 50)
    pass

def run_left():
    print('Left')
    pass

def run_rectangle():
    print('Rectangle')

    #run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_circle():
    print('Circle')

    r, cx, cy = 300, 800 // 2, 600 // 2
    
    for d in range(0, 360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy

        draw_boy(x, y)
    
    pass

while True:
    #run_circle()
    run_rectangle()
    break

close_canvas()
