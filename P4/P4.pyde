# Project 4 base code (GPU shaders)

def setup():
    global catTexture, mountainTexture
    size(640, 640, P3D)
    noStroke()
    
    catTexture = loadImage("data/cat.png")
    mountainTexture = loadImage("data/green_mountain.jpg")
    
    loadShaders()

# load the vertex and fragment shaders (four of each)
def loadShaders():
    global shaders
    shaders = []
    for i in range(4):
        shader = loadShader("data/shader" + str(i) + ".frag", "data/shader" + str(i) + ".vert")
        shaders.append(shader)
        # pass

# draw the whole scene
def draw():
    
    noLights()
    background(0, 0, 0)
    camera (0, 0, 400, 0, 0, 0, 0, 1, 0)

    pushMatrix()
    
    # rotate the scene based on the mouse position
    dirY = (mouseY / float(height) - 0.5) * 2
    dirX = (mouseX / float(width) - 0.5) * 2
    rotate(-dirY, 1, 0, 0)
    rotate(dirX * 3, 0, 1, 0)
    
    # draw the various shaded quadrilaterals
    ground_plane()
    mandelbrot()
    edge_detection()
    green_mountain()
    swiss_cheese()
    
    popMatrix()

# Draw Quad 0 (Swiss Cheese)
def swiss_cheese():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[0])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 1 (Edge Detection)
def edge_detection():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[1])
    textureMode(NORMAL)
    beginShape()
    texture(catTexture)
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 2 (Mandelbrot Set)
def mandelbrot():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, -120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    textureMode(NORMAL)
    shader(shaders[2])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 3 (Green Mountain) -- You will need to modify this routine to chop up the quad into pieces
def green_mountain():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, -120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[3])
    textureMode(NORMAL)

    # change c to change the number of grids
    # there are c x c grids
    c = 40
    b = 200.0/c
    a = float(c)

    for i in range(c):
        for j in range(c):
            beginShape()
            texture(mountainTexture)
            vertex(b*i - 100, b*j - 100, 0, i/a, j/a)
            vertex(b*(i+1) - 100, b*j - 100, 0, (i+1)/a, j/a)
            vertex(b*(i+1) - 100, b*(j+1) - 100, 0, (i+1)/a, (j+1)/a)
            vertex(b*i - 100, b*(j+1) - 100, 0, i/a, (j+1)/a)
            endShape()

    popMatrix()

# Draw the ground plane
def ground_plane():
    noStroke()
    fill(200, 200, 200)
    pushMatrix()
    translate(0, 150, 0)
    rotate(PI/2, 1, 0, 0)
    scale(2.0, 2.0, 2.0)
    resetShader()  # de-activate any shader that was previously in use
    for i in range(-100, 100, 8):
        for j in range(-100, 100, 8):
            beginShape()
            vertex(i, j, 0, i/200 + 1, j/200 + 1)
            vertex(i + 8, j, 0, i/200 + 1.04, j/200 + 1)
            vertex(i + 8, j + 8, 0, i/200 + 1.04, j/200 + 1.04)
            vertex(i, j + 8, 0, i/200 + 1, j/200 + 1.04)
            endShape()
    popMatrix()