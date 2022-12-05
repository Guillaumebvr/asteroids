import core
from pygame import Rect
import random



def targetCollision():
    for proj in core.memory("projectiles"):
        if core.memory('target').collidepoint(proj["position"].x, proj["position"].y) :
            #print("BOOM")
            core.memory("projectiles").remove(proj)
            core.memory("target", Rect(random.randint(50, 750), random.randint(50, 750), 50, 50))
            core.memory('score',core.memory('score')+1)

def drawTarget():
    core.Draw.rect((255, 0, 0), core.memory("target"))
    #P7 =(200,200)
    #P8 = (180,220)
#    P9 = (210,250)
 #   P10 = (195,270)
  #  P11 = (180,210)
   #  core.Draw.polygon((255,255,255),(P7,P8,P9,P10,P11))
    #mettre des random P4 P5 P6, pour faire 5 vecteurs pour mon polygon
    #core.Draw.polygon((255,255,255),)

#def targetmovement():
 #   Rect(random.randint(50, 750), random.randint(50, 750), 50, 50)


