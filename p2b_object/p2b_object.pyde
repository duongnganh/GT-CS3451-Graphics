# Nguyen, Anh Duong

# I created my_bear() in project 2A
# In this project, I added motion for my_bear(): 
# 1. translation for each bear's hands, horns and pink nose
# 2. rotation for the bear's ears and feet
# I also used my_bear() as the object instancing:
# my_bear() goes back and forth and jumps over the fence()

import math

time = 0   # use time to move objects from one frame to the next
# color for bears
white = (255, 255, 255)
lblue = (225, 225, 255)
lpink = (255, 225, 225)
lgreen = (225, 255, 225)

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a light source
    ambientLight(100, 100, 100);
    lightSpecular(100, 100, 100)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    directionalLight(50, 50, 50, 0, 0, -1);
    
    noStroke()
    specular (1, 1, 1)
    shininess (1.0)
    
    pushMatrix()
    # rotate the camera view
    translate(0, 10, 0)
    rotateY(time)
    # rotateX(math.radians(-5))
    
    # 4 bears in 4 different position, moving in different speeds
    r = 3
    pushMatrix()
    const = (5*time*75)%200 - 100
    z = (50 - math.fabs(const))
    y = min(math.fabs(z) - 15, 0)
    translate(-15, y - 1.5*r, z)
    if const > 0:
        rotateY(math.radians(180))
    my_bear(r, lpink)
    popMatrix()
    
    r = 2
    pushMatrix()
    const = (3*time*75)%200 - 100
    z = (50 - math.fabs(const))
    y = min(math.fabs(z) - 15, 0)
    translate(-30, y - 1.5*r, z)
    if const > 0:
        rotateY(math.radians(180))
    my_bear(r, lblue)
    popMatrix()
    
    r = 3
    pushMatrix()
    const = (1.5*time*75)%200 - 100
    z = (math.fabs(const)-50)
    y = min(math.fabs(z) - 15, 0)
    translate(25, y - 1.5*r, z)
    if const < 0:
        rotateY(math.radians(180))
    my_bear(r, lgreen)
    popMatrix()
    
    r = 5
    pushMatrix()
    const = (time*75)%200 - 100
    z = (50 - math.fabs(const))
    y = min(math.fabs(z) - 20, 0)
    translate(10, y - 1.5*r, z)
    if const > 0:
        rotateY(math.radians(180))
    my_bear(r, white)
    popMatrix()
    
    # build the fence
    fence(5)
    popMatrix()
    
