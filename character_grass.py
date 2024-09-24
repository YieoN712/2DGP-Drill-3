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
    for x in range(0,780,10):
        draw_boy(x, 550)
    pass

def run_right():
    print('Right')
    for y in range(600,20,-10):
        draw_boy(780, y)
    pass

def run_bottom():
    print('Bottom')
    for x in range(780,0,-10):
        draw_boy(x, 50)
    pass

def run_left():
    print('Left')
    for y in range(20,600,10):
        draw_boy(10, y)
    pass

def run_leftline():
    print('LeftLine')
    for x in range(0,300,10):
        draw_boy(x, x)
    pass

def run_rightline():
    print('RightLine')
    pass

def run_rectangle():
    print('Rectangle')

    run_top()
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

def run_triangle():
    print('Triangle')

    #run_bottom()
    run_leftline()
    run_rightline()
    
    pass

while True:
    #run_circle()
    #run_rectangle()
    run_triangle()
    break

close_canvas()
