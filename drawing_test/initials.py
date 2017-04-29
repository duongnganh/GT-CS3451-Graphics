# Nguyen, Anh Duong
# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective (60, -100, 100)
    gtPushMatrix()
    gtTranslate(0, 0, -4)
    gtRotateX(-30)
    draw_gt()
    gtPopMatrix()

def draw_gt():
    gtBeginShape ()

    gtVertex (1, 1, 0)
    gtVertex (-1, 1, 0)
    
    gtVertex (-1, 1, 0)
    gtVertex (-1, -1, 0)
    
    gtVertex (-1, -1, 0)
    gtVertex (1, -1, 0)
    
    gtVertex (0, 0, 0)
    gtVertex (2, 0, 0)
    
    gtVertex (1, 0, 0)
    gtVertex (1, -2, 0)
    
    gtEndShape()