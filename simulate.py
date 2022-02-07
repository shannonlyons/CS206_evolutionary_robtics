import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

pie = math.pi

for i in range (1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(robotId, "Torso_BackLeg", p.POSITION_CONTROL, random.uniform(-pie/2, pie/2), 50)
    pyrosim.Set_Motor_For_Joint(robotId, "Torso_FrontLeg", p.POSITION_CONTROL, random.uniform(-pie/2, pie/2), 50)
    time.sleep(1/60)

# save here
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

print('Back leg:')
print(backLegSensorValues)

print('Front leg:')
print(backLegSensorValues)

p.disconnect()