# Nguyen, Anh Duong
# Matrix Stack Library -- Use your code from Project 1A

# Matrix Stack Library

# you should modify the routines below to complete the assignment
import math

gtStack = []

def gtInitialize():
    matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    del gtStack[0:len(gtStack)]
    gtStack.append(matrix)

def gtPushMatrix():
    top = gtStack[-1]
    gtStack.append(top)

def gtPopMatrix():
    if len(gtStack) <= 1:
        print("cannot pop the matrix stack")
    else:
        gtStack.pop()

def gtTranslate(x, y, z):
    t = [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], t)

def gtScale(x, y, z):
    s = [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], s)
    print "scale"
    print gtStack[-1]

def gtRotateX(theta):
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    r = [[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], r)

def gtRotateY(theta):
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    r = [[cos, 0, sin, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], r)

def gtRotateZ(theta):
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    r = [[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    gtStack[-1] = matrix_mul(gtStack[-1], r)

def print_ctm():
    top = gtStack[-1]
    for i in top:
        print i
    print "\n"

def matrix_mul(m1, m2):
    res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                res[i][j] += m1[i][k] * m2[k][j]
    return res