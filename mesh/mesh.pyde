# Anh Duong, Nguyen
from helper import *
rotate_flag = True    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation
vertices = []
corners = []
faces = []
randomMode = False
randomList = []
flatMode = True

def hasV(cid1, cid2, cid3, vid):
    global corners
    c1, c2, c3 = corners[cid1], corners[cid2], corners[cid3]
    if c1.vid == vid:
        return c1.cid
    if c2.vid == vid:
        return c2.cid
    if c3.vid == vid:
        return c3.cid
    return None

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current mesh
def draw():
    global time
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (100, 100, 100)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD DRAW THE MESH
    
    no_faces = len(faces)

    for i in range(no_faces):
        if randomMode:
            rcolor = randomList[i]
            fill(rcolor[0], rcolor[1], rcolor[2])

        vid1 = corners[3*i].vid
        vid2 = corners[3*i + 1].vid
        vid3 = corners[3*i + 2].vid

        if flatMode:
            n = faces[i].n
            beginShape()
            normal (n.x, n.y, n.z)
            vertex (vertices[vid1].x, vertices[vid1].y, vertices[vid1].z)
            vertex (vertices[vid2].x, vertices[vid2].y, vertices[vid2].z)
            vertex (vertices[vid3].x, vertices[vid3].y, vertices[vid3].z)
            endShape(CLOSE)
        else:
            beginShape()
            n = vertices[vid1].n
            normal (n.x, n.y, n.z)
            vertex (vertices[vid1].x, vertices[vid1].y, vertices[vid1].z)

            n = vertices[vid2].n
            normal (n.x, n.y, n.z)
            vertex (vertices[vid2].x, vertices[vid2].y, vertices[vid2].z)

            n = vertices[vid3].n
            normal (n.x, n.y, n.z)
            vertex (vertices[vid3].x, vertices[vid3].y, vertices[vid3].z)
            endShape(CLOSE)
    
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag, randomMode, flatMode, randomList
    fill(200, 200, 200)
    
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        # toggle per-vertex shading
        flatMode = not flatMode
    elif key == 'r':
        # randomly color faces
        randomMode = True
    elif key == 'w':
        # color faces white
        randomMode = False
        fill(200, 200, 200)
    elif key == 'd':
        dual()  # calculate the dual mesh
    elif key == 'q':
        exit()
        
    l = ['1', '2', '3', '4', '5', 'r', 'd']
    
    if key in l:
        randomList = []
        for _ in range(len(faces)):
            randomList.append((random()*255, random()*255, random()*255))

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    global vertices, corners, faces

    vertices, corners, faces = [], [], []

    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x, y, z = float(words[0]), float(words[1]), float(words[2])
        vertices.append(Vertex(x, y, z))
    
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        
        index1, index2, index3 = int(words[1]), int(words[2]), int(words[3])

        corners.append(Corner(3*i, index1, i, 3*i + 1, 3*i + 2))
        corners.append(Corner(3*i + 1, index2, i, 3*i + 2, 3*i))
        corners.append(Corner(3*i + 2, index3, i, 3*i, 3*i + 1))

        # face normal vector
        u = v_diff(vertices[index2], vertices[index1])
        v = v_diff(vertices[index3], vertices[index1])
        n = normalize(v_cross(u, v))

        # face centroid
        v1, v2, v3 = vertices[index1], vertices[index2], vertices[index3]
        cen = centroid(v1, v2, v3)

        faces.append(Face(i, 3*i, 3*i + 1, 3*i + 2, n, cen))

    opp_and_n()

def dual():
    global vertices, corners, faces
    newv, newc, newf = [], [], []

    num_vertices = len(vertices)
    num_faces = len(faces)

    for fid in range(num_faces):
        cen = faces[fid].cen
        newv.append(Vertex(cen.x, cen.y, cen.z))

    for vid in range(num_vertices):
        fids = swing(vid) # new vids
        cens = []
        for newvid in fids:
            cens.append(newv[newvid])

        sumx, sumy, sumz = 0, 0, 0
        for cen in cens:
            sumx += cen.x
            sumy += cen.y
            sumz += cen.z
        avg = Vertex(sumx/len(cens), sumy/len(cens), sumz/len(cens))

        newv.append(avg)
        index1 = len(newv) - 1
        newlength = len(fids) # len of new vids
        lf = len(newf)

        for j in range(newlength):
            i = j + lf
            index2 = fids[j]
            index3 = fids[(j + 1)%newlength]

            newc.append(Corner(3*i, index1, i, 3*i + 1, 3*i + 2))
            newc.append(Corner(3*i + 1, index2, i, 3*i + 2, 3*i))
            newc.append(Corner(3*i + 2, index3, i, 3*i, 3*i + 1))

            # face normal vector
            u = v_diff(newv[index2], newv[index1])
            v = v_diff(newv[index3], newv[index1])
            n = normalize(v_cross(u, v))

            # face centroid
            v1, v2, v3 = newv[index1], newv[index2], newv[index3]
            cen = centroid(v1, v2, v3)

            newf.append(Face(i, 3*i, 3*i + 1, 3*i + 2, n, cen))

    corners = newc
    vertices = newv
    faces = newf

    opp_and_n()

def swing(vid):
    fids = []
    num_faces = len(faces)

    # find the first fid
    for fid in range(num_faces):
        cid1, cid2, cid3 = faces[fid].cid1, faces[fid].cid2, faces[fid].cid3
        cid = hasV(cid1, cid2, cid3, vid)
        if cid != None:
            fids.append(fid)
            break

    opp = corners[corners[corners[cid].nid].oid]
    next_fid = opp.fid

    while next_fid != fids[0]:
        fids.append(next_fid)
        cid = opp.nid
        opp = corners[corners[corners[cid].nid].oid]
        next_fid = opp.fid

    return fids

def opp_and_n():
    # find opposite
    for a in corners:
        for b in corners:
            an, ap = corners[a.nid], corners[a.pid]
            bn, bp = corners[b.nid], corners[b.pid]
            if an.vid == bp.vid and ap.vid == bn.vid:
                a.oid = b.cid
                b.oid = a.cid

    num_vertices = len(vertices)

    for i in range(num_vertices):
        for c in corners:
            if c.vid == i:
                vn = vertices[corners[c.nid].vid]
                vp = vertices[corners[c.pid].vid]
                u = v_cross(vn, vp)
                vertices[i].n = v_sum(vertices[i].n, u)

        vertices[i].n = normalize(vertices[i].n)