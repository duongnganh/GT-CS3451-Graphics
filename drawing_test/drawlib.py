# Nguyen, Anh Duong
# Drawing Routines, like OpenGL

from matlib import *

def gtOrtho(left, right, bottom, top, near, far):
    o = [[200.0/float(right-left), 0, 0, -float(right+left)/float(right-left)], 
         [0, 200.0/float(top-bottom), 0, -float(top+bottom)/float(top-bottom)], 
         [0, 0, 200.0/float(near-far), -float(near+far)/float(near-far)], 
         [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], o)

def gtPerspective(fov, near, far):
    const = math.tan(math.radians(fov)/2) * float(near)
    per = [[float(100.0*near)/const, 0, 0, 0], 
           [0, float(100.0*near)/const, 0, 0],
           [0, 0, float(far+near)/float(near-far), (200.0*far*near)/float(far-near)], 
           [0, 0, -1, 0]]
    gtStack[-1] = matrix_mul(gtStack[-1], per)

vertices = []
def gtBeginShape():
    del vertices[0:]

def gtEndShape():
    i = len(vertices) - 1
    while (i >= 0):
    	x1, y1, z1 = vertices.pop()
    	x2, y2, z2 = vertices.pop()
    	line(x1 + width/2, -y1 + height/2, x2 + width/2, -y2 + height/2)
    	i -= 2

def gtVertex(x, y, z):
    a, b, c, r = mul41(gtStack[-1], [x, y, z, 1])
    if r != 0:
        vertices.append((a/r,b/r,c/r))
    else:
        vertices.append((a,b,c))
    
def mul41(m1, m2):
    res = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            res[i] += m1[i][k] * m2[k]
    return res