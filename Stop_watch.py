# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
a = 0
b = 0
running = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    sec = t/10
    D = t%10
    A = t/600
    x = sec%60
    B = x/10
    C = x%10
    return str(A)+":"+str(B)+str(C)+"."+str(D)    
    
    
    
# define event handlers for buttons; "Start", "Stop", "Reset()

def start():
    global t,running
    running = True
    timer.start()
    
def stop():
    global t,a,b,running
    if running:
        a = a+1
        if(D == 0):
            b = b+1
    running = False          
    timer.stop()
    
    
def reset():
    global t,a,b
    a = 0
    b = 0   
    t = 0
    


# define event handler for timer with 0.1 sec interval
def update():
    global t
    t = t+1
   
    
def score():
    return str(b)+"/"+str(a)
    
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),[70,100],25,"White")
    canvas.draw_text(score(),[150,30],25,"White")

    
# create frame
frame = simplegui.create_frame("Stopwatch",200,200)


frame.add_button("Start",start,200)
frame.add_button("Stop",stop,200)
frame.add_button("Reset",reset,200)


# register event handlers
timer = simplegui.create_timer(100,update)
frame.set_draw_handler(draw)



# start frame
frame.start()



