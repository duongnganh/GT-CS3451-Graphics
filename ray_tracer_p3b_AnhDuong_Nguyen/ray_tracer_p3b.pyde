# Anh Duong. Nguyen
# Project 3B
from helper import *

objects = []
light = []
scene = Scene()

def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    print(key)
    # initialize global variable
    refresh() 
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global objects
    global light
    global scene
    surface = None
    obj = None

    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x, y, z = float(words[2]), float(words[3]), float(words[4])
            obj = Sphere(radius, x, y, z, surface)
            objects.append(obj)
        elif words[0] == 'fov':
            fov = float(words[1])
            scene.fov = fov
        elif words[0] == 'background':
            r, g, b = float(words[1]), float(words[2]), float(words[3])
            scene.bg = (r, g, b)
        elif words[0] == 'light':
            # light position
            x, y, z = float(words[1]), float(words[2]), float(words[3])
            # its color
            r, g, b = float(words[4]), float(words[5]), float(words[6])
            l = Light(x, y, z, r, g, b)
            light.append(l)
        elif words[0] == 'surface':
            Cdr, Cdg, Cdb = float(words[1]), float(words[2]), float(words[3])
            Car, Cag, Cab = float(words[4]), float(words[5]), float(words[6])
            Csr, Csg, Csb = float(words[7]), float(words[8]), float(words[9])
            P, Krefl = float(words[10]), float(words[11])
            surface = Surface(Cdr, Cdg, Cdb, Car, Cag, Cab, Csr, Csg, Csb, P, Krefl)
        elif words[0] == 'begin':
            obj = Tri(surface)
        elif words[0] == 'vertex':
            obj.add(float(words[1]), float(words[2]), float(words[3]))
        elif words[0] == 'end':
            objects.append(obj)
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    global scene

    # hardcode n, which is the distance from the viewing point to the plane
    n = 100.0
    
    top = math.tan(math.radians(scene.fov)/2) * n
    right = top/height * width

    for j in range(height):
        for i in range(width):
            # compute viewing ray
            u = -right + 2.0*right*(i + 0.5)/width
            v = -top + 2.0*top*(j + 0.5)/height
            ray = Ray((u, -v, -n), (0, 0, 0)) #flip v so that y axis points up

            # find first object hit by eye ray
            hit = get_hit_from_ray(ray)

            # calculate the color using the recursive raycolor function
            r, g, b = raycolor(hit, 0)
            pix_color = color(r, g, b)
            set(i, j, pix_color)       # fill the pixel with the calculated color

def get_hit_from_ray(ray, maxt = 100):
    global objects
    
    t = None

    for s in objects:
        if s.type == "sphere":
            dis = get_discriminant(ray.d, ray.e, s.c, s.R)
            if dis >= 0:
                t1, t2 = get_t_sphere(ray.d, ray.e, s.c, dis)

                # get rid of rounding error
                t1 = 0 if t1 < 0.0001 or t1 > maxt else t1
                t2 = 0 if t2 < 0.0001 or t2 > maxt else t2

                m = t1 + t2 if t1 * t2 == 0 else min(t1, t2)

                if (m > 0) and (t == None or t > m):
                    t = m
                    pt = v_sum(ray.e, v_const_mul(t, ray.d))
                    obj = s

        elif s.type == "tri":
            detA = get_detA(s.a, s.b, s.c, ray.d)
            if detA > 0:
                t1 = get_t_tri(s.a, s.b, s.c, ray.e, detA)
                B = get_B(s.a, ray.e, s.c, ray.d, detA)
                Y = get_Y(s.a, s.b, ray.e, ray.d, detA)
                # get rid of rounding error
                t1 = 0 if t1 < 0.0001 else t1
                if t1 > 0 and (t == None or t > t1) and Y >= 0 and Y <= 1 and B >= 0 and B <= 1-Y:
                    t = t1
                    pt = v_sum(ray.e, v_const_mul(t, ray.d))
                    obj = s
    
    if t == None:
        return None
    
    return Hit(obj, pt, obj.get_n(pt), ray)

def raycolor(hit, depth):
    global scene
    global light

    if hit == None:
        return scene.bg[0], scene.bg[1], scene.bg[2]

    phong, Krefl = hit.obj.surface.P, hit.obj.surface.Krefl
    v = normalize(v_diff(hit.ray.e, hit.pt))[0]

    a_color = (0, 0, 0)
    d_color = (0, 0, 0)
    s_color = (0, 0, 0)

    for l in light:
        L, maxt = normalize(v_diff(l.position, hit.pt))
        H = normalize(v_sum(v, L))[0]

        a_color = v_sum(a_color, l.color)

        shadow_hit = get_hit_from_ray(Ray(L, hit.pt), maxt)

        if (shadow_hit == None):
            cL = math.fabs(v_dot_mul(hit.N, L))
            d_color = v_sum(d_color, v_const_mul(cL, l.color))
            
            cH = math.fabs(v_dot_mul(hit.N, H))**phong
            s_color = v_sum(s_color, v_const_mul(cH, l.color))

    kd = hit.obj.surface.getDisfuse()
    ka = hit.obj.surface.getAmbient()
    ks = hit.obj.surface.getSpecular()

    r = v_dot_mul((ka[0], kd[0], ks[0]), (a_color[0], d_color[0], s_color[0]))
    g = v_dot_mul((ka[1], kd[1], ks[1]), (a_color[1], d_color[1], s_color[1]))
    b = v_dot_mul((ka[2], kd[2], ks[2]), (a_color[2], d_color[2], s_color[2]))
    res = (r, g, b)

    if Krefl > 0 and depth < 100:
        r_ray_d = v_diff(hit.ray.d, v_const_mul(2*v_dot_mul(hit.ray.d, hit.N), hit.N))
        r_ray = Ray(r_ray_d, hit.pt)
        r_color = v_const_mul(Krefl, raycolor(get_hit_from_ray(r_ray), depth+1))
        res = v_sum(res, r_color)

    return res

def refresh():
    global objects
    global light
    global scene
    objects = []
    light = []
    scene = Scene()
    
# should remain empty for this assignment
def draw():
    pass