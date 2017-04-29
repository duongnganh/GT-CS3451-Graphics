import math

class Scene:
    def __init__(self):
        self.fov = 0
        self.bg = (0, 0, 0)

class Light:
    def __init__(self, x, y, z, r, g, b):
        self.position = (x, y, z)
        self.color = (r, g, b)

class Surface:
    def __init__(self, Cdr, Cdg, Cdb, Car, Cag, Cab, Csr, Csg, Csb, P, Krefl):
        self.Cdr = Cdr
        self.Cdg = Cdg
        self.Cdb = Cdb

        self.Car = Car
        self.Cag = Cag
        self.Cab = Cab

        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb

        self.P = P
        self.Krefl = Krefl

    def getDisfuse(self):
        return (self.Cdr, self.Cdg, self.Cdb)

    def getAmbient(self):
        return (self.Car, self.Cag, self.Cab)

    def getSpecular(self):
        return (self.Csr, self.Csg, self.Csb)

class Ray:
    def __init__(self, x, y):
        self.d = x
        self.e = y

class Hit:
    def __init__(self, obj, pt, N, r):
        self.pt = pt
        self.obj = obj
        self.N = N
        self.ray = r

class Sphere:
    def __init__(self, radius, x, y, z, s):
        self.R = radius
        self.c = (x, y, z)
        self.surface = s
        self.type = "sphere"

    def get_n(self, pt):
        return normalize(v_diff(pt, self.c))[0]

class Tri:
    def __init__(self, s):
        self.a = None
        self.b = None
        self.c = None
        self.surface = s
        self.type = "tri"

    def add(self, x, y, z):
        if self.a == None:
            self.a = (x, y, z)
        elif self.b == None:
            self.b = (x, y, z)
        else:
            self.c = (x, y, z)

    def get_n(self, pt):
        u = v_diff(self.b, self.a)
        v = v_diff(self.c, self.a)
        n = normalize((-10*(u[1]*v[2] - u[2]*v[1]), -10*(u[2]*v[0] - u[0]*v[2]), -10*(u[0]*v[1] - u[1]*v[0])))[0]
        return n

def normalize(v):
    length = math.sqrt(v_dot_mul(v, v))
    return (v[0]/length, v[1]/length, v[2]/length), length
def v_const_mul(c, v):
    return (c*v[0], c*v[1], c*v[2])
def v_sum(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
def v_diff(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
def v_dot_mul(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def get_discriminant(d, e, c, R):
    v = v_diff(e, c)
    c1 = v_dot_mul(d, v)
    c2 = v_dot_mul(d, d) * (v_dot_mul(v, v) - R*R)
    return c1*c1 - c2
def get_t_sphere(d, e, c, dis):
    v = v_diff(e, c)
    c1 = v_dot_mul(d, v)
    c2 = v_dot_mul(d, d)
    return (-c1+math.sqrt(dis))/c2, (-c1-math.sqrt(dis))/c2

def det(m):
    return m[0][0]*m[1][1]*m[2][2] - m[0][0]*m[1][2]*m[2][1] - m[0][1]*m[1][0]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] - m[0][2]*m[1][1]*m[2][0]
def get_t_tri(a, b, c, e, detA):
    m = [[a[0] - b[0], a[0] - c[0], a[0] - e[0]], [a[1] - b[1], a[1] - c[1], a[1] - e[1]], [a[2] - b[2], a[2] - c[2], a[2] - e[2]]]
    return det(m)/detA
def get_B(a, e, c, d, detA):
    m = [[a[0] - e[0], a[0] - c[0], d[0]], [a[1] - e[1], a[1] - c[1], d[1]], [a[2] - e[2], a[2] - c[2], d[2]]]
    return det(m)/detA
def get_Y(a, b, e, d, detA):
    m = [[a[0] - b[0], a[0] - e[0], d[0]], [a[1] - b[1], a[1] - e[1], d[1]], [a[2] - b[2], a[2] - e[2], d[2]]]
    return det(m)/detA
def get_detA(a, b, c, d):
    m = [[a[0] - b[0], a[0] - c[0], d[0]], [a[1] - b[1], a[1] - c[1], d[1]], [a[2] - b[2], a[2] - c[2], d[2]]]
    return det(m)