def my_bear(r = 10, col = white):
    # white
    fill (col[0], col[1], col[2])
        
    # nose    
    pushMatrix()
    sphereDetail(30)
    translate(0, -0.9*r, 0.7*r)
    scale(1.0, 1, 1.2)
    sphere(0.5*r)
    popMatrix()
    
    # head
    pushMatrix()
    sphereDetail(30)
    translate(0, -r, 0)
    scale(1.2, 1.2, 1.2)
    globe = createShape(SPHERE, r)
    globe.setTexture(loadImage("wool.jpg"))
    shape(globe)
    popMatrix()
    
    # ears
    pushMatrix()
    sphereDetail(20)
    translate(1.1*r, -1.1*r, 0.3*r)
    rotateZ(math.radians(15)+0.15*sin(50*time))
    scale(2.5, 1, 1)
    popMatrix()
    
    pushMatrix()
    sphereDetail(20)
    translate(-1.1*r, -1.1*r, 0.3*r)
    rotateZ(math.radians(-15)-0.15*sin(50*time))
    scale(2.5, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
    # body
    pushMatrix()
    sphereDetail(30)
    scale(1, 1, 0.9)
    globe2 = createShape(SPHERE, r*1.5)
    globe2.setTexture(loadImage("wool.jpg"))
    shape(globe2)
    popMatrix()
    
    # hands - left and right
    pushMatrix()
    translate((-0.5 + 0.02*sin(50*time))*r, 0, 1.2*r)
    rotateZ(math.radians(15))
    rotateY(math.radians(-30))
    scale(1.5, 1.3, 1)
    hand(0.15*r)
    popMatrix()
    
    pushMatrix()
    translate((0.5 - 0.02*sin(50*time))*r, 0, 1.2*r)
    rotateZ(math.radians(-15))
    rotateY(math.radians(30))
    scale(1.5, 1.3, 1)
    hand(0.15*r)
    popMatrix()
    
    # feet - left and right
    pushMatrix()
    translate(0.7*r, r, 0.8*r)
    rotateX(math.radians(-45) + 0.5*sin(50*time))
    scale(1.5, 0.5, 1)
    sphere(0.2*r)
    popMatrix()
    
    pushMatrix()
    translate(-0.7*r, r, 0.8*r)
    rotateX(math.radians(-45) - 0.5*sin(50*time))
    scale(1.5, 0.5, 1)
    sphere(0.2*r)
    popMatrix()
    
    # tail
    pushMatrix()
    sphereDetail(10)
    translate(0, r, -r)
    scale(1.5, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
    # black
    fill(0, 0, 0)
    
    # eyes
    pushMatrix()
    sphereDetail(10)
    translate(0.4*r, -1.2*r, 0.95*r)
    sphere(0.2*r)
    popMatrix()
    
    pushMatrix()
    sphereDetail(10)
    translate(-0.4*r, -1.2*r, 0.95*r)
    sphere(0.2*r)
    popMatrix()
    
    # gold
    fill(200, 200, 100)
    
    # horn
    pushMatrix()
    translate(-1.2*r, (-1.75 + 0.1*sin(50*time)) * r, 0)
    scale(0.15*r, 0.15*r, 0.15*r)
    spiral(1)
    popMatrix()
    
    pushMatrix()
    translate(1.2*r, (-1.75 + 0.1*sin(50*time)) * r, 0)
    scale(0.15*r, 0.15*r, 0.15*r)
    spiral(-1)
    popMatrix()
    
    # pink nose
    fill(255, 150, 175)
    
    pushMatrix()
    sphereDetail(10)
    translate(0, (0.02*sin(50*time)-0.85)*r, 1.1*r)
    scale(1.3, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
# draw horn using Archimedean spiral equation
# p = 1/-1 is used to draw left/right horn
def spiral(p):
    theta = 0
    while theta < 2* math.pi:
        r = theta
        x = p * r * math.cos(theta)
        y = r * math.sin(theta)
        
        pushMatrix()
        translate(0.75*x, 0.75*y, 0)
        rotateX(math.radians(90))
        scale(r/4, r/4, 1)
        cylinder(8)
        popMatrix()
        theta += 0.1
        
def fence(s = 4):
    fill(75, 25, 0)
    
    # vertical
    pushMatrix()
    translate(-10*s, -1.5*s, 0)
    scale(1, 3, 0.1)
    box(s)
    popMatrix()
    
    pushMatrix()
    translate(-10*s, -s*3, 0)
    rotateZ(math.radians(45))
    scale(1, 1, 0.1*math.sqrt(2))
    box(s/math.sqrt(2))
    popMatrix()
    
    pushMatrix()
    translate(10*s, -1.5*s, 0)
    scale(1, 3, 0.1)
    box(s)
    popMatrix()
    
    pushMatrix()
    translate(10*s, -s*3, 0)
    rotateZ(math.radians(45))
    scale(1, 1, 0.1*math.sqrt(2))
    box(s/math.sqrt(2))
    popMatrix()
    
    # horizontal
    pushMatrix()
    translate(0, -0.6*s-1.5*s, 0)
    scale(25, 0.5, 0.1)
    box(s)
    popMatrix()
    
    pushMatrix()
    translate(0, 0.6*s-1.5*s, 0)
    scale(25, 0.5, 0.1)
    box(s)
    popMatrix()
    
    # white nails
    fill(255, 255, 255)
    
    pushMatrix()
    translate(-10*s, -0.6*s-1.5*s, 0)
    scale(1, 1, 0.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(10*s, -0.6*s-1.5*s, 0)
    scale(1, 1, 0.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(-10*s, 0.6*s-1.5*s, 0)
    scale(1, 1, 0.5)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(10*s, 0.6*s-1.5*s, 0)
    scale(1, 1, 0.5)
    cylinder()
    popMatrix()

# create the hand from 1 cylinder and 2 sphere at both ends
def hand(r = 1.5):
    pushMatrix()
    translate (0, 0, 0)
    rotateY(math.radians(90))
    scale (r, r, r)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (r, 0, 0)
    sphere(r*1.0)
    popMatrix()
    
    pushMatrix()
    translate (-r, 0, 0)
    sphere(r*1.0)
    popMatrix()
    
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 32):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        # normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        # normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

    