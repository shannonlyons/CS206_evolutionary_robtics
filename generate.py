import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# size variables
length = 1
width = 1
height = 1

# box position variables
x = 0
y = 0
z = 0

# box2 position variables
x2 = 0
y2 = 0
z2 = 1

# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[length,width,height])

while z < 4:
    pyrosim.Send_Cube(name="Box00", pos=[0,0,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box10", pos=[1,0,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box20", pos=[2,0,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box01", pos=[0,1,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box11", pos=[1,1,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box21", pos=[2,1,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box02", pos=[0,2,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box12", pos=[1,2,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

z = 0
length = 1
width = 1
height = 1
while z < 4:
    pyrosim.Send_Cube(name="Box22", pos=[2,2,z], size=[length,width,height])
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    z = z + 1

pyrosim.End()
