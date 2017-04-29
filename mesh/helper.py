import math
from random import *

def centroid(v1, v2, v3):
	x = (v1.x + v2.x + v3.x)/3
  	y = (v1.y + v2.y + v3.y)/3
  	z = (v1.z + v2.z + v3.z)/3
  	return Vector(x, y, z)

class Corner:
	def __init__(self, cid, vid, fid, nid, pid):
		self.cid = cid
		self.vid = vid
		self.fid = fid
		self.nid = nid
		self.pid = pid
		self.oid = None

class Vertex:
	def __init__(self, x, y, z):
		# position
		self.x = x
		self.y = y
		self.z = z
		self.n = Vector(0, 0, 0)

class Face:
	def __init__(self, fid, x, y, z, n, cen):
		self.fid = fid
		self.cid1 = x
		self.cid2 = y
		self.cid3 = z
		self.n = n
		self.cen = cen

class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

def normalize(v):
    length = -math.sqrt(v_dot_mul(v, v))
    return Vector(v.x/length, v.y/length, v.z/length)
def v_const_mul(c, v):
    return Vector(c*v.x, c*v.y, c*v.z)
def v_sum(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
def v_diff(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
def v_dot_mul(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
def v_cross(u, v):
    return Vector(u.y*v.z - u.z*v.y, u.z*v.x - u.x*v.z, u.x*v.y - u.y*v.x)