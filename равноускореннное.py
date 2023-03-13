from vpython import *
scene.width = 2000
scene.height=1000
scene.camera.pos=vector(0,20,40)
a = vertex(pos = vector(-scene.width, -0.5, scene.width))
b = vertex(pos = vector(scene.width, -0.5, scene.width))
d = vertex(pos = vector(-scene.width,-0.5, -scene.width))
c = vertex(pos = vector(scene.width, -0.5, -scene.width))
Q = quad(vs=[a,b,c,d])
sph = sphere(color = color.red, pos = vector(0, 0, 0))
v0 = 0
a = 0.00005
t = 0
delta = 0.005
while t < 100:
    rate(100)
#    t = t+ delta
    t = t+1
    v = v0 + (a*t)
    s = (a*t*t)/2
    l = vector(s,0,0 )
    sph.pos = sph.pos + l
    print(v)

