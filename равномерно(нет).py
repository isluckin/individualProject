from vpython import *
b = sphere(pos=vector(1,0,0), radius=0.5, color=color.red)
#def Speed(x):
#    speed = x.number
#    global v
#    v = speed

#winput(bind=Speed, prompt="Speed: ",type="numeric")
velocity = vector(0,0,0)
def sped(s):
    global velosity
    velosity = s.value
winput(bind=sped, prompt="Speed: ",type="numeric")

deltat = 0.005
t = 0
b.pos = b.pos + velocity * deltat
while t < 3:
    rate(100)
    b.pos = b.pos + velocity * deltat
    t = t + deltat
