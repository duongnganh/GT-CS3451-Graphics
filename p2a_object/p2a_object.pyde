# Nguyen, Anh Duong
# Building my bear
import math

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (10.0)
    
    rotateY(2*time)
    # rotateX(0.5*time)
    my_bear()
    
def my_bear(r = 15):

    # white
    fill (255, 255, 255)
        
    # nose    
    pushMatrix()
    sphereDetail(60)
    translate(0, -0.9*r, 0.7*r)
    scale(1.0, 1, 1.2)
    sphere(0.5*r)
    popMatrix()
    
    # head
    pushMatrix()
    sphereDetail(60)
    translate(0, -r, 0)
    scale(1.2, 1.2, 1.2)
    sphere(r)
    popMatrix()
    
    # ears
    pushMatrix()
    sphereDetail(60)
    translate(1.1*r, -1.1*r, 0.3*r)
    rotateZ(math.radians(15))
    scale(2.5, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
    pushMatrix()
    sphereDetail(60)
    translate(-1.1*r, -1.1*r, 0.3*r)
    rotateZ(math.radians(-15))
    scale(2.5, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
    # body
    pushMatrix()
    sphereDetail(60)
    scale(1, 1, 0.9)
    sphere(1.5*r)
    popMatrix()
    
    # hands - left and right
    pushMatrix()
    translate(-0.5*r, 0, 1.2*r)
    rotateZ(math.radians(15))
    rotateY(math.radians(-30))
    scale(1.5, 1.3, 1)
    hand(0.15*r)
    popMatrix()
    
    pushMatrix()
    translate(0.5*r, 0, 1.2*r)
    rotateZ(math.radians(-15))
    rotateY(math.radians(30))
    scale(1.5, 1.3, 1)
    hand(0.15*r)
    popMatrix()
    
    # feet - left and right
    pushMatrix()
    translate(0.7*r, r, 0.8*r)
    rotateX(math.radians(-45))
    scale(1.5, 0.5, 1)
    sphere(0.2*r)
    popMatrix()
    
    pushMatrix()
    translate(-0.7*r, r, 0.8*r)
    rotateX(math.radians(-45))
    scale(1.5, 0.5, 1)
    sphere(0.2*r)
    popMatrix()
    
    # tail
    pushMatrix()
    translate(0, r, -r)
    scale(1.5, 1, 1)
    sphere(0.2*r)
    popMatrix()
    
    # black
    fill(0, 0, 0)
    
    # eyes
    pushMatrix()
    sphereDetail(60)
    translate(0.4*r, -1.2*r, 0.95*r)
    sphere(0.2*r)
    popMatrix()
    
    pushMatrix()
    sphereDetail(60)
    translate(-0.4*r, -1.2*r, 0.95*r)
    sphere(0.2*r)
    popMatrix()
    
    # gold
    fill(200, 200, 100)
    
    # horn
    pushMatrix()
    translate(-1.2*r, -1.75*r, 0)
    scale(0.15*r, 0.15*r, 0.15*r)
    spiral(1)
    popMatrix()
    
    pushMatrix()
    translate(1.2*r, -1.75*r, 0)
    scale(0.15*r, 0.15*r, 0.15*r)
    spiral(-1)
    popMatrix()
    
    # pushMatrix()
    # sphereDetail(60)
    # translate(0, -0.5*r, 1.15*r)
    # scale(1.2, 1, 1)
    # sphere(0.15*r)
    # popMatrix()
    
    # pink nose
    fill(255, 150, 175)
    
    pushMatrix()
    sphereDetail(60)
    translate(0, -0.85*r, 1.1*r)
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
        cylinder()
        popMatrix()
        theta += 0.1
    
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
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
    
def hand(r = 1.5):
    pushMatrix()
    translate (0, 0, 0)
    rotateY(math.radians(90))
    scale (r, r, r)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate (r, 0, 0)
    sphere(r)
    popMatrix()
    
    pushMatrix()
    translate (-r, 0, 0)
    sphere(r)
    popMatrix()

    